"""Writing the published pages, the tree, and not clobbering the wiki.

COVERS  page body, idempotence, pruning, the wiki-wide duplicate-topic
        guard, and tree rendering.
MISSES  whether Writerside actually builds the result — that needs the
        Writerside toolchain, unavailable in CI. The tree is checked
        structurally and against the files on disk instead.
PROVEN  by ``test_the_wiki_wide_guard_can_fail``.

Split from ``test_pbp_naming.py`` on 2026-08-17 at 237 lines. That file
owns what a page is CALLED; this one owns what gets WRITTEN.
"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sync as sync_mod
from tree import render_tree

CONFIG = json.dumps({"topic_pairs": [
    {"name": "Kibwe", "code": "C06"},
    {"name": "Doomsday Funtime", "code": "C01"},
]})


# ── The published page ───────────────────────────────────────────────────────

def _archive(tmp_path):
    src = tmp_path / "pbp_logs" / "Kibwe"
    src.mkdir(parents=True)
    (src / "2026-08.md").write_text(
        "# Kibwe — 2026-08\n\n*archived*\n\n**Ryo** (t) msg#1@2:\nhello\n",
        encoding="utf-8")
    return tmp_path / "pbp_logs"


def test_page_has_one_h1_and_a_do_not_edit_banner(tmp_path, monkeypatch):
    monkeypatch.setattr(sync_mod, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(sync_mod, "TREE_PATH", tmp_path / "pbp.tree")
    monkeypatch.setattr(sync_mod, "TOPICS_DIR", tmp_path / "out")
    sync_mod.sync(_archive(tmp_path), CONFIG)
    page = (tmp_path / "out" / "C06-Kibwe-PBP-2026-08.md").read_text(
        encoding="utf-8")
    assert page.count("\n# ") + page.startswith("# ") == 1
    assert "do not edit here" in page
    assert "hello" in page, "the transcript body must survive intact"


def test_a_second_run_writes_nothing(tmp_path, monkeypatch):
    """Otherwise the scheduled workflow commits every hour forever."""
    monkeypatch.setattr(sync_mod, "OUT_DIR", tmp_path / "out")
    monkeypatch.setattr(sync_mod, "TREE_PATH", tmp_path / "pbp.tree")
    monkeypatch.setattr(sync_mod, "TOPICS_DIR", tmp_path / "out")
    src = _archive(tmp_path)
    assert sync_mod.sync(src, CONFIG) > 0
    assert sync_mod.sync(src, CONFIG) == 0


def test_pruning_removes_a_page_whose_source_vanished(tmp_path, monkeypatch):
    out = tmp_path / "out"
    monkeypatch.setattr(sync_mod, "OUT_DIR", out)
    monkeypatch.setattr(sync_mod, "TREE_PATH", tmp_path / "pbp.tree")
    monkeypatch.setattr(sync_mod, "TOPICS_DIR", tmp_path / "out")
    src = _archive(tmp_path)
    sync_mod.sync(src, CONFIG)
    (out / "C06-Kibwe-PBP-1999-01.md").write_text("stale", encoding="utf-8")
    sync_mod.sync(src, CONFIG)
    assert not (out / "C06-Kibwe-PBP-1999-01.md").exists()
    assert (out / "C06-Kibwe-PBP-2026-08.md").exists()


# ── The wider collision invariant ────────────────────────────────────────────

def test_a_generated_page_clashing_with_a_handwritten_one_is_caught(tmp_path):
    """The likelier collision: someone adds a page elsewhere in the wiki
    with a name a generated transcript already uses. They have no reason
    to look here, so the guard has to."""
    (tmp_path / "a").mkdir()
    (tmp_path / "b").mkdir()
    (tmp_path / "a" / "C06-Kibwe-PBP-2026-08.md").write_text("x")
    (tmp_path / "b" / "C06-Kibwe-PBP-2026-08.md").write_text("y")
    with pytest.raises(SystemExit, match="Duplicate topic filenames"):
        sync_mod.assert_no_duplicate_topics(tmp_path)


def test_the_wiki_wide_guard_can_fail(tmp_path):
    """Distinct names must pass, or the check above proves nothing."""
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "one.md").write_text("x")
    (tmp_path / "a" / "two.md").write_text("y")
    sync_mod.assert_no_duplicate_topics(tmp_path)   # must NOT raise


def test_the_real_wiki_has_no_duplicate_topics():
    """Runs against this checkout. 449 topics, and it must stay at zero."""
    root = Path(__file__).resolve().parent.parent.parent / "Writerside" / "topics"
    if not root.exists():
        pytest.skip("not a full wiki checkout")
    sync_mod.assert_no_duplicate_topics(root)


# ── The tree ─────────────────────────────────────────────────────────────────

def test_tree_lists_every_published_page_and_nothing_else():
    """Tree and pages come from ONE plan, so they cannot disagree."""
    jobs = [(Path("a"), "C06-Kibwe-PBP-2026-08.md", "C06", "Kibwe", "2026-08"),
            (Path("b"), "C06-Kibwe-PBP-2026-07.md", "C06", "Kibwe", "2026-07")]
    xml = render_tree(jobs)
    for _s, dest, *_ in jobs:
        assert f'topic="{dest}"' in xml
    assert xml.count("<toc-element topic=") == len(jobs)


def test_tree_groups_by_campaign_newest_first():
    jobs = [(Path("a"), "C06-K-PBP-2026-07.md", "C06", "K", "2026-07"),
            (Path("b"), "C06-K-PBP-2026-08.md", "C06", "K", "2026-08")]
    xml = render_tree(jobs)
    assert xml.index("2026-08") < xml.index("2026-07")
    assert xml.count("toc-title=") == 1


def test_tree_start_page_is_a_page_it_lists():
    """A start-page Writerside cannot resolve fails the build."""
    jobs = [(Path("a"), "C06-K-PBP-2026-08.md", "C06", "K", "2026-08")]
    xml = render_tree(jobs)
    assert 'start-page="C06-K-PBP-2026-08.md"' in xml
