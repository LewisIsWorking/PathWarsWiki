"""The parts of the timeline that must not quietly lie.

The model's output is never tested here; it cannot be. What is tested is
everything that stands between it and the page: the transcript parser,
the checks that reject a bad scene split, and the arithmetic on the page.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from messages import parse_month  # noqa: E402
from page_render import build_visits, duration, in_game_hours, render  # noqa: E402
from scenes import build_prompt, parse_reply, validate  # noqa: E402

MONTH = """# Magni Guard — 2026-06

*PBP transcript archived by PathWarsNudge bot.*

---

## Week 23 (Jun 01–Jun 07)

### 📅 Tuesday, Jun 02

**Path Wars** [GM] (2026-06-02 10:00:00) msg#100@76799:
You reach the atrium. It is the next morning.

**Ryo** (2026-06-02 12:30:00) msg#101@76799:
I look around.

### 📅 Friday, Jun 05

**Path Wars** [GM] (2026-06-05 10:00:00):
The kobolds attack in the tunnels.
"""


def _msgs():
    return parse_month("2026-06", MONTH, "Path_Wars")


def _scenes(*spans):
    return {"scenes": [{"first": a, "last": b, "location": loc,
                        "events": [{"at": a, "text": f"at {loc}"}],
                        "time_cues": cues}
                       for a, b, loc, cues in spans]}


# ── parsing ──────────────────────────────────────────────────────────────

def test_parses_messages_in_order_without_headings():
    m = _msgs()
    assert [x.n for x in m] == [1, 2, 3]
    assert m[0].gm and not m[1].gm
    assert m[1].text == "I look around."
    assert "📅" not in m[1].text, "a day heading leaked into a message"


def test_links_only_where_the_archive_has_an_id():
    m = _msgs()
    assert m[0].link == "https://t.me/Path_Wars/76799/100"
    assert m[2].link is None, "pre-id messages must not get a broken link"


def test_prompt_numbers_every_message_and_names_known_places():
    prompt = build_prompt(_msgs(), ["The Atrium"])
    assert "1. [2026-06-02 10:00] Path Wars (GM): You reach" in prompt
    assert "3. [2026-06-05 10:00]" in prompt
    assert "- The Atrium" in prompt


def test_prompt_says_where_the_last_month_ended():
    """A month boundary is not a move. Without this the model reset to the
    first known place every month."""
    assert "starts: Room 9" in build_prompt(_msgs(), ["Room 5", "Room 9"], "Room 9")
    assert "starts: unknown" in build_prompt(_msgs(), [])


# The JSON escape for the accented name, spelled out so no editor can turn
# it into the character itself (one did, 2026-09-16).
ESCAPED = "B" + "\\" + "u00e1yakan"


def test_a_reply_with_a_destroyed_character_is_rejected():
    damaged = '{"scenes": [{"location": "B' + chr(0xFFFD) + 'yakan"}]}'
    with pytest.raises(ValueError):
        parse_reply(damaged)


def test_escaped_names_decode_exactly():
    assert parse_reply('{"n": "' + ESCAPED + '"}') == {"n": "B" + chr(0xE1) + "yakan"}


def test_prompt_asks_for_escapes_the_model_can_copy():
    assert '"' + ESCAPED + '"' in build_prompt(_msgs(), [])


def test_reply_json_is_found_inside_chatter():
    assert parse_reply('Sure!\n```json\n{"scenes": []}\n```') == {"scenes": []}


# ── validation: the reason the model can be used at all ─────────────────

def test_a_clean_split_passes():
    scenes, dropped = validate(_scenes((1, 2, "Atrium", ["the next morning"]),
                                       (3, 3, "Tunnels", [])), _msgs())
    assert [s["location"] for s in scenes] == ["Atrium", "Tunnels"]
    assert dropped == []


@pytest.mark.parametrize("spans, why", [
    (((1, 1, "A", []), (3, 3, "B", [])), "skips message 2"),
    (((1, 2, "A", []), (2, 3, "B", [])), "overlaps"),
    (((2, 3, "A", []),), "does not start at 1"),
    (((1, 2, "A", []),), "stops before the last message"),
    (((1, 4, "A", []),), "runs past the last message"),
])
def test_a_split_that_loses_or_repeats_messages_is_rejected(spans, why):
    with pytest.raises(ValueError):
        validate(_scenes(*spans), _msgs())


def test_an_invented_time_cue_is_dropped_not_kept():
    scenes, dropped = validate(_scenes((1, 3, "Atrium", ["Day 3", "the next  MORNING"])),
                               _msgs())
    assert scenes[0]["time_cues"] == ["the next  MORNING"]
    assert dropped == ["Day 3"]


def test_an_event_outside_its_scene_is_not_kept():
    data = _scenes((1, 2, "A", []), (3, 3, "B", []))
    data["scenes"][0]["events"].append({"at": 3, "text": "wrong scene"})
    scenes, _ = validate(data, _msgs())
    assert all(e["text"] != "wrong scene" for e in scenes[0]["events"])


# ── the page ─────────────────────────────────────────────────────────────

def _data(**extra):
    scenes, _ = validate(_scenes((1, 1, "Atrium", []), (2, 2, "Atrium", []),
                                 (3, 3, "Tunnels", [])), _msgs())
    return {"code": "C04", "campaign": "Magni Guard",
            "months": {"2026-06": {"messages": 3, "scenes": scenes}},
            "in_game": {}, "renames": {}, **extra}


def test_consecutive_scenes_at_one_place_are_one_visit():
    visits = build_visits(_data(), {"2026-06": _msgs()})
    assert [(v.location, v.messages) for v in visits] == [("Atrium", 2), ("Tunnels", 1)]
    assert visits[0].key == "2026-06#1"


def test_a_rename_merges_places():
    visits = build_visits(_data(renames={"Tunnels": "Atrium"}), {"2026-06": _msgs()})
    assert len(visits) == 1


def test_the_page_scrolls_down_and_measures_irl_to_the_next_place():
    page = render(_data(in_game={"2026-06#1": "2d 4h"}), {"2026-06": _msgs()})
    assert "flowchart TD" in page and "gantt" not in page
    # Atrium ran from 2 Jun 10:00 to the Tunnels' first post, 5 Jun 10:00.
    assert "🗓️ IRL 3d ▰▰▰▰▰▰▰▰▰▰" in page
    assert "⏳ In-game 2d 4h" in page
    assert '`"2026-06#3"`' in page, "an unfilled visit must name its key"


@pytest.mark.parametrize("text, hours", [
    ("2d 4h", 52), ("30m", 0.5), ("1w", 168), ("3 days", 72),
    ("1 week and 2 hours", 170), ("about 3 days", None), ("a while", None), ("", None),
])
def test_in_game_time_is_read_or_refused(text, hours):
    assert in_game_hours(text) == hours


@pytest.mark.parametrize("hours, shown", [
    (0.4, "<1h"), (5, "5h"), (50, "2d 2h"), (400, "2w 2d"),
])
def test_durations(hours, shown):
    assert duration(hours) == shown
