"""Propose which "areas" are really rooms inside a bigger place, and keep only what checks out.

    python scripts/campaign_timeline/group_areas.py --only C04b C07          # propose
    python scripts/campaign_timeline/group_areas.py --only C04b --apply    # write

The scene split names an area per month, and it is not consistent about
size: C04b has "Carriage" and "Infirmary" as areas beside "Magnimar Zoo",
and C07 has "A lift" beside "Little Akiton". This asks muse-spark-1.3 to
group them, then writes a grouping into ``area_renames`` only if:

* the area it moves exists in that campaign's data, and
* the parent it moves it into is named somewhere in that campaign's posts.

⛔ **Nothing is written unless ``--apply`` is given**, and every proposal should
be checked against the posts first. Being named in the posts is not proof of
being inside: on the first run (2026-09-16) muse-spark-1.3 put "CASTLE
COUNTING" inside "Manee's bodega", when the posts call it a separate arms
dealer that is "nearby", and "the speed lift" inside "the space port", when an
autotrain drops the party at the lift. Both passed the checks below. The
other four proposals were right, and the posts confirmed them.

An area moved into a parent keeps its rooms and their names, so no place
disappears from the page. "Unknown" areas are left out, since grouping them
would be a guess. Anything Lewis already set in ``area_renames`` is never
overwritten.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from extract import ask  # noqa: E402
from messages import read_campaign  # noqa: E402
from run_all import CAMPAIGNS, ROOT, slug  # noqa: E402
from scenes import parse_reply  # noqa: E402

PROMPT = """You are tidying a location timeline for a tabletop RPG campaign.
Each line below is an AREA the party visited, with the rooms seen inside it and
one thing that happened there. Some "areas" are really just a room or spot inside
a bigger place (a building, district, city, ship or station) that another area
names or that the events make clear.

For each area that belongs INSIDE a bigger place, give that bigger place's name.
Use a place name that appears in the list or the events. Leave out any area
that is already a whole place in its own right. Never invent a place.

Write every non-ASCII character as a JSON escape. Reply with ONLY this JSON:
{{"inside": {{"<area exactly as listed>": "<bigger place>"}}}}

Areas ({count}):
{areas}
"""


def area_summary(data: dict) -> dict[str, dict]:
    """Every raw area, with its rooms and a first event, in first-seen order."""
    out: dict[str, dict] = {}
    for month in sorted(data["months"]):
        for s in data["months"][month]["scenes"]:
            if (s.get("area") or s["location"]).strip().lower() in ("unknown", ""):
                continue
            a = out.setdefault(s.get("area") or s["location"],
                               {"rooms": [], "event": s["events"][0]["text"]})
            if s["location"] not in a["rooms"]:
                a["rooms"].append(s["location"])
    return out


def build_prompt(summary: dict) -> str:
    lines = [f"- {name} | rooms: {', '.join(v['rooms'][:6])} | {v['event']}"
             for name, v in summary.items()]
    return PROMPT.format(count=len(lines), areas="\n".join(lines))


def accept(proposal: dict, summary: dict, corpus: str,
           data: dict) -> tuple[dict, list[str]]:
    """The groupings that pass the checks, as (area_renames, rejected)."""
    area_renames, rejected = {}, []
    have_area = data.get("area_renames") or {}
    text = corpus.lower()
    for area, parent in (proposal.get("inside") or {}).items():
        parent = str(parent).strip()
        why = None
        if area not in summary:
            why = "not an area in the data"
        elif not parent or parent.lower() == area.lower():
            why = "no different parent"
        elif area in have_area:
            why = "already set by hand"
        elif parent not in summary and parent.lower() not in text:
            why = f"parent {parent!r} is never named in the posts"
        if why:
            rejected.append(f"{area} -> {parent}: {why}")
            continue
        area_renames[area] = parent
    # Follow chains: "A lift" inside "Little Akiton" inside "Absalom Station"
    # must land in the outermost place, because renames apply only once.
    for area in list(area_renames):
        seen = {area}
        while area_renames[area] in area_renames and area_renames[area] not in seen:
            seen.add(area_renames[area])
            area_renames[area] = area_renames[area_renames[area]]
    return area_renames, rejected


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--archive", type=Path,
                   default=ROOT.parent / "telegram-pbp-reminder" / "data" / "pbp_logs")
    p.add_argument("--only", nargs="*", default=None)
    p.add_argument("--apply", action="store_true",
                   help="write the accepted groupings (check them against the posts first)")
    a = p.parse_args()
    for directory, code, name, *_ in CAMPAIGNS:
        if a.only and code not in a.only:
            continue
        path = ROOT / "timelines" / f"{code}-{slug(name)}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        summary = area_summary(data)
        if len(summary) < 3:
            print(f"{code}: {len(summary)} areas, nothing to group")
            continue
        corpus = "\n".join(m.text for msgs in read_campaign(a.archive / directory,
                                                           "Path_Wars").values()
                           for m in msgs)
        reply, model = ask(build_prompt(summary))
        try:
            proposal = parse_reply(reply)
        except (ValueError, json.JSONDecodeError) as e:
            print(f"{code}: reply unusable ({model}): {e}")
            continue
        area_renames, rejected = accept(proposal, summary, corpus, data)
        if a.apply:
            data.setdefault("area_renames", {}).update(area_renames)
            path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
        verb = "grouped" if a.apply else "PROPOSED (not written)"
        print(f"{code}: {verb} {len(area_renames)} of {len(summary)} areas ({model})")
        for k, v in area_renames.items():
            print(f"    {k} -> {v}")
        for r in rejected:
            print(f"    REJECTED {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
