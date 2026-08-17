"""Publish the bot's PBP transcript archive into this wiki.

The PathWarsNudge bot has been archiving every play-by-post message since
2023-08 into ``data/pbp_logs/<Campaign>/<YYYY-MM>.md`` in its own repo.
This copies that archive into ``Writerside/topics/Play-by-posts/Transcripts``
and regenerates ``Writerside/pbp.tree`` so the pages appear in the wiki.

⭐ **The bot's repo is the source of truth. Everything under
``Transcripts/`` is generated and will be overwritten.** Each published
page carries a banner saying so. To correct a transcript, fix it in the
bot repo; an edit made here survives exactly until the next sync.

One-way by design. A two-way sync would need this repo to hold a token
that can write to the bot's repo, and there is nothing here worth that
risk — the wiki is a published mirror, not a second master.

Idempotent: a run that changes nothing writes nothing, so the scheduled
workflow does not produce an empty commit every hour.
"""

import argparse
import sys
from pathlib import Path

from guards import _assert_unique, assert_no_duplicate_topics  # noqa: F401
from index import (campaign_index_name, render_campaign_index,
                   render_master_index)
from naming import (NOT_A_CAMPAIGN, is_month_file, published_name,
                    resolve_campaigns, title_for)
from publish import _body, _group_username, _year_of
from render import count_messages, date_span, speakers
from tree import render_tree

# The one page to link to from the rest of the wiki.
MASTER_INDEX = "PBP-Transcripts.md"

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent
TOPICS_DIR = WIKI_ROOT / "Writerside" / "topics"
OUT_DIR = TOPICS_DIR / "Play-by-posts" / "Transcripts"
TREE_PATH = WIKI_ROOT / "Writerside" / "pbp.tree"
# TOPICS_DIR is named rather than derived as OUT_DIR.parent.parent. The
# derived form was correct in production and wrong under test, where
# OUT_DIR is redirected to a tmp dir and walking up two levels landed on
# pytest's shared root — so the guard scanned other tests' fixtures and
# the source archive. A path computed by counting parents silently means
# something different the moment its base moves.



def _plan(source_root: Path, config_text: str):
    """Work out every (src, dest_name, code, slug, month) to publish."""
    dirs = sorted(d.name for d in source_root.iterdir() if d.is_dir())
    mapping, unmapped = resolve_campaigns(config_text, dirs)
    jobs = []
    for campaign_dir, (code, campaign_slug) in sorted(mapping.items()):
        for src in sorted((source_root / campaign_dir).glob("*.md")):
            if not is_month_file(src.stem):
                continue
            jobs.append((src, published_name(code, campaign_slug, src.stem),
                         code, campaign_slug, src.stem))
    return jobs, unmapped, dirs


def _write_indexes(by_campaign: dict, expected: set,
                   expected_paths: set) -> int:
    """Write the per-campaign and master index pages. Returns files written."""
    written = 0
    for (code, campaign_slug), months in by_campaign.items():
        name = campaign_index_name(code, campaign_slug)
        expected.add(name)
        body = render_campaign_index(code, campaign_slug, months)
        target = OUT_DIR / name
        expected_paths.add(target)
        if not target.exists() or target.read_text(encoding="utf-8") != body:
            target.write_text(body, encoding="utf-8")
            written += 1

    expected.add(MASTER_INDEX)
    body = render_master_index(by_campaign, [])
    target = OUT_DIR / MASTER_INDEX
    expected_paths.add(target)
    if not target.exists() or target.read_text(encoding="utf-8") != body:
        target.write_text(body, encoding="utf-8")
        written += 1
    return written


def sync(source_root: Path, config_text: str, *, prune: bool = True) -> int:
    """Publish the archive. Returns the number of files written."""
    jobs, unmapped, dirs = _plan(source_root, config_text)
    if unmapped:
        raise SystemExit(
            f"Transcript directories with no campaign mapping: {unmapped}.\n"
            f"A new campaign must be added to the bot's config (preferred, "
            f"it then maps automatically) or to naming.RETIRED if it has "
            f"finished. Refusing to sync rather than silently skip it — a "
            f"campaign whose history quietly fails to publish is worse "
            f"than a failed run.")
    _assert_unique(jobs)

    group_username = _group_username(config_text)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written, expected = 0, set()
    expected_paths: set[Path] = set()
    by_campaign: dict = {}
    for src, dest, code, campaign_slug, month in jobs:
        expected.add(dest)
        # Year folders: a human browsing the repo wants 2026/ not 173
        # files in one directory. Writerside resolves topics by bare
        # filename, so the nesting is free.
        target = OUT_DIR / _year_of(month) / dest
        expected_paths.add(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        raw = src.read_text(encoding="utf-8", errors="replace")
        body = _body(raw, code, campaign_slug, month, group_username)
        # ⚠️ Stats come from RAW, never from the rendered body. Rendering
        # rewrites exactly the lines these functions match, so counting
        # the output reports zero of everything — which it did, silently,
        # on the first run: "0 messages" across all ten campaigns, in a
        # table that otherwise looked perfectly correct.
        by_campaign.setdefault((code, campaign_slug), []).append(
            (month, dest, count_messages(raw), date_span(raw), speakers(raw)))
        # Compare before writing so an unchanged month does not churn the
        # git history every sync.
        if target.exists() and target.read_text(encoding="utf-8") == body:
            continue
        target.write_text(body, encoding="utf-8")
        written += 1

    written += _write_indexes(by_campaign, expected, expected_paths)

    removed = 0
    if prune:
        # ⚠️ Prune by PATH, not by basename. When the pages moved into
        # year folders the old flat copy and the new nested one shared a
        # name, so a name-based sweep kept both — and the duplicate-topic
        # guard then failed the whole run, correctly, on files this step
        # was supposed to have removed. A name is not an identity once
        # the same name can live in two places.
        #
        # rglob, not glob, for the same reason: a glob would have quietly
        # stopped pruning anything the moment the pages nested.
        for stale in OUT_DIR.rglob("*.md"):
            if stale not in expected_paths:
                stale.unlink()
                removed += 1
        for empty in sorted(OUT_DIR.rglob("*"), reverse=True):
            if empty.is_dir() and not any(empty.iterdir()):
                empty.rmdir()

    assert_no_duplicate_topics(TOPICS_DIR)

    tree = render_tree(jobs, MASTER_INDEX, campaign_index_name)
    if not TREE_PATH.exists() or TREE_PATH.read_text(encoding="utf-8") != tree:
        TREE_PATH.write_text(tree, encoding="utf-8")
        written += 1

    print(f"{len(jobs)} transcript(s) across {len(dirs)} source directories; "
          f"{written} file(s) written, {removed} pruned.")
    skipped = sorted(d for d in dirs if d in NOT_A_CAMPAIGN)
    if skipped:
        # Say what was skipped and why. A silent exclusion reads as
        # "covered everything" when it did not.
        print(f"Skipped (not campaigns): {skipped}")
    return written


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", required=True,
                    help="path to the bot repo's data/pbp_logs directory")
    ap.add_argument("--config", required=True,
                    help="path to the bot repo's config.json")
    ap.add_argument("--no-prune", action="store_true",
                    help="keep generated pages whose source has vanished")
    args = ap.parse_args(argv)
    sync(Path(args.source), Path(args.config).read_text(encoding="utf-8"),
         prune=not args.no_prune)
    return 0


if __name__ == "__main__":
    sys.exit(main())
