"""The two collision guards. Writerside fails silently without them.

Extracted from ``sync.py`` on 2026-08-17 at 278 lines. They belong
together: both exist because Writerside resolves ``.tree`` topics by
BARE FILENAME across the whole ``topics/`` tree, so two pages sharing a
name do not error — one of them simply never gets published, and nothing
anywhere says so.

``_assert_unique`` covers the pages this run is about to write.
``assert_no_duplicate_topics`` covers the entire wiki, which is the one
that matters: a generated page colliding with a hand-written one is just
as silent and far easier to introduce, because whoever adds the
hand-written page has no reason to look here.
"""

from pathlib import Path


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
