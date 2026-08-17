"""Turn a raw transcript line into something a person wants to read.

The archive stores each message as::

    **Ryo Yamakawa** (2026-08-15 07:51:12) msg#172171@40585:
    "Next. Next we stop those psychos and protect our city."

That header is written for machines. Every line repeats the full date the
day heading already gave, the seconds nobody needs, and a nine-digit
message id followed by a five-digit thread id. Across 79,000 lines it is
most of what the eye has to skip.

Published, the same line becomes::

    **Ryo Yamakawa** · 07:51 · [↗](https://t.me/Path_Wars/40585/172171)

⭐ The id is not dropped, it is **spent**. Those two numbers are exactly
what a t.me deep link needs, so the noisiest part of the line turns into
the one thing the wiki could not otherwise offer: a jump straight to the
message in Telegram.

⚠️ Message ids only exist from 2026 onward — the archiver started writing
``msg#`` markers this year. Earlier lines have name and timestamp only,
so they render without a link rather than with a broken one.
"""

import re

# **Name** [GM] (2026-08-15 07:51:12) msg#172171@40585:
# and the pre-2026 shape, which has no msg# suffix.
_HEADER = re.compile(
    r"^\*\*(?P<who>[^*]+)\*\*"
    r"(?P<gm>\s*\[GM\])?"
    r"\s*\((?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}):\d{2}\)"
    r"(?:\s*msg#(?P<mid>\d+)@(?P<thread>\d+))?"
    r":\s*$")


def is_message_header(line: str) -> bool:
    """True for a line that introduces a message."""
    return _HEADER.match(line) is not None


def render_header(line: str, group_username: str) -> str:
    """Rewrite one message header. Returns the line unchanged if unmatched.

    Unchanged-on-no-match is deliberate. A transcript line this does not
    recognise is still someone's words, and dropping or mangling it would
    be far worse than leaving it in its raw form — which is, after all,
    exactly what every page looked like before this existed.
    """
    m = _HEADER.match(line)
    if not m:
        return line
    who = m.group("who").strip()
    parts = [f"**{who}**"]
    if m.group("gm"):
        parts.append("*(GM)*")
    parts.append("·")
    parts.append(m.group("time"))
    if m.group("mid") and group_username:
        link = (f"https://t.me/{group_username}/"
                f"{m.group('thread')}/{m.group('mid')}")
        parts.append(f"· [↗]({link})")
    return " ".join(parts)


def render_body(text: str, group_username: str) -> str:
    """Rewrite every message header in a transcript, body untouched.

    Only lines matching the header shape are rewritten. Everything else —
    prose, images, week and day headings, the archiver's own notes — is
    passed through byte for byte, so the published page can never say
    something the archive did not.
    """
    return "\n".join(render_header(line, group_username)
                     for line in text.splitlines())


def count_messages(text: str) -> int:
    """How many messages a transcript holds. Used for the index pages,
    and as the check that rendering never loses one."""
    return sum(1 for line in text.splitlines() if is_message_header(line))


def speakers(text: str) -> list[str]:
    """Distinct speakers in a transcript, in first-appearance order.

    Shown on the index so a reader can tell at a glance whose month it
    was, and which campaign a half-remembered name belongs to.
    """
    seen: list[str] = []
    for line in text.splitlines():
        m = _HEADER.match(line)
        if not m:
            continue
        who = m.group("who").strip()
        if who not in seen:
            seen.append(who)
    return seen


def date_span(text: str) -> tuple[str, str] | None:
    """First and last dates appearing in the transcript, or None."""
    dates = [m.group("date") for m in
             (_HEADER.match(line) for line in text.splitlines()) if m]
    return (dates[0], dates[-1]) if dates else None
