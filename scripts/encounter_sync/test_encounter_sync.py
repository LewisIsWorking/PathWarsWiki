"""Encounter pages generated from the bot's records. Added 2026-09-17."""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from encounter_render import page_name, render_page, slug, when  # noqa: E402
from encounter_pages import load_records, plan, render_tree, sync  # noqa: E402

RECORD = {
    "code": "C09", "campaign": "Metal City", "encounter_id": "AbC123",
    "name": "Captain Vex Ashburn", "location": "The Stargazer - Bridge",
    "started_at": "2026-09-13T18:49:00+00:00", "ended": True, "ended_at": "2026-09-16T20:10:00+00:00",
    "rounds": 2,
    "initiative": [{"name": "Captain Vex", "initiative": 24.5, "side": "enemy"},
                   {"name": "Arktos", "initiative": 24, "side": "ally", "player": "@StorybookRhizome"}],
    "allies": [{"name": "Arktos", "player": "@StorybookRhizome"}, {"name": "Drone", "player": None}],
    "enemies": ["Captain Vex", "Ovvat (Nova pirate helmsman)."],
    "hits": [{"round": 1, "text": "Knemdom (Nova pirate #01). ▱▱▱▱▱▱▱▱▱▱ Down · Horizon Thunder Sphere from Reign"},
             {"round": 2, "text": "Vex <b>. ▰▰▰▰▱▱▱▱▱▱ Bloodied"}],
}


def test_the_page_follows_the_hand_written_layout():
    page = render_page(RECORD)
    assert page.startswith("# C09-Combat-Captain-Vex-Ashburn-2026-09-13\n")
    assert ">> 1. Encounter name: Captain Vex Ashburn." in page
    assert ">> 2. Encounter location: The Stargazer - Bridge." in page
    assert ">> 3. Encounter started = 2026 September 13th at 19:49." in page
    assert ">> 4. Encounter ended = 2026 September 16th at 21:10, after 2 rounds." in page
    assert ">> 1. Captain Vex 24.5.\n>> 2. Arktos 24 @StorybookRhizome." in page
    assert ">> 1. Arktos @StorybookRhizome.\n>> 2. Drone." in page
    assert ">> 2. Ovvat (Nova pirate helmsman)." in page and "helmsman).." not in page
    assert "## Round 1.\n\n> Round 1: Hits.\n>> 1. Knemdom (Nova pirate #01)." in page
    assert "Vex &lt;b&gt;." in page and "<b>" not in page


def test_a_running_fight_says_so_and_an_empty_list_reads_none():
    page = render_page({**RECORD, "ended": False, "initiative": [], "hits": []})
    assert ">> 4. Still running: round 2." in page
    assert "> Initiative.\n>> 1. None." in page
    assert "## Round" not in page


def test_names_are_safe_filenames_and_dates_are_uk_time():
    assert slug("Polly & the Spiritual Sinkwell!") == "Polly-the-Spiritual-Sinkwell"
    assert page_name({**RECORD, "name": "", "started_at": None}) == "C09-Combat-Encounter-undated.md"
    assert when("2026-01-01T23:30:00+00:00") == "2026 January 1st at 23:30"
    assert when("2026-09-22T11:00:00+00:00") == "2026 September 22nd at 12:00"
    assert when(None) == "unknown"


def _source(tmp_path, *records):
    source = tmp_path / "encounters" / "C09"
    source.mkdir(parents=True)
    for i, record in enumerate(records):
        (source / f"{i}.json").write_text(json.dumps(record), encoding="utf-8")
    (source / "broken.json").write_text("{not json", encoding="utf-8")
    return tmp_path / "encounters"


def test_sync_writes_pages_index_and_tree_then_removes_what_no_record_backs(tmp_path):
    topics = tmp_path / "topics"
    out, tree = topics / "Encounters", tmp_path / "encounters.tree"
    (topics / "C09-Metal-City").mkdir(parents=True)
    (topics / "C09-Metal-City" / "C09-Intro-Combat-Captain-Vex-Ashburn.md").write_text("hand-written")
    source = _source(tmp_path, RECORD)
    assert sync(source, out, tree, topics) == 3
    assert sync(source, out, tree, topics) == 0
    assert (out / "C09-Combat-Captain-Vex-Ashburn-2026-09-13.md").exists()
    assert "[Captain Vex Ashburn](C09-Combat-Captain-Vex-Ashburn-2026-09-13.md)" in (out / "Encounters.md").read_text()
    assert 'toc-title="C09 Metal City"' in tree.read_text()
    (source / "C09" / "0.json").unlink()
    sync(source, out, tree, topics)
    assert sorted(p.name for p in out.glob("*.md")) == ["Encounters.md"]
    assert "No encounters yet." in (out / "Encounters.md").read_text()
    assert (topics / "C09-Metal-City" / "C09-Intro-Combat-Captain-Vex-Ashburn.md").read_text() == "hand-written"


def test_a_generated_page_may_never_share_a_name_with_a_hand_written_one(tmp_path):
    topics = tmp_path / "topics"
    (topics / "Elsewhere").mkdir(parents=True)
    (topics / "Elsewhere" / "C09-Combat-Captain-Vex-Ashburn-2026-09-13.md").write_text("hand-written")
    with pytest.raises(SystemExit, match="Duplicate topic filenames"):
        sync(_source(tmp_path, RECORD), topics / "Encounters", tmp_path / "e.tree", topics)


def test_two_fights_with_one_name_on_one_day_both_publish(tmp_path):
    twin = {**RECORD, "encounter_id": "ZzZ999"}
    names = [name for name, _ in plan(load_records(_source(tmp_path, RECORD, twin)))]
    assert names == ["C09-Combat-Captain-Vex-Ashburn-2026-09-13-AbC123.md",
                     "C09-Combat-Captain-Vex-Ashburn-2026-09-13-ZzZ999.md"]
    assert load_records(tmp_path / "missing") == []
    assert 'topic="Encounters.md"' in render_tree([])
