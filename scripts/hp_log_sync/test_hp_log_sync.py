"""The HP and Stamina log pages: grouped by day, safe in a table, and never lost to a failed fetch."""

import io
import json
import sys
import urllib.error
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hp_log_pages  # noqa: E402
from hp_log_render import EM_DASH, page_name, render_page  # noqa: E402

# The case that started this, C06 2026-09-01: Daichi's Stamina fell from 35 to 8 with no record.
DAICHI = {"id": "1", "at": "2026-09-01T19:30:00Z", "actorId": "daichi", "character": "Daichi Kenshin",
          "hpBefore": 40, "hpAfter": 40, "maxHp": 40, "spBefore": 35, "spAfter": 8, "maxSp": 35,
          "reason": "manual change"}
BOLT = {"id": "2", "at": "2026-09-02T20:05:00Z", "actorId": "daichi", "character": "Daichi Kenshin",
        "hpBefore": 40, "hpAfter": 25, "maxHp": 40, "spBefore": 8, "spAfter": 0, "maxSp": 35,
        "reason": "Electrical Bolt from Chamber of Scribing"}


def wiki(tmp_path):
    topics = tmp_path / "topics"
    for folder in ("C06-Kibwe", "C01-Arc-11-Fun", "C01-Doomsday-Funtime", "C04-The-Magni-Guard", "Info"):
        (topics / folder).mkdir(parents=True)
    (topics / "C06-Kibwe" / "C06-Kibwe.md").write_text("# Kibwe\n", encoding="utf-8")
    (topics / "C01-Doomsday-Funtime" / "C01-Doomsday-Funtime.md").write_text("# C01\n", encoding="utf-8")
    return topics


def run(tmp_path, topics, history):
    def fetch(code):
        result = history.get(code, [])
        if isinstance(result, Exception):
            raise result
        return result
    return hp_log_pages.sync(fetch, topics, tmp_path / "index", tmp_path / "hp-logs.tree")


def test_a_page_groups_changes_by_day_with_before_and_after():
    page = render_page("C06", "Kibwe", [DAICHI, BOLT])
    assert page.startswith("# C06 Kibwe: HP and Stamina log\n")
    assert page.index("## 2026-09-01") < page.index("## 2026-09-02")
    assert "| 19:30 | Daichi Kenshin | 40 → 40 / 40 | 35 → 8 / 35 | manual change |" in page
    assert "| 20:05 | Daichi Kenshin | 40 → 25 / 40 | 8 → 0 / 35 | Electrical Bolt from Chamber of Scribing |" in page


def test_an_unknown_before_and_a_missing_pool_are_shown_as_such():
    first_seen = {**BOLT, "hpBefore": None, "spBefore": None, "spAfter": None, "maxSp": None}
    assert "| 20:05 | Daichi Kenshin | ? → 25 / 40 | - |" in render_page("C06", "Kibwe", [first_seen])


def test_server_text_cannot_break_the_table_or_writerside():
    nasty = {**DAICHI, "character": "A|B <b>", "reason": f"cut {EM_DASH} 50% %var%\nnext"}
    page = render_page("C06", "Kibwe", [nasty])
    assert EM_DASH not in page
    assert "A/B &lt;b&gt;" in page and "%var%" not in page and "\nnext" not in page


def test_only_campaigns_with_history_get_a_page_in_their_own_folder(tmp_path):
    topics = wiki(tmp_path)
    changed, failed = run(tmp_path, topics, {"C06": [DAICHI, BOLT]})

    assert failed == [] and changed == 3
    assert (topics / "C06-Kibwe" / page_name("C06")).exists()
    assert not list(topics.rglob("C01-HP-And-Stamina-Log.md"))
    tree = (tmp_path / "hp-logs.tree").read_text(encoding="utf-8")
    assert '<toc-element topic="C06-HP-And-Stamina-Log.md"/>' in tree and "C04" not in tree
    assert "2 change(s), latest 2026-09-02" in (tmp_path / "index" / "HP-And-Stamina-Logs.md").read_text("utf-8")


def test_a_second_identical_run_changes_nothing(tmp_path):
    topics = wiki(tmp_path)
    run(tmp_path, topics, {"C06": [DAICHI]})
    assert run(tmp_path, topics, {"C06": [DAICHI]}) == (0, [])


def test_a_failed_fetch_keeps_the_page_it_had(tmp_path):
    topics = wiki(tmp_path)
    run(tmp_path, topics, {"C06": [DAICHI]})
    page = (topics / "C06-Kibwe" / page_name("C06")).read_text(encoding="utf-8")

    changed, failed = run(tmp_path, topics, {"C06": hp_log_pages.FetchFailed("C06: HTTP 502")})

    assert failed == ["C06"]
    assert (topics / "C06-Kibwe" / page_name("C06")).read_text(encoding="utf-8") == page
    assert "C06-HP-And-Stamina-Log.md" in (tmp_path / "hp-logs.tree").read_text(encoding="utf-8")


def test_main_campaign_folder_is_the_one_named_after_its_page(tmp_path):
    folders = hp_log_pages.campaign_folders(wiki(tmp_path))
    assert folders["C01"].name == "C01-Doomsday-Funtime"
    assert folders["C04"].name == "C04-The-Magni-Guard"
    assert "Info" not in {f.name for f in folders.values()}
    assert hp_log_pages.campaign_name(folders["C04"]) == "The Magni Guard"


class _Answer(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


def test_fetch_pages_through_truncated_answers_and_reads_404_as_none():
    calls = []

    def opener(request, timeout):
        calls.append(request.full_url)
        if len(calls) == 1:
            return _Answer(json.dumps({"truncated": True, "changes": [DAICHI]}).encode())
        return _Answer(json.dumps({"truncated": False, "changes": [DAICHI, BOLT]}).encode())

    assert [c["id"] for c in hp_log_pages.fetch_history("https://coo.example/", "C06", opener)] == ["1", "2"]
    assert calls[0] == "https://coo.example/api/pathwars/campaigns/C06/hp-history"
    assert "since=2026-09-01T19%3A30%3A00Z" in calls[1]

    def missing(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found", {}, None)

    assert hp_log_pages.fetch_history("https://coo.example", "C06", missing) == []

    def down(request, timeout):
        raise urllib.error.HTTPError(request.full_url, 502, "Bad Gateway", {}, None)

    with pytest.raises(hp_log_pages.FetchFailed):
        hp_log_pages.fetch_history("https://coo.example", "C06", down)
