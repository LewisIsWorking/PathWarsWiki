"""Turn a campaign's saved scenes into a wiki page that scrolls DOWN.

Lewis, 2026-09-16: "It would be good if it was scroll down not scroll to
the left/right." So no Gantt chart, which is horizontal by nature. The
timeline is a top-to-bottom Mermaid flowchart with one box per visit to a
location, and each box carries two bars on its own scale:

* **IRL**: from the visit's first post to the next visit's first post, so
  it includes the waiting between posts. That is the real cost of a scene.
* **In-game**: whatever Lewis writes into ``in_game`` in the data file.
  Nothing is estimated. An empty one says so and names the key to fill.

Below the chart, every visit gets a section with its events, each linked
to its post where the archive has an id (2026 onward).
"""

import re
from dataclasses import dataclass, field
from datetime import datetime

from messages import Message

BAR_CELLS = 10
_UNIT_HOURS = {"w": 168, "d": 24, "h": 1, "m": 1 / 60}
# "2d 4h", "3 days", "1 week and 2 hours", "90 mins".
_IN_GAME = re.compile(r"(\d+(?:\.\d+)?)\s*(w(?:ee)?k?s?|d(?:ays?)?|h(?:ours?|rs?)?|m(?:in(?:ute)?s?)?)\b")


@dataclass
class Visit:
    key: str                 # "2026-06#14": month and first message
    location: str
    first: Message
    last: Message
    events: list = field(default_factory=list)   # (Message, text)
    cues: list = field(default_factory=list)
    messages: int = 0
    area: str = ""           # the wider place this room is inside


def group_areas(visits: list[Visit]) -> list[tuple[str, list[int]]]:
    """Back-to-back visits inside one area, as (area, visit indexes).

    Lewis, 2026-09-16: "locations breaking down into sub locations aka rooms
    within their overall location node". An area left and later returned to
    is a second group, because the timeline is in order.
    """
    groups: list[tuple[str, list[int]]] = []
    for i, v in enumerate(visits):
        if not groups or groups[-1][0] != v.area:
            groups.append((v.area, []))
        groups[-1][1].append(i)
    return groups


def area_in_game(hours: list[float | None]) -> float | None:
    """An area's in-game time: the sum of its rooms, but only once every room
    has one. A partial sum would read as a total and understate it."""
    return None if any(h is None for h in hours) else sum(hours)


def build_visits(data: dict, months: dict[str, list[Message]]) -> list[Visit]:
    """Consecutive scenes at the same place, across months, become one visit."""
    # ⚠️ Separate maps. The C04 pilot's model named the whole temple after
    # its first room, so one name had to become "The Temple" as an area and
    # "Room 5: The Grand Hall" as a room. One shared map cannot say both.
    renames = data.get("renames") or {}
    area_renames = data.get("area_renames") or {}
    visits: list[Visit] = []
    for month in sorted(data["months"]):
        msgs = months.get(month) or []
        for s in data["months"][month]["scenes"]:
            if s["last"] > len(msgs):
                continue  # archive shrank under the data; skip, never guess
            raw_area = s.get("area") or s["location"]
            area = area_renames.get(raw_area, raw_area)
            location = renames.get(s["location"], s["location"])
            first, last = msgs[s["first"] - 1], msgs[s["last"] - 1]
            if not visits or (visits[-1].area, visits[-1].location) != (area, location):
                visits.append(Visit(f"{month}#{s['first']}", location, first, last,
                                    area=area))
            v = visits[-1]
            v.last = last
            v.messages += s["last"] - s["first"] + 1
            v.events += [(msgs[e["at"] - 1], e["text"]) for e in s["events"]]
            v.cues += [(first, c) for c in s["time_cues"]]
    return visits


def irl_hours(visits: list[Visit], i: int) -> float:
    end = visits[i + 1].first.at if i + 1 < len(visits) else visits[i].last.at
    return max((end - visits[i].first.at).total_seconds() / 3600, 0)


def in_game_hours(text: str | None) -> float | None:
    """Hours from "2d 4h", "3 days", "1w". None when it cannot be read.

    ⚠️ All or nothing: text with anything left over ("about 3 days", "a
    while") gets no bar, rather than a bar built from the part it understood.
    """
    if not text:
        return None
    lowered = text.lower()
    parts = _IN_GAME.findall(lowered)
    leftover = re.sub(r"\band\b|[\s,+]", "", _IN_GAME.sub("", lowered))
    if not parts or leftover:
        return None
    return sum(float(n) * _UNIT_HOURS[u[0]] for n, u in parts)


def duration(hours: float) -> str:
    if hours < 1:
        return "<1h"
    total = int(round(hours))
    w, rest = divmod(total, 168)
    d, h = divmod(rest, 24)
    shown = [f"{n}{u}" for n, u in ((w, "w"), (d, "d"), (h, "h")) if n]
    return " ".join(shown[:2])


