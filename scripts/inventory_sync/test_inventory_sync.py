"""Inventory pages generated from the bot's daily snapshots. Added 2026-10-17."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from inventory_render import diff, render_page  # noqa: E402
from inventory_pages import load_snapshots, render_tree, sync  # noqa: E402


def actor(id_, name, items=(), currency=None, kind="character", owners=("Terra",)):
    return {"id": id_, "name": name, "kind": kind, "owners": list(owners), "currency": currency or {},
            "items": [{"name": n, "type": t, "quantity": q} for n, t, q in items]}


def snap(date, *actors):
    return {"code": "C07", "campaign": "The Hopeful End-Times", "date": date, "actors": list(actors)}


DAY1 = snap("2026-10-18",
            actor("p", "The Party", [("Radiation Sweeper", "equipment", 1), ("Medpatch", "consumable", 3)],
                  {"credits": 155}, kind="party", owners=()),
            actor("lai", "Lai", [("Battery", "consumable", 2)], {"credits": 5}))


def test_a_hand_out_from_the_stash_is_a_move_not_a_gain():
    day2 = snap("2026-10-19",
                actor("p", "The Party", [("Medpatch", "consumable", 3)], {"credits": 155}, kind="party", owners=()),
                actor("lai", "Lai", [("Battery", "consumable", 2), ("Radiation Sweeper", "equipment", 1)],
                      {"credits": 5}))
    assert diff(DAY1, day2) == ["- Radiation Sweeper moved from The Party to Lai"]


def test_gold_or_items_from_nowhere_are_named_with_the_amount():
    day2 = snap("2026-10-19", DAY1["actors"][0],
                actor("lai", "Lai", [("Battery", "consumable", 5), ("Plasma Cannon", "weapon", 1)], {"credits": 900}))
    assert diff(DAY1, day2) == ["- **Lai** gained 3 x Battery", "- **Lai** gained Plasma Cannon",
                                "- **Lai** credits: 5 to 900 (+895)"]


def test_a_partial_move_leaves_the_rest_as_a_loss():
    day2 = snap("2026-10-19",
                actor("p", "The Party", [("Radiation Sweeper", "equipment", 1)], {"credits": 155}, kind="party",
                      owners=()),
                actor("lai", "Lai", [("Battery", "consumable", 2), ("Medpatch", "consumable", 1)], {"credits": 5}))
    assert diff(DAY1, day2) == ["- Medpatch moved from The Party to Lai", "- **The Party** lost 2 x Medpatch"]


def test_a_new_or_gone_sheet_is_said_first():
    day2 = snap("2026-10-19", DAY1["actors"][0], actor("rune", "Rune", owners=("RyoYamakawa",)))
    lines = diff(DAY1, day2)
    assert lines[:2] == ["- Lai is no longer in the records", "- Rune appears in the records"]
    assert "- **Lai** lost 2 x Battery" in lines


def test_two_stacks_of_one_item_count_together():
    a = snap("2026-10-18", actor("lai", "Lai", [("Battery", "consumable", 1), ("Battery", "consumable", 1)]))
    b = snap("2026-10-19", actor("lai", "Lai", [("Battery", "consumable", 2)]))
    assert diff(a, b) == []


def test_the_page_shows_now_then_changes_newest_first():
    day2 = snap("2026-10-19", DAY1["actors"][0], actor("lai", "Lai", [("Battery", "consumable", 2)], {"credits": 6}))
    day3 = snap("2026-10-20", DAY1["actors"][0], actor("lai", "Lai", [("Battery", "consumable", 2)], {"credits": 7}))
    page = render_page([DAY1, day2, day3])
    assert page.startswith("# C07 The Hopeful End-Times inventories\n")
    assert page.index("### The Party") < page.index("### Lai") < page.index("## Changes by day")
    assert "Currency: 155 credits." in page and "| Radiation Sweeper | equipment | 1 |" in page
    assert page.index("### 2026-10-20") < page.index("### 2026-10-19")
    assert "- **Lai** credits: 6 to 7 (+1)" in page


def test_a_pipe_in_an_item_name_stays_in_its_cell():
    page = render_page([snap("2026-10-18", actor("lai", "Lai", [("Knife | serrated", "weapon", 1)]))])
    assert r"| Knife \| serrated | weapon | 1 |" in page


def test_sync_writes_pages_index_tree_and_removes_stale(tmp_path):
    source, out, topics = tmp_path / "inv", tmp_path / "topics" / "Inventories", tmp_path / "topics"
    (source / "C07").mkdir(parents=True)
    (source / "C07" / "2026-10-18.json").write_text(json.dumps(DAY1), encoding="utf-8")
    (source / "C07" / "broken.json").write_text("{", encoding="utf-8")
    out.mkdir(parents=True)
    (out / "C99-Inventory.md").write_text("old", encoding="utf-8")
    tree = tmp_path / "inventories.tree"
    assert sync(source, out, tree, topics) == 4
    assert sorted(p.name for p in out.glob("*.md")) == ["C07-Inventory.md", "Inventories.md"]
    assert 'topic="C07-Inventory.md"' in tree.read_text(encoding="utf-8")
    assert sync(source, out, tree, topics) == 0, "a second run changes nothing"


def test_no_snapshots_yet_is_an_empty_index_not_an_error(tmp_path):
    assert load_snapshots(tmp_path / "missing") == {}
    assert "<toc-element topic=\"Inventories.md\">" in render_tree([])
