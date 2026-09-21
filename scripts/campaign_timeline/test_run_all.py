"""The campaign table and the tree edit that lists each timeline page."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))

from run_all import CAMPAIGNS, ROOT, TOPICS, add_to_tree, slug  # noqa: E402


@pytest.mark.parametrize("directory, code, name, folder, tree, parent", CAMPAIGNS)
def test_every_campaign_points_at_a_real_folder_and_parent(directory, code, name,
                                                           folder, tree, parent):
    """A wrong parent would stop the run halfway, after hours of extraction."""
    assert (TOPICS / folder).is_dir(), folder
    assert f'topic="{parent}"' in (ROOT / "Writerside" / tree).read_text(encoding="utf-8")


def test_every_page_name_is_unique():
    """Writerside resolves topics by bare filename; a clash hides a page."""
    names = [f"{code}-{slug(name)}-Timeline.md" for _d, code, name, *_ in CAMPAIGNS]
    assert len(names) == len(set(names))


def _tree(tmp_path, body, nl="\n"):
    path = tmp_path / "t.tree"
    path.write_bytes(body.replace("\n", nl).encode("utf-8"))
    return path


def test_a_self_closing_parent_opens_to_hold_the_page(tmp_path):
    tree = _tree(tmp_path, '<x>\n    <toc-element topic="P.md"/>\n</x>\n')
    assert add_to_tree(tree, "P.md", "T.md")
    assert tree.read_text(encoding="utf-8") == (
        '<x>\n    <toc-element topic="P.md">\n'
        '        <toc-element topic="T.md"/>\n    </toc-element>\n</x>\n')


def test_an_open_parent_gets_the_page_first_and_line_endings_are_kept(tmp_path):
    tree = _tree(tmp_path, '<toc-element topic="P.md">\n    <toc-element topic="A.md"/>\n'
                           '</toc-element>\n', nl="\r\n")
    assert add_to_tree(tree, "P.md", "T.md")
    text = tree.read_bytes().decode("utf-8")
    assert text.index("T.md") < text.index("A.md")
    assert "\n" not in text.replace("\r\n", "")


def test_listing_twice_changes_nothing(tmp_path):
    tree = _tree(tmp_path, '<toc-element topic="P.md"/>\n')
    add_to_tree(tree, "P.md", "T.md")
    assert not add_to_tree(tree, "P.md", "T.md")


def test_a_missing_parent_stops_loudly(tmp_path):
    with pytest.raises(SystemExit):
        add_to_tree(_tree(tmp_path, "<x/>\n"), "P.md", "T.md")
