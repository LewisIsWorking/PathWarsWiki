"""Build or refresh every campaign's timeline in one go.

    python scripts/campaign_timeline/run_all.py                  # extract, then pages
    python scripts/campaign_timeline/run_all.py --pages-only     # after hand edits
    python scripts/campaign_timeline/run_all.py --only C00 C09

Lewis, 2026-09-16: "Every campaign will get a timeline." Extraction only
sends months that are new or have grown, so re-running this is cheap.

Each page is listed in the wiki under its campaign's own page, in whichever
tree that page already lives in. The trees are not uniform (C00 sits in
characters.tree, C09 at the top of mi.tree, C05 under Links-to-campaigns),
so each campaign names its parent explicitly rather than guessing.
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from extract import extract  # noqa: E402
from messages import read_campaign  # noqa: E402
from page_render import render  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TOPICS = ROOT / "Writerside" / "topics"

# (archive dir, code, name, topic folder, tree file, parent topic)
CAMPAIGNS = [
    ("Riddleport", "C00", "Riddleport", "C00-Riddleport",
     "characters.tree", "C00-Riddleport.md"),
    ("Doomsday_Funtime", "C01", "Doomsday Funtime", "C01-Doomsday-Funtime",
     "mi.tree", "C01-Doomsday-Funtime.md"),
    ("Magni_Guard", "C04", "Magni Guard", "C04-The-Magni-Guard",
     "mi.tree", "C04-Magni-Guard.md"),
    ("Magni_Watch", "C04b", "Magni Watch", "C04-The-Magni-Guard",
     "mi.tree", "C04-Magni-Guard.md"),
    ("Grand_Explorers", "C05", "Grand Explorers", "C05-The-Grand-Explorers",
     "mi.tree", "C05-The-Grand-Explorers.md"),
    ("Kibwe", "C06", "Kibwe", "C06-Kibwe",
     "mi.tree", "C06-Kibwe.md"),
    ("Hopeful_End-Times", "C07", "Hopeful End-Times", "C07-The-Hopeful-End-Times",
     "mi.tree", "C07-Hopeful-end-times.md"),
    ("Theria", "C08", "Theria", "C08-Theria",
     "mi.tree", "C08-Theria.md"),
    ("Metal_City", "C09", "Metal City", "C09-Metal-City-Stargazing",
     "mi.tree", "C09-Metal-City.md"),
    ("The_Junction", "C10", "The Junction", "Other-campaigns",
     "mi.tree", "C10-Special.md"),
    ("Dark_Pockets", "C11", "Dark Pockets", "C11-Dark-Pockets",
     "mi.tree", "C11-Dark-Pockets.md"),
]


def slug(name: str) -> str:
    return name.replace(" ", "-")


def add_to_tree(tree: Path, parent: str, child: str) -> bool:
    """List ``child`` under ``parent``. True if the tree changed.

    Handles both shapes a parent can have: self-closing, which becomes an
    open element, and already open, which gets the child as its first entry.
    """
    # Bytes, not read_text: that turns CRLF into LF, and the edited tree
    # would then be written back with every line ending changed.
    text = tree.read_bytes().decode("utf-8")
    if f'topic="{child}"' in text:
        return False
    esc = re.escape(parent)
    closed = re.search(rf'^(?P<ind>[ \t]*)<toc-element topic="{esc}"/>\r?\n', text, re.M)
    opened = re.search(rf'^(?P<ind>[ \t]*)<toc-element topic="{esc}">\r?\n', text, re.M)
    nl = "\r\n" if "\r\n" in text else "\n"
    if closed:
        ind = closed.group("ind")
        new = (f'{ind}<toc-element topic="{parent}">{nl}'
               f'{ind}    <toc-element topic="{child}"/>{nl}'
               f'{ind}</toc-element>{nl}')
        text = text[:closed.start()] + new + text[closed.end():]
    elif opened:
        ind = opened.group("ind")
        text = (text[:opened.end()] + f'{ind}    <toc-element topic="{child}"/>{nl}'
                + text[opened.end():])
    else:
        raise SystemExit(f"{parent} is not in {tree.name}; fix CAMPAIGNS")
    tree.write_bytes(text.encode("utf-8"))
    return True


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archive", type=Path,
                   default=ROOT.parent / "telegram-pbp-reminder" / "data" / "pbp_logs")
    p.add_argument("--pages-only", action="store_true")
    p.add_argument("--only", nargs="*", default=None)
    a = p.parse_args()
    failed = 0
    for directory, code, name, folder, tree, parent in CAMPAIGNS:
        if a.only and code not in a.only:
            continue
        source = a.archive / directory
        data_path = ROOT / "timelines" / f"{code}-{slug(name)}.json"
        print(f"=== {code} {name}")
        if not a.pages_only:
            failed |= extract(source, data_path, code, name, "Path_Wars")
        if not data_path.exists():
            print("  no data yet, no page")
            continue
        topic = f"{code}-{slug(name)}-Timeline.md"
        page = render(json.loads(data_path.read_text(encoding="utf-8")),
                      read_campaign(source, "Path_Wars"),
                      data_file=data_path.relative_to(ROOT).as_posix())
        (TOPICS / folder / topic).write_text(page, encoding="utf-8", newline="\n")
        if add_to_tree(ROOT / "Writerside" / tree, parent, topic):
            print(f"  listed under {parent} in {tree}")
    return failed


if __name__ == "__main__":
    sys.exit(main())
