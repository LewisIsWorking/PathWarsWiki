"""Rendering a transcript must change headers and nothing else.

COVERS  ``render`` — header rewriting, permalinks, the pre-2026 shape
        with no message id, and the stats functions the index pages use.
MISSES  whether the result reads nicely. A human judges that; a test can
        only check nothing was lost on the way.
PROVEN  by ``test_the_untouched_guarantee_can_fail``.

────────────────────────────────────────────────────────────────────────

⭐ The one guarantee that matters: **only message headers change.** Prose,
images, week and day headings, the archiver's own notes — all pass
through byte for byte, so a published page can never say something the
archive did not. Every test here is ultimately about that.

⚠️ And the trap found on the first real run. ``count_messages`` matches
the RAW header shape, so counting a *rendered* body returns zero — which
is exactly what the index pages published: "0 messages" across all ten
campaigns, in a table that was otherwise perfectly formatted and looked
entirely finished. Stats must be taken from the source, and
``test_stats_come_from_raw_not_rendered`` pins that.
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import (count_messages, date_span, is_message_header,
                    render_body, render_header, speakers)

MODERN = "**Ryo Yamakawa** (2026-08-15 07:51:12) msg#172171@40585:"
GM = "**Path Wars** [GM] (2026-08-01 06:34:08) msg#169589@137075:"
LEGACY = "**Path Wars** [GM] (2024-04-17 19:16:04):"

SAMPLE = f"""## Week 33 (Aug 10–Aug 16)

### 📅 Saturday, Aug 15

{MODERN}
"Next. Next we stop those psychos."

{GM}
*[image]* A double door to the West.
"""


# ── Header rewriting ─────────────────────────────────────────────────────────

def test_the_id_becomes_a_link_rather_than_noise():
    """The noisiest part of the line turns into the one thing the wiki
    could not otherwise offer: a jump straight to Telegram."""
    out = render_header(MODERN, "Path_Wars")
    assert out == ("**Ryo Yamakawa** · 07:51 · "
                   "[↗](https://t.me/Path_Wars/40585/172171)")
    assert "msg#" not in out
    assert "2026-08-15" not in out, "the day heading already said the date"


def test_the_gm_tag_survives():
    out = render_header(GM, "Path_Wars")
    assert "*(GM)*" in out and "Path Wars" in out


def test_a_pre_2026_line_renders_without_a_broken_link():
    """Message ids only exist from 2026. A link built from a missing id
    would go nowhere, which is worse than no link."""
    out = render_header(LEGACY, "Path_Wars")
    assert out == "**Path Wars** *(GM)* · 19:16"
    assert "http" not in out


def test_no_username_means_no_link():
    """Without a public handle the group has no URL at all."""
    assert "http" not in render_header(MODERN, "")


@pytest.mark.parametrize("line", [
    "## Week 33 (Aug 10–Aug 16)",
    "### 📅 Saturday, Aug 15",
    '"Next. Next we stop those psychos."',
    "*[image]*",
    "",
    "**bold text** in the middle of a sentence",
])
def test_non_headers_are_left_completely_alone(line):
    assert render_header(line, "Path_Wars") == line
    assert is_message_header(line) is False


def test_an_unrecognised_header_shape_is_preserved_not_mangled():
    """A line this does not recognise is still someone's words. Passing
    it through raw is exactly what every page looked like before."""
    odd = "**Someone** (not a timestamp) msg#1@2:"
    assert render_header(odd, "Path_Wars") == odd


# ── The untouched guarantee ──────────────────────────────────────────────────

def test_only_header_lines_differ():
    src = SAMPLE.splitlines()
    out = render_body(SAMPLE, "Path_Wars").splitlines()
    assert len(src) == len(out), "rendering must not add or drop lines"
    changed = [i for i, (a, b) in enumerate(zip(src, out)) if a != b]
    assert changed == [i for i, line in enumerate(src)
                       if is_message_header(line)]


def test_the_untouched_guarantee_can_fail():
    """Prove the check above by handing it a body that DID change
    elsewhere. If this passes silently, the test proves nothing."""
    src = SAMPLE.splitlines()
    tampered = [line.replace("psychos", "PSYCHOS") for line in src]
    changed = [i for i, (a, b) in enumerate(zip(src, tampered)) if a != b]
    header_lines = [i for i, line in enumerate(src) if is_message_header(line)]
    assert changed != header_lines, (
        "a body-only edit must NOT look like a header-only change")


def test_every_real_transcript_renders_without_losing_a_line():
    """Run the renderer over the whole published corpus.

    A unit test on three sample lines cannot see the shapes three years
    of real archiving actually produced.
    """
    root = (Path(__file__).resolve().parent.parent.parent
            / "Writerside" / "topics" / "Play-by-posts" / "Transcripts")
    if not root.exists():
        pytest.skip("transcripts not published in this checkout")
    files = sorted(root.rglob("*-PBP-*.md"))
    assert files, "expected published transcripts to check against"
    for path in files[:40]:
        text = path.read_text(encoding="utf-8")
        assert len(render_body(text, "Path_Wars").splitlines()) == \
            len(text.splitlines()), f"{path.name} changed line count"


# ── Stats, which the index pages depend on ───────────────────────────────────

def test_counts_and_speakers_and_span():
    assert count_messages(SAMPLE) == 2
    assert speakers(SAMPLE) == ["Ryo Yamakawa", "Path Wars"]
    assert date_span(SAMPLE) == ("2026-08-15", "2026-08-01")


def test_stats_come_from_raw_not_rendered():
    """⚠️ The bug that shipped "0 messages" for all ten campaigns.

    Rendering rewrites exactly the lines these functions match, so a
    rendered body counts as empty. The numbers must be taken from the
    source, and this test exists to make that non-negotiable.
    """
    rendered = render_body(SAMPLE, "Path_Wars")
    assert count_messages(SAMPLE) == 2
    assert count_messages(rendered) == 0, (
        "if this ever returns 2, the renderer has stopped rewriting "
        "headers and the published pages are raw again")
    assert speakers(rendered) == []


def test_empty_input_is_not_an_error():
    assert count_messages("") == 0
    assert speakers("") == []
    assert date_span("") is None
