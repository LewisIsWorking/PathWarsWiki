"""Naming rules for published transcripts — the part with the sharp edge.

COVERS  the filename collision trap, campaign resolution in BOTH
        directions, and which files count as monthly transcripts.
MISSES  anything touching the filesystem; that is ``test_pbp_sync.py``.
PROVEN  by ``test_the_collision_guard_can_fail`` and
        ``test_the_mapping_guard_can_fail``.

⛔ The trap. Writerside ``.tree`` files reference topics by **bare
filename**, resolved recursively across ``topics/``. The source archive is
``<Campaign>/<YYYY-MM>.md``, so **ten campaigns each own a 2026-08.md**.
Copied across unchanged, Writerside resolves every reference to whichever
twin it finds first — publishing one month and silently hiding nine. It
does not error. Nothing looks wrong.

⭐ Both directions of the campaign mapping are checked, and an unmapped
directory is a hard failure rather than a skip. That is what found C10
(configured, no transcripts yet) and Dark_Pockets / Magni_Watch
(transcripts, no config) on the first run. A campaign whose history
quietly fails to publish is worse than a run that fails loudly.
"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sync as sync_mod
from naming import (RETIRED, is_month_file, published_name,
                    resolve_campaigns, sanitize_dirname, slug)
from tree import render_tree

CONFIG = json.dumps({"topic_pairs": [
    {"name": "Kibwe", "code": "C06"},
    {"name": "Doomsday Funtime", "code": "C01"},
    {"name": "Hopeful End-Times", "code": "C07"},
    {"name": "The Junction", "code": "C10"},
]})


# ── The collision trap ───────────────────────────────────────────────────────

def test_the_same_month_in_two_campaigns_gets_two_names():
    """The whole reason for the naming scheme."""
    a = published_name("C06", "Kibwe", "2026-08")
    b = published_name("C01", "Doomsday-Funtime", "2026-08")
    assert a != b
    assert a == "C06-Kibwe-PBP-2026-08.md"


def test_sync_refuses_to_publish_a_collision(tmp_path, monkeypatch):
    """Belt and braces: if the naming rule ever regresses, stop."""
    jobs = [(tmp_path / "a.md", "same.md", "C06", "Kibwe", "2026-08"),
            (tmp_path / "b.md", "same.md", "C01", "Doom", "2026-08")]
    with pytest.raises(SystemExit, match="collision"):
        sync_mod._assert_unique(jobs)


def test_the_collision_guard_can_fail():
    """Prove the guard by feeding it the bug: distinct names must pass."""
    jobs = [(Path("a"), "one.md", "C06", "K", "2026-08"),
            (Path("b"), "two.md", "C01", "D", "2026-08")]
    sync_mod._assert_unique(jobs)   # must NOT raise


# ── Campaign resolution, both directions ─────────────────────────────────────

def test_config_campaigns_map_automatically():
    mapping, unmapped = resolve_campaigns(CONFIG, ["Kibwe", "Doomsday_Funtime"])
    assert mapping["Kibwe"] == ("C06", "Kibwe")
    assert mapping["Doomsday_Funtime"] == ("C01", "Doomsday-Funtime")
    assert unmapped == []


def test_a_retired_campaign_is_still_published():
    """Finished campaigns leave the config but keep their history."""
    mapping, unmapped = resolve_campaigns(CONFIG, ["Dark_Pockets"])
    assert mapping["Dark_Pockets"] == RETIRED["Dark_Pockets"]
    assert unmapped == []


def test_a_configured_campaign_with_no_transcripts_is_not_an_error():
    """C10 exists in config and has never posted. That is normal."""
    _mapping, unmapped = resolve_campaigns(CONFIG, ["Kibwe"])
    assert unmapped == []


def test_an_unmapped_directory_is_reported_not_skipped():
    """The direction that actually bites: new campaign, no mapping."""
    _mapping, unmapped = resolve_campaigns(CONFIG, ["Brand_New_Campaign"])
    assert unmapped == ["Brand_New_Campaign"]


def test_non_campaign_directories_are_ignored():
    _mapping, unmapped = resolve_campaigns(CONFIG, ["summaries"])
    assert unmapped == []


def test_the_mapping_guard_can_fail(tmp_path):
    """An unmapped directory must stop the whole sync."""
    (tmp_path / "Mystery_Campaign").mkdir()
    with pytest.raises(SystemExit, match="no campaign mapping"):
        sync_mod._plan(tmp_path, CONFIG)[0]
        sync_mod.sync(tmp_path, CONFIG)


def test_directory_rule_matches_the_bot():
    """sanitize_dirname mirrors transcript.logger in the bot repo.

    If the bot changes its rule, config names stop matching the
    directories it creates and every campaign becomes 'unmapped'. These
    cases are the shapes that actually occur in the archive.
    """
    assert sanitize_dirname("Hopeful End-Times") == "Hopeful_End-Times"
    assert sanitize_dirname("Doomsday Funtime") == "Doomsday_Funtime"
    assert sanitize_dirname("Kibwe") == "Kibwe"
    assert slug("Hopeful End-Times") == "Hopeful-End-Times"


# ── Which files are transcripts ──────────────────────────────────────────────

@pytest.mark.parametrize("stem,expected", [
    ("2026-08", True), ("2023-08", True),
    ("README", False), ("2026-02-gm", False), ("notes", False),
])
def test_only_monthly_logs_are_published(stem, expected):
    assert is_month_file(stem) is expected


