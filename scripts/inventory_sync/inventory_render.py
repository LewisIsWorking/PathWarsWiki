"""Render one campaign's daily inventory snapshots as a wiki page: what everyone holds now, and every change by day.

Added 2026-10-17 (Lewis: "track party inventory and character inventory on a daily basis so if a player
accidentally (or cheats) more gold or items, then it's checkable when items were added").

A snapshot is the bot's ``data/inventories/<code>/<YYYY-MM-DD>.json``::

    {"code": "C07", "campaign": "...", "date": "2026-10-18",
     "actors": [{"id": "...", "name": "Lai", "kind": "character" | "party", "owners": ["Terra"],
                 "currency": {"credits": 12}, "items": [{"name": "...", "type": "...", "quantity": 1}]}]}

⭐ Items are compared by name and type, not by id: Foundry gives an item a new id whenever it moves between
sheets, so an id diff would show every hand-over as one loss and one gain with nothing to tie them.
⭐ A gain on one sheet that matches a loss on another the same day is shown as a move, so a stash hand-out does
not look like an item appearing from nowhere. Only what is left unexplained reads as gained or lost.
"""

from collections import Counter


def page_name(code: str) -> str:
    return f"{code}-Inventory.md"


def holdings(actor: dict) -> Counter:
    """(name, type) -> total quantity, so two stacks of one item count as one line."""
    held = Counter()
    for item in actor.get("items") or []:
        if item.get("name"):
            held[(item["name"], item.get("type") or "")] += int(item.get("quantity") or 1)
    return held


def _by_actor(snapshot: dict) -> dict:
    return {a.get("id") or a.get("name"): a for a in snapshot.get("actors") or [] if a.get("name")}


def diff(before: dict, after: dict) -> list[str]:
    """One line per change from ``before`` to ``after``: moves, then gains and losses, then currency."""
    old, new = _by_actor(before), _by_actor(after)
    gains, losses = [], []  # (actor name, (item name, type), quantity)
    for key in sorted(set(old) | set(new), key=lambda k: (new.get(k) or old.get(k))["name"]):
        a, b = old.get(key, {}), new.get(key, {})
        name = (b or a)["name"]
        was, now = holdings(a), holdings(b)
        for item in sorted(set(was) | set(now)):
            change = now[item] - was[item]
            if change > 0:
                gains.append([name, item, change])
            elif change < 0:
                losses.append([name, item, -change])
    lines = []
    for gain in gains:
        for loss in losses:
            if gain[2] and loss[2] and gain[1] == loss[1] and gain[0] != loss[0]:
                moved = min(gain[2], loss[2])
                lines.append(f"- {_qty(moved)}{gain[1][0]} moved from {loss[0]} to {gain[0]}")
                gain[2] -= moved
                loss[2] -= moved
    lines += [f"- **{who}** gained {_qty(n)}{item[0]}" for who, item, n in gains if n]
    lines += [f"- **{who}** lost {_qty(n)}{item[0]}" for who, item, n in losses if n]
    for key in sorted(set(old) | set(new), key=lambda k: (new.get(k) or old.get(k))["name"]):
        a, b = old.get(key, {}), new.get(key, {})
        was, now = a.get("currency") or {}, b.get("currency") or {}
        for coin in sorted(set(was) | set(now)):
            change = (now.get(coin) or 0) - (was.get(coin) or 0)
            if change:
                lines.append(f"- **{(b or a)['name']}** {coin}: {was.get(coin) or 0} to {now.get(coin) or 0} "
                             f"({'+' if change > 0 else ''}{change})")
    for key in sorted(set(new) - set(old)):
        lines.insert(0, f"- {new[key]['name']} appears in the records")
    for key in sorted(set(old) - set(new)):
        lines.insert(0, f"- {old[key]['name']} is no longer in the records")
    return lines


def _qty(n: int) -> str:
    return f"{n} x " if n != 1 else ""


def _cell(text: str) -> str:
    """A table cell: a "|" in an item name would otherwise split the row."""
    return (text or "").replace("|", r"\|")


def _currency(actor: dict) -> str:
    coins = {k: v for k, v in (actor.get("currency") or {}).items() if v}
    return ", ".join(f"{v} {k}" for k, v in sorted(coins.items())) or "none"


def render_actor(actor: dict) -> list[str]:
    owners = ", ".join(actor.get("owners") or [])
    kind = "Party" if actor.get("kind") == "party" else "Character"
    out = [f"### {actor['name']}", "", f"{kind}{f', played by {owners}' if owners else ''}. "
           f"Currency: {_currency(actor)}.", ""]
    held = holdings(actor)
    if not held:
        return out + ["Carries nothing.", ""]
    out += ["| Item | Type | Quantity |", "|---|---|---|"]
    out += [f"| {_cell(name)} | {_cell(kind_)} | {n} |" for (name, kind_), n in sorted(held.items())]
    return out + [""]


def render_page(snapshots: list[dict]) -> str:
    """``snapshots`` oldest first, all for one campaign."""
    latest = snapshots[-1]
    title = f"{latest['code']} {latest.get('campaign') or ''}".strip()
    out = [f"# {title} inventories", "",
           f"Every character's and party's items and currency, recorded each morning while Foundry is closed for "
           f"its update. Generated from the Path Wars Nudge bot's records; latest record {latest['date']}.", "",
           "## Now", ""]
    actors = sorted(latest.get("actors") or [], key=lambda a: (a.get("kind") != "party", a.get("name") or ""))
    for actor in actors:
        out += render_actor(actor)
    out += ["## Changes by day", ""]
    days = []
    for before, after in zip(snapshots, snapshots[1:]):
        lines = diff(before, after)
        if lines:
            days.append([f"### {after['date']}", "", f"Since {before['date']}:", ""] + lines + [""])
    if not days:
        out.append("No changes recorded yet.")
    for day in reversed(days):
        out += day
    return "\n".join(out).rstrip("\n") + "\n"
