"""Read one campaign's transcript archive into numbered messages.

The archive is ``data/pbp_logs/<Campaign>/<YYYY-MM>.md`` in the bot repo,
the same source ``scripts/pbp_sync`` publishes. Each month's messages are
numbered from 1 in order, and that ``(month, n)`` pair is how a scene
names its first and last message. It is stable: the archive only ever
appends, so message 12 of 2026-06 stays message 12.

⚠️ Only the latest month can still grow. ``extract`` re-reads it when its
count changes; earlier months are fixed.
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

# Same header shape as pbp_sync.render._HEADER, with seconds kept: IRL
# durations are measured between messages, and nothing is gained by
# rounding them before the arithmetic.
_HEADER = re.compile(
    r"^\*\*(?P<who>[^*]+)\*\*"
    r"(?P<gm>\s*\[GM\])?"
    r"\s*\((?P<stamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\)"
    r"(?:\s*msg#(?P<mid>\d+)@(?P<thread>\d+))?"
    r":\s*$")
_MONTH_FILE = re.compile(r"^\d{4}-\d{2}\.md$")
# "## Week 23 (Jun 01-Jun 07)" and "### 📅 Tuesday, Jun 02".
_HEADING = re.compile(r"^#{2,3} ")


@dataclass(frozen=True)
class Message:
    month: str          # "2026-06"
    n: int              # 1-based position within the month
    who: str
    gm: bool
    at: datetime        # UTC, as the bot archived it
    text: str
    link: str | None    # t.me deep link; ids only exist from 2026


def parse_month(month: str, text: str, group_username: str) -> list[Message]:
    """Split one month's transcript into messages, in order."""
    out: list[Message] = []
    head = None
    body: list[str] = []

    def flush():
        if head is None:
            return
        link = None
        if head.group("mid"):
            link = (f"https://t.me/{group_username}/"
                    f"{head.group('thread')}/{head.group('mid')}")
        out.append(Message(
            month=month, n=len(out) + 1, who=head.group("who").strip(),
            gm=bool(head.group("gm")),
            at=datetime.strptime(head.group("stamp"), "%Y-%m-%d %H:%M:%S"),
            text="\n".join(body).strip(), link=link))

    for line in text.splitlines():
        m = _HEADER.match(line)
        if m:
            flush()
            head, body = m, []
        elif head is not None and not _HEADING.match(line):
            # Day and week headings belong to the archive, not a message.
            body.append(line)
    flush()
    return out


def read_campaign(directory: Path, group_username: str) -> dict[str, list[Message]]:
    """Every month of a campaign, oldest first, keyed by ``YYYY-MM``."""
    months = sorted(p for p in directory.iterdir() if _MONTH_FILE.match(p.name))
    return {p.stem: parse_month(p.stem, p.read_text(encoding="utf-8"),
                                group_username)
            for p in months}
