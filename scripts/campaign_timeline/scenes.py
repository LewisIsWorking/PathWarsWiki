"""The model's job, and the checks that decide whether to believe it.

A free model reads one month of numbered messages and splits it into
scenes: where the party was, from which message to which, what happened,
and any in-game time the posts actually state.

⛔ Nothing it returns is trusted on its word. ``validate`` rejects a
month whose scenes do not cover every message exactly once and in order,
and drops any time cue that is not a real quote from that month. A
rejected month is retried, never patched up: a timeline that quietly
skips messages would be wrong in a way nobody reading it could see.
"""

import json
import re

from messages import Message

# Long posts are cut for the prompt. Location and events are almost always
# clear from the opening of a post, and whole months must fit one request.
_EXCERPT = 500
_DESTROYED = chr(0xFFFD)

PROMPT = """You are indexing a play-by-post tabletop RPG transcript (one month).
Messages are numbered. Split them into consecutive SCENES by LOCATION: a new
scene starts only when the characters move somewhere else.

Rules:
- Every message belongs to exactly one scene. Scenes are in order, the first
  starts at message 1, each next scene starts right after the previous one
  ends, and the last ends at message {count}.
- "area": the wider place (a building, dungeon, ship, district or town), max
  6 words, as the posts name it.
- "location": the specific room or spot inside that area, max 6 words. If
  the posts name no smaller spot, repeat the area.
- A new scene starts when the area OR the location changes.
- If the party is at a place already listed below, reuse those EXACT names.
- "events": 1 to 6 plain one-line summaries of what happened there, each
  with "at", the message number it happened in. Past tense. No invention.
- "time_cues": in-game time the posts STATE, copied word for word (for
  example "the next morning", "Day 3", "8 hours later"). Empty list if none.
  Never estimate.
- Out-of-character chatter stays in whatever scene it falls in.

Where the party is when this month starts: {current}
Keep that location until the posts show the characters actually moving. A
new month is NOT a move.

Locations already used in this campaign:
{known}

Write every non-ASCII character as a JSON escape, for example
"B\\u00e1yakan" for the accented name. Reply with ONLY this JSON, no prose,
no code fence:
{{"scenes": [{{"first": 1, "last": 9, "area": "...", "location": "...",
  "events": [{{"at": 2, "text": "..."}}], "time_cues": ["..."]}}]}}

Messages ({count}):
{messages}
"""


def build_prompt(messages: list[Message], known_locations: list[str],
                 current: str | None = None) -> str:
    """The prompt for one month.

    ⚠️ ``current`` is where the previous month ended. Without it, the C04
    pilot (2026-09-16) moved to Room 9 in July and then snapped back to the
    first place on the list for August, events in Room 9 and all: the model
    had no way to know a month boundary is not a change of scene.
    """
    lines = []
    for m in messages:
        body = " ".join(m.text.split())
        if len(body) > _EXCERPT:
            body = body[:_EXCERPT] + " [...]"
        role = " (GM)" if m.gm else ""
        lines.append(f"{m.n}. [{m.at:%Y-%m-%d %H:%M}] {m.who}{role}: {body}")
    known = "\n".join(f"- {name}" for name in known_locations) or "- (none yet)"
    return PROMPT.format(count=len(messages), known=known,
                         current=current or "unknown (start of the campaign)",
                         messages="\n".join(lines))


def parse_reply(reply: str) -> dict:
    """The JSON object in a model reply, tolerating a stray fence or preamble.

    ⛔ A replacement character means something was destroyed on the way
    back. In the C04 pilot (2026-09-16) "Báyakan" arrived with its accent
    gone. The prompt asks for escapes so the reply is pure ASCII; a reply
    that ignored that and got damaged is rejected and retried, never saved.
    """
    if _DESTROYED in reply:
        raise ValueError("reply contains a destroyed character (U+FFFD)")
    # The FIRST complete object, not first "{" to last "}". C05's grouping
    # reply (2026-09-17) carried a second JSON snippet after the answer, and
    # slicing to the last brace failed with "Extra data".
    start = reply.find("{")
    if start < 0:
        raise ValueError("no JSON object in the reply")
    value, _end = json.JSONDecoder().raw_decode(reply, start)
    return value


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def validate(data: dict, messages: list[Message]) -> tuple[list[dict], list[str]]:
    """Check a month's scenes. Returns ``(scenes, dropped_cues)``.

    Raises ``ValueError`` when the scene boundaries are wrong, since those
    cannot be repaired without guessing. Time cues that are not quotes are
    dropped and reported rather than failing the month: the scene split is
    still good, and an invented cue is worse than a missing one.
    """
    count = len(messages)
    scenes = data.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        raise ValueError("no scenes")
    source = _norm(" ".join(m.text for m in messages))
    expected_first, clean, dropped = 1, [], []
    for i, s in enumerate(scenes):
        first, last = s.get("first"), s.get("last")
        if not (isinstance(first, int) and isinstance(last, int)):
            raise ValueError(f"scene {i + 1}: first/last must be integers")
        if first != expected_first or last < first or last > count:
            raise ValueError(f"scene {i + 1} spans {first}-{last}, "
                             f"expected to start at {expected_first}")
        area = str(s.get("area") or "").strip()
        location = str(s.get("location") or "").strip() or area
        if not area:
            raise ValueError(f"scene {i + 1}: no area")
        events = []
        for e in s.get("events") or []:
            text = str(e.get("text") or "").strip()
            at = e.get("at")
            if text and isinstance(at, int) and first <= at <= last:
                events.append({"at": at, "text": text})
        if not events:
            raise ValueError(f"scene {i + 1} ({location}): no usable events")
        cues = []
        for cue in s.get("time_cues") or []:
            (cues if _norm(str(cue)) and _norm(str(cue)) in source
             else dropped).append(str(cue))
        clean.append({"first": first, "last": last, "area": area,
                      "location": location,
                      "events": events, "time_cues": cues})
        expected_first = last + 1
    if expected_first != count + 1:
        raise ValueError(f"scenes end at {expected_first - 1}, not {count}")
    return clean, dropped
