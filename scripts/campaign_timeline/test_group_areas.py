"""The checks that decide which proposed area groupings are kept."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from group_areas import accept, area_summary  # noqa: E402

SUMMARY = {"Magnimar Zoo": {"rooms": ["Entrance"], "event": "x"},
           "Carriage": {"rooms": ["Carriage"], "event": "x"},
           "A lift": {"rooms": ["A lift"], "event": "x"},
           "Little Akiton": {"rooms": ["Streets"], "event": "x"}}
POSTS = "They rode through Magnimar. Little Akiton is on Absalom Station."


def test_a_grouping_into_a_named_place_is_kept():
    got, rejected = accept({"inside": {"Carriage": "Magnimar"}}, SUMMARY, POSTS, {})
    assert got == {"Carriage": "Magnimar"} and rejected == []


def test_a_parent_never_named_in_the_posts_is_rejected():
    got, rejected = accept({"inside": {"Carriage": "Varisia"}}, SUMMARY, POSTS, {})
    assert got == {} and "never named" in rejected[0]


def test_an_invented_area_is_rejected():
    got, rejected = accept({"inside": {"Balloon": "Magnimar"}}, SUMMARY, POSTS, {})
    assert got == {} and "not an area" in rejected[0]


def test_a_hand_set_grouping_is_never_overwritten():
    got, rejected = accept({"inside": {"Carriage": "Magnimar"}}, SUMMARY, POSTS,
                           {"area_renames": {"Carriage": "The Zoo"}})
    assert got == {} and "by hand" in rejected[0]


def test_chains_land_in_the_outermost_place():
    got, _ = accept({"inside": {"A lift": "Little Akiton",
                                "Little Akiton": "Absalom Station"}}, SUMMARY, POSTS, {})
    assert got == {"A lift": "Absalom Station", "Little Akiton": "Absalom Station"}


def test_unknown_areas_are_never_offered_for_grouping():
    data = {"months": {"2026-01": {"scenes": [
        {"area": "Unknown", "location": "Unknown", "events": [{"text": "x"}]},
        {"area": "Kibwe", "location": "Sun Temple", "events": [{"text": "y"}]}]}}}
    assert list(area_summary(data)) == ["Kibwe"]
