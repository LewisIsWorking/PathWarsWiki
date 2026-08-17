"""Building one published page from one archived month.

Extracted from ``sync.py`` on 2026-08-17 at 278 lines. ``sync`` keeps the
orchestration — what to publish, in what order, and what to delete — and
this answers the narrower question of what a single page looks like.
"""

import json

from naming import title_for
from render import render_body

BANNER = (
    "> ⚠️ **Generated page — do not edit here.**\n"
    "> This transcript is archived automatically by the PathWarsNudge bot\n"
    "> and copied into the wiki. Any change made on this page is lost on\n"
    "> the next sync. Fix it in the bot's `data/pbp_logs/` instead.\n"
    "{#generated-banner}\n\n")


def _body(raw: str, code: str, campaign_slug: str, month: str,
          group_username: str) -> str:
    """The published page: a title, the banner, then the rendered archive.

    Takes the raw TEXT rather than a path, so the caller reads the source
    once and can compute its stats from the same string it renders. When
    this took a path the caller had nothing but the rendered output to
    count, and counted zero.

    The source's own ``# Campaign — YYYY-MM`` heading is dropped so the
    page has exactly one H1, which is what Writerside wants.

    Only message *headers* are rewritten (see ``render``); every other
    line passes through byte for byte, so a published page can never say
    something the archive did not.
    """
    lines = raw.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = render_body("\n".join(lines).lstrip("\n"), group_username)
    return f"# {title_for(code, campaign_slug, month)}\n\n" + BANNER + body + "\n"


def _year_of(month: str) -> str:
    """``2026-08`` -> ``2026``. Year folders are for humans reading the
    repo; Writerside resolves topics by bare filename and does not care
    where they sit."""
    return month.split("-")[0]


def _group_username(config_text: str) -> str:
    """The t.me handle used to build permalinks. Empty means no links.

    Empty is a real outcome, not a failure: without a handle the group
    has no public URL, so a link would be broken. render_header omits it
    rather than emitting one that goes nowhere.
    """
    try:
        return json.loads(config_text).get("group_username") or ""
    except (TypeError, ValueError):
        return ""
