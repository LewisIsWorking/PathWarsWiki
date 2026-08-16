"""Campaign directory -> wiki code, and transcript file -> wiki filename.

Split from ``sync.py`` so the naming rules — the part with the sharp edge —
can be tested without touching a filesystem.

⛔ THE SHARP EDGE. Writerside ``.tree`` files reference topics by **bare
filename**, resolved recursively across ``topics/``:

    <toc-element topic="C06-Kibwe.md"/>

The source archive is ``data/pbp_logs/<Campaign>/<YYYY-MM>.md``, so ten
campaigns all own a file called ``2026-08.md``. Copied across unchanged
they would be ten different topics with one name, and Writerside would
resolve every reference to whichever it found first. Every published
filename is therefore prefixed with the campaign code and slug, and
``sync`` asserts uniqueness before writing anything.
"""

import json
import re

# Campaigns that have transcripts but are no longer in the bot's config,
# because they finished. Their history is still worth publishing, so they
# are named here rather than dropped. A directory that appears in neither
# config nor this map stops the sync — see ``resolve_campaigns``.
RETIRED = {
    "Dark_Pockets": ("C11", "Dark-Pockets"),
    "Magni_Watch": ("C04b", "Magni-Watch"),
}

# Directories under data/pbp_logs that are not campaigns at all.
NOT_A_CAMPAIGN = {"summaries"}

_MONTH = re.compile(r"^\d{4}-\d{2}$")


def sanitize_dirname(name: str) -> str:
    """Mirror of the bot's ``transcript.logger.sanitize_dirname``.

    Kept byte-identical in behaviour on purpose: it is how a config entry
    is matched to the directory the archiver created. If the bot ever
    changes its rule this must change with it, and
    ``test_directory_rule_matches_the_bot`` fails loudly if the two drift.
    """
    kept = "".join(c if c.isalnum() or c in (" ", "-", "_") else ""
                   for c in name)
    return kept.strip().replace(" ", "_")


def slug(name: str) -> str:
    """A campaign name as it should appear in a filename."""
    return sanitize_dirname(name).replace("_", "-")


def resolve_campaigns(config_text: str, present_dirs) -> tuple[dict, list]:
    """Map every transcript directory to ``(code, slug)``.

    Returns ``(mapping, unmapped)``. The caller is expected to treat a
    non-empty ``unmapped`` as a failure rather than skipping quietly:
    a new campaign whose transcripts silently fail to publish is exactly
    the kind of gap that reads as done. Checking both directions is what
    surfaced C10 (configured, no transcripts yet) and Dark_Pockets /
    Magni_Watch (transcripts, no config) in the first place.
    """
    mapping: dict[str, tuple[str, str]] = {}
    try:
        pairs = json.loads(config_text).get("topic_pairs", [])
    except (TypeError, ValueError):
        pairs = []
    for pair in pairs:
        name = pair.get("name") or ""
        code = pair.get("code") or "C??"
        if name:
            mapping[sanitize_dirname(name)] = (code, slug(name))
    mapping.update(RETIRED)

    unmapped = sorted(d for d in present_dirs
                      if d not in mapping and d not in NOT_A_CAMPAIGN)
    live = {d: mapping[d] for d in present_dirs if d in mapping}
    return live, unmapped


def published_name(code: str, campaign_slug: str, month: str) -> str:
    """Filename for one month of one campaign, unique across the wiki."""
    return f"{code}-{campaign_slug}-PBP-{month}.md"


def is_month_file(stem: str) -> bool:
    """True for ``2026-08``-shaped stems, which are the monthly logs.

    Anything else in a campaign directory (a README, a hand-written note)
    is left alone rather than published under a guessed name.
    """
    return bool(_MONTH.match(stem))


def title_for(code: str, campaign_slug: str, month: str) -> str:
    """Human title for the generated page and its TOC entry."""
    return f"{code} {campaign_slug.replace('-', ' ')} — {month}"
