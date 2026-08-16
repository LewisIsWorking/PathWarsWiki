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

from naming import (NOT_A_CAMPAIGN, is_month_file, published_name,
                    resolve_campaigns, title_for)
from tree import render_tree

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

BANNER = (
    "> ⚠️ **Generated page — do not edit here.**\n"
    "> This transcript is archived automatically by the PathWarsNudge bot\n"
    "> and copied into the wiki. Any change made on this page is lost on\n"
    "> the next sync. Fix it in the bot's `data/pbp_logs/` instead.\n"
    "{#generated-banner}\n\n")


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


def _assert_unique(jobs) -> None:
    """No two published pages may share a filename.

    Writerside resolves ``.tree`` topics by bare filename across the whole
    topics tree, so a collision does not error — it silently points every
    reference at one of the twins. Fail here instead.
    """
    seen: dict[str, Path] = {}
    for src, dest, *_ in jobs:
        if dest in seen:
            raise SystemExit(
                f"Filename collision: {dest} would be written from both "
                f"{seen[dest]} and {src}. Writerside resolves topics by "
                f"bare filename, so this would silently publish one and "
                f"hide the other.")
        seen[dest] = src


def assert_no_duplicate_topics(topics_root: Path) -> None:
    """No two .md files anywhere under topics/ may share a basename.

    ``_assert_unique`` only compares the pages this script is about to
    write. This is the wider invariant, and it is the one that actually
    protects the wiki: Writerside resolves ``.tree`` topics by bare
    filename across the WHOLE topics tree, so a generated page colliding
    with a hand-written one is just as silent as two generated pages
    colliding with each other — and far easier to introduce, because the
    person adding the hand-written page has no reason to look here.

    Checked after writing, over the real tree, so it cannot be fooled by
    a stale plan.
    """
    seen: dict[str, Path] = {}
    clashes = []
    for path in topics_root.rglob("*.md"):
        other = seen.get(path.name)
        if other is not None:
            clashes.append((path.name, other, path))
        seen[path.name] = path
    if clashes:
        lines = "\n".join(f"  {n}: {a} and {b}" for n, a, b in clashes)
        raise SystemExit(
            f"Duplicate topic filenames under {topics_root}:\n{lines}\n"
            f"Writerside resolves topics by bare filename, so one of each "
            f"pair would silently never be published. Rename one.")


def _body(src: Path, code: str, campaign_slug: str, month: str) -> str:
    """The published page: a title, the banner, then the archive verbatim.

    The source's own ``# Campaign — YYYY-MM`` heading is dropped so the
    page has exactly one H1, which is what Writerside wants.
    """
    raw = src.read_text(encoding="utf-8", errors="replace")
    lines = raw.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return (f"# {title_for(code, campaign_slug, month)}\n\n"
            + BANNER + "\n".join(lines).lstrip("\n") + "\n")


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

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written, expected = 0, set()
    for src, dest, code, campaign_slug, month in jobs:
        expected.add(dest)
        target = OUT_DIR / dest
        body = _body(src, code, campaign_slug, month)
        # Compare before writing so an unchanged month does not churn the
        # git history every hour.
        if target.exists() and target.read_text(encoding="utf-8") == body:
            continue
        target.write_text(body, encoding="utf-8")
        written += 1

    removed = 0
    if prune:
        # Only ever inside Transcripts/, which this script owns entirely.
        # Hand-written pages live one level up in Play-by-posts/ and are
        # never touched.
        for stale in OUT_DIR.glob("*.md"):
            if stale.name not in expected:
                stale.unlink()
                removed += 1

    assert_no_duplicate_topics(TOPICS_DIR)

    tree = render_tree(jobs)
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
