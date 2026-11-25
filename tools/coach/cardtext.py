#!/usr/bin/env python3
"""Print card text for one or more cards, from YGOPRODeck, with a local cache.

    ./cardtext.py "Rikka Black Princess" "Contrast HERO Chaos"
    ./cardtext.py --fuzzy Daredevil        # partial name search
    ./cardtext.py --refresh "Card Name"    # ignore the cache

Cache: tools/coach/cache/<name>.json (card text rarely changes; use --refresh after errata).

If YGOPRODeck can't be reached (it is blocked from the cloud container), it falls back to
ProjectIgnis BabelCDB (raw.githubusercontent.com), downloaded once to ~/.cache/babelcdb.
"""
import json, os, sqlite3, sys, urllib.parse, urllib.request

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


BABEL = "https://raw.githubusercontent.com/ProjectIgnis/BabelCDB/master/"
BABEL_DIR = os.path.expanduser("~/.cache/babelcdb")
# Master Duel names that BabelCDB spells differently (it uses TCG/OCG names).
ALIASES = {
    "Rikka Sacred Queen Strenna": "Rikka Empress Strenna",
    "Rikka Moonlit Waters": "Rikka June Moon",
    "Teardrop the Rikka Sacred Queen": "Teardrop the Rikka Empress",
}
RACES = ["Warrior", "Spellcaster", "Fairy", "Fiend", "Zombie", "Machine", "Aqua", "Pyro", "Rock", "Winged Beast",
         "Plant", "Insect", "Thunder", "Dragon", "Beast", "Beast-Warrior", "Dinosaur", "Fish", "Sea Serpent", "Reptile",
         "Psychic", "Divine-Beast", "Creator God", "Wyrm", "Cyberse", "Illusion"]
ATTRS = ["EARTH", "WATER", "FIRE", "WIND", "LIGHT", "DARK", "DIVINE"]


def babel(name, fuzzy=False):
    os.makedirs(BABEL_DIR, exist_ok=True)
    out = []
    for f in ("cards.cdb", "prerelease-imph.cdb"):
        path = os.path.join(BABEL_DIR, f)
        if not os.path.exists(path):
            urllib.request.urlretrieve(BABEL + f, path)
        db = sqlite3.connect(path)
        q = "select t.name, t.desc, d.type, d.atk, d.def, d.level, d.race, d.attribute from texts t join datas d on t.id = d.id where "
        n = ALIASES.get(name, name)
        rows = db.execute(q + ("t.name like ?" if fuzzy else "t.name = ? collate nocase"), (f"%{n}%" if fuzzy else n,)).fetchall()
        for nm, desc, typ, atk, df, lv, race, attr in rows:
            kind = "Spell Card" if typ & 2 else "Trap Card" if typ & 4 else "Monster"
            for bit, word in ((0x40, "Fusion"), (0x2000, "Synchro"), (0x800000, "XYZ"), (0x4000000, "Link")):
                if typ & bit:
                    kind = word + " Monster"
            c = {"name": name if nm == n else nm, "type": kind, "desc": desc}
            if typ & 1:
                c["race"] = next((r for i, r in enumerate(RACES) if race >> i & 1), "")
                c["attribute"] = next((a for i, a in enumerate(ATTRS) if attr >> i & 1), "")
                c["atk"] = atk
                if typ & 0x4000000:
                    c["linkval"] = lv & 0xFF
                else:
                    c["level"], c["def"] = lv & 0xFF, df
            out.append(c)
    return out


def lookup(name, fuzzy=False, refresh=False):
    if fuzzy:
        try:
            return fetch({"fname": name})
        except OSError:
            return babel(name, fuzzy=True)
    path = os.path.join(CACHE, "".join(c if c.isalnum() else "_" for c in name) + ".json")
    if not refresh and os.path.exists(path):
        return json.load(open(path))
    try:
        data = fetch({"name": name}) or fetch({"fname": name})[:1]
    except OSError:
        data = babel(name)[:1]
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
        q = lambda v: "?" if v == -2 else v
        stats.append(f"ATK {q(c['atk'])}" + (f" / DEF {q(c['def'])}" if c.get("def") is not None else ""))
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
