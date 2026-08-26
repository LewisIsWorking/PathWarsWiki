"""Index pages, because 173 files in a sidebar is not navigation.

Two levels:

* one page per campaign — every month it ran, with message counts, the
  dates covered and who spoke, so a reader can find the month they half
  remember without opening six of them;
* one page over everything — campaigns by span and volume, and a
  chronological view across all of them at once, which is the thing the
  per-campaign pages cannot show.

⭐ Counts come from parsing the published text, not from a tally kept
alongside it. A number maintained separately from the thing it counts
drifts the first time anything else changes, and nothing notices.
"""

from collections import defaultdict

GENERATED = (
    "> ⚠️ **Generated page — do not edit here.**\n"
    "> Rebuilt from the PathWarsNudge bot's archive on every sync.\n"
    "{#generated-banner}\n\n")


def _month_name(month: str) -> str:
    """``2026-08`` -> ``Aug 2026``."""
    names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    year, mon = month.split("-")
    return f"{names[int(mon)]} {year}"


def campaign_index_name(code: str, campaign_slug: str) -> str:
    return f"{code}-{campaign_slug}-PBP-Index.md"


def render_campaign_index(code: str, campaign_slug: str, months: list) -> str:
    """One campaign's months, newest first.

    ``months`` is a list of ``(month, dest_name, message_count, span,
    speakers)``.
    """
    title = f"{code} {campaign_slug.replace('-', ' ')} — transcript index"
    total = sum(m[2] for m in months)
    lines = [f"# {title}\n", GENERATED]
    lines.append(f"**{len(months)} month(s)**, **{total:,} messages** "
                 f"archived by the PathWarsNudge bot.\n")
    lines.append("| Month | Messages | Dates covered | Voices |")
    lines.append("|---|---:|---|---|")
    for month, dest, count, span, who in sorted(months, reverse=True):
        covered = f"{span[0]} → {span[1]}" if span else "—"
        names = ", ".join(who[:4]) + ("…" if len(who) > 4 else "")
        lines.append(f"| [{_month_name(month)}]({dest}) | {count:,} | "
                     f"{covered} | {names or '—'} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def render_master_index(by_campaign: dict, summaries: list) -> str:
    """Every campaign, plus a chronological view across all of them."""
    lines = ["# Play-by-post transcripts\n", GENERATED]
    total = sum(m[2] for months in by_campaign.values() for m in months)
    lines.append(
        f"Every play-by-post message the PathWarsNudge bot has archived: "
        f"**{total:,} messages** across **{len(by_campaign)} campaigns**, "
        f"the oldest from **{_earliest(by_campaign)}**.\n")
    lines.append("## Campaigns\n")
    lines.append("| Campaign | Months | Messages | First | Latest |")
    lines.append("|---|---:|---:|---|---|")
    for (code, slug), months in sorted(by_campaign.items()):
        ordered = sorted(m[0] for m in months)
        idx = campaign_index_name(code, slug)
        name = f"{code} {slug.replace('-', ' ')}"
        lines.append(f"| [{name}]({idx}) | {len(months)} | "
                     f"{sum(m[2] for m in months):,} | "
                     f"{_month_name(ordered[0])} | {_month_name(ordered[-1])} |")

    if summaries:
        lines.append("\n## Monthly write-ups\n")
        lines.append(
            "Narrative summaries of what actually happened, rather than "
            "the raw logs.\n")
        for month, dest, label in sorted(summaries, reverse=True):
            lines.append(f"- [{_month_name(month)} — {label}]({dest})")

    lines.append("\n## Everything, month by month\n")
    lines.append(
        "The same transcripts read across campaigns instead of down one, "
        "which is how a month actually happened.\n")
    for month, entries in sorted(_by_month(by_campaign).items(), reverse=True):
        pretty = " · ".join(
            f"[{code}]({dest})" for code, dest in sorted(entries))
        lines.append(f"- **{_month_name(month)}** — {pretty}")
    lines.append("")
    return "\n".join(lines) + "\n"


def _by_month(by_campaign: dict) -> dict:
    """Regroup campaign months into ``{month: [(code, dest), ...]}``."""
    out = defaultdict(list)
    for (code, _slug), months in by_campaign.items():
        for month, dest, *_rest in months:
            out[month].append((code, dest))
    return out


def _earliest(by_campaign: dict) -> str:
    months = [m[0] for months in by_campaign.values() for m in months]
    return _month_name(min(months)) if months else "—"
