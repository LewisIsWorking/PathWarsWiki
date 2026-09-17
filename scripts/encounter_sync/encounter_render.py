"""One encounter record rendered as a wiki page, in the style of the hand-written ones.

The layout copies ``C09-Intro-Combat-Captain-Vex-Ashburn.md``: a quoted
COMBAT header, numbered ``>>`` lists, and a ``## Round N.`` section per
round. Only what Foundry and the bot know is here: the header, initiative,
allies with their players, enemies, and each round's health bands as they
were posted. Narration, misses and movement stay the GM's to write by hand.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

# The group plays on UK time, and the hand-written pages use it.
TZ = ZoneInfo("Europe/London")

BANNER = ("> ⚙️ Generated from Foundry by the Path Wars Nudge bot. An edit here is overwritten on the next "
          "sync; add narration to a hand-written page instead.")


def slug(text: str) -> str:
    """``Captain Vex Ashburn`` to ``Captain-Vex-Ashburn``: letters, digits and single hyphens."""
    words = "".join(ch if ch.isalnum() else " " for ch in text).split()
    return "-".join(words) or "Encounter"


def page_name(record: dict) -> str:
    """``C09-Combat-Captain-Vex-Ashburn-2026-09-13.md``. The date keeps two fights on one scene apart."""
    day = str(record.get("started_at") or "")[:10] or "undated"
    return f"{record['code']}-Combat-{slug(record.get('name') or 'Encounter')}-{day}.md"


def _text(value) -> str:
    """Plain text safe in Writerside markdown: no tags, no stray list markers."""
    return str(value).replace("<", "&lt;").replace(">", "&gt;").strip()


def _ordinal(day: int) -> str:
    suffix = "th" if 11 <= day % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"


def when(iso: str | None) -> str:
    """``2026 September 13th at 20:49``, in UK time as the hand-written pages have it."""
    if not iso:
        return "unknown"
    moment = datetime.fromisoformat(iso).astimezone(TZ)
    return f"{moment.year} {moment:%B} {_ordinal(moment.day)} at {moment:%H:%M}"


def _numbered(lines: list[str]) -> list[str]:
    return [f">> {i}. {line}" for i, line in enumerate(lines, 1)] or [">> 1. None."]


def _dot(text: str) -> str:
    return text if text.endswith((".", "!", "?")) else f"{text}."


def render_page(record: dict) -> str:
    rounds = record.get("rounds") or 0
    header = [
        f"Encounter name: {_dot(_text(record.get('name') or 'Encounter'))}",
        f"Encounter location: {_dot(_text(record.get('location') or 'unknown'))}",
        f"Encounter started = {when(record.get('started_at'))}.",
        (f"Encounter ended = {when(record.get('ended_at'))}, after {rounds} {'round' if rounds == 1 else 'rounds'}."
         if record.get("ended") else f"Still running: round {rounds}."),
    ]
    initiative = [_dot(f"{_text(c['name'])} {c['initiative']:g}" + (f" {_text(c['player'])}" if c.get("player") else ""))
                  for c in record.get("initiative", [])]
    allies = [_dot(_text(a["name"]) + (f" {_text(a['player'])}" if a.get("player") else ""))
              for a in record.get("allies", [])]
    enemies = [_dot(_text(e)) for e in record.get("enemies", [])]

    out = [f"# {page_name(record)[:-3]}", "", BANNER, "", "> COMBAT.", *_numbered(header), "",
           "> Initiative.", *_numbered(initiative), "", "> Allies.", *_numbered(allies), "",
           "> Enemies.", *_numbered(enemies)]
    by_round: dict[int, list[str]] = {}
    for hit in record.get("hits", []):
        by_round.setdefault(hit.get("round") or 0, []).append(_dot(_text(hit.get("text", ""))))
    for number in sorted(by_round):
        label = f"Round {number}" if number else "Before round 1"
        out += ["", f"## {label}.", "", f"> {label}: Hits.", *_numbered(by_round[number])]
    return "\n".join(out) + "\n"