def bar(value: float | None, longest: float) -> str:
    if value is None or longest <= 0:
        return ""
    filled = max(1, round(BAR_CELLS * value / longest)) if value > 0 else 0
    return "▰" * filled + "▱" * (BAR_CELLS - filled)


def _label(text: str) -> str:
    return text.replace('"', "#quot;")


def _day(at: datetime) -> str:
    return f"{at:%d %b %Y}".lstrip("0")


def render(data: dict, months: dict[str, list[Message]],
           data_file: str = "timelines/<campaign>.json") -> str:
    visits = build_visits(data, months)
    in_game = data.get("in_game") or {}
    irl = [irl_hours(visits, i) for i in range(len(visits))]
    game = [in_game_hours(in_game.get(v.key)) for v in visits]
    longest_irl = max(irl, default=0)
    longest_game = max((g for g in game if g is not None), default=0)
    groups = group_areas(visits)
    area_irl = [sum(irl[i] for i in idx) for _a, idx in groups]
    area_game = [area_in_game([game[i] for i in idx]) for _a, idx in groups]
    longest_area_irl = max(area_irl, default=0)
    longest_area_game = max((g for g in area_game if g is not None), default=0)
    title = f"{data['code']} {data['campaign']}: Timeline"
    out = [f"# {title}", "",
           "Where the party went, in order. Each outer box is an area, and "
           "each box inside it is a room or spot the party spent time in.",
           "",
           "- 🗓️ **IRL** is measured from the first post there to the first "
           "post at the next place.",
           "- ⏳ **In-game** time is filled in by the GM. An area's total "
           "appears once all of its rooms have one.",
           "", "```mermaid", "flowchart TD"]
    for n, (area, idx) in enumerate(groups):
        header = [f"{n + 1}. {_label(area)}",
                  f"🗓️ IRL {duration(area_irl[n])} "
                  f"{bar(area_irl[n], longest_area_irl)}",
                  (f"⏳ In-game {duration(area_game[n])} "
                   f"{bar(area_game[n], longest_area_game)}"
                   if area_game[n] is not None else "⏳ In-game ?")]
        out += [f'    subgraph a{n}["{" · ".join(header)}"]', "    direction TB"]
        for r, i in enumerate(idx):
            v, g = visits[i], in_game.get(visits[i].key)
            lines = [f"<b>{n + 1}.{r + 1} {_label(v.location)}</b>",
                     f"🗓️ IRL {duration(irl[i])} {bar(irl[i], longest_irl)}",
                     (f"⏳ In-game {_label(g)} {bar(game[i], longest_game)}".rstrip()
                      if g else "⏳ In-game ?")]
            out.append(f'        v{i}["{"<br/>".join(lines)}"]')
        out.append("    end")
    # Edges after every subgraph: declared inside one, an edge to a node in
    # the next would pull that node into the wrong box.
    out += [f"    v{i - 1} --> v{i}" for i in range(1, len(visits))]
    out += ["```", ""]
    numbers = {i: f"{n + 1}.{r + 1}" for n, (_a, idx) in enumerate(groups)
               for r, i in enumerate(idx)}
    starts = {idx[0]: n for n, (_a, idx) in enumerate(groups)}
    for i, v in enumerate(visits):
        if i in starts:
            n = starts[i]
            area, idx = groups[n]
            first, last = visits[idx[0]].first, visits[idx[-1]].last
            total = (duration(area_game[n]) if area_game[n] is not None
                     else "not all rooms filled in")
            out += [f"## {n + 1}. {area}", "",
                    f"- 🗓️ **IRL:** {_day(first.at)} to {_day(last.at)}, "
                    f"{duration(area_irl[n])}",
                    f"- ⏳ **In-game:** {total}", ""]
        g = in_game.get(v.key)
        out += [f"### {numbers[i]} {v.location}", "",
                f"- 🗓️ **IRL:** {_day(v.first.at)} to {_day(v.last.at)}, "
                f"{duration(irl[i])}, {v.messages} posts",
                f"- ⏳ **In-game:** {g}" if g else
                f"- ⏳ **In-game:** not filled in (`\"{v.key}\"` in "
                f"`{data_file}`)"]
        if v.cues:
            cues = "; ".join(f"\"{c}\"" for _m, c in v.cues)
            out.append(f"- 💬 **Time said in posts:** {cues}")
        out += ["", "**Events**", ""]
        for m, text in v.events:
            link = f" [↗]({m.link})" if m.link else ""
            out.append(f"- {m.at:%d %b}: {text}{link}")
        out.append("")
    return "\n".join(out).rstrip() + "\n"
