#!/usr/bin/env python3
"""Print card text for one or more cards, from YGOPRODeck, with a local cache.

    ./cardtext.py "Rikka Black Princess" "Contrast HERO Chaos"
    ./cardtext.py --fuzzy Daredevil        # partial name search
    ./cardtext.py --refresh "Card Name"    # ignore the cache

Cache: tools/coach/cache/<name>.json (card text rarely changes; use --refresh after errata).
"""
import json, os, sys, urllib.parse, urllib.request

API = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def fetch(params):
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(params), headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.load(r).get("data", [])
    except urllib.error.HTTPError as e:
        if e.code == 400:  # no match
            return []
        raise


def lookup(name, fuzzy=False, refresh=False):
    if fuzzy:
        return fetch({"fname": name})
    path = os.path.join(CACHE, "".join(c if c.isalnum() else "_" for c in name) + ".json")
    if not refresh and os.path.exists(path):
        return json.load(open(path))
    data = fetch({"name": name}) or fetch({"fname": name})[:1]
    if data:
        os.makedirs(CACHE, exist_ok=True)
        json.dump(data, open(path, "w"))
    return data


def show(c):
    stats = [c.get("type", "")]
    for k in ("race", "attribute"):
        if c.get(k):
            stats.append(c[k])
    if c.get("level") is not None and not c.get("linkval"):
        stats.append(("Rank " if "XYZ" in c.get("type", "") else "Level ") + str(c["level"]))
    if c.get("linkval"):
        stats.append(f"Link-{c['linkval']} " + "/".join(c.get("linkmarkers", [])))
    if c.get("atk") is not None:
        stats.append(f"ATK {c['atk']}" + (f" / DEF {c['def']}" if c.get("def") is not None else ""))
    print(f"## {c['name']}\n{' | '.join(stats)}\n{c['desc']}\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    fuzzy = "--fuzzy" in args
    refresh = "--refresh" in args
    names = [a for a in args if not a.startswith("--")]
    if not names:
        sys.exit(__doc__)
    for n in names:
        cards = lookup(n, fuzzy, refresh)
        if not cards:
            print(f"## {n}\nNOT FOUND (check the spelling, or try --fuzzy)\n")
        for c in cards[: 8 if fuzzy else 1]:
            show(c)
