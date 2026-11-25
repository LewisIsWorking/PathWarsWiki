#!/usr/bin/env python3
"""Live-match helper: find a pre-checked line for a hand, check a pasted line, read card text.
Built to answer in seconds while the Master Duel timer runs. Run through ./quick (it installs CUE).

  ./quick setup                       install CUE if missing, warm caches, run every check (~5 s)
  ./quick find mudan moonlit predap   best checked lines for this hand (short names work)
       --field "Rikka Princess"         cards already on your field
       --droll / --darklaw / --cactus   situation flags (shown against each line's conditions)
       --late   late game: allow lines that assume cards already gone from the Deck (deckGone)
       --deck RikkaM1                   default PredaRikka
  ./quick check my_line.cue           check one pasted line (file, or - for stdin); prints it ready to send
  ./quick show "Line C"               print a saved line's steps (any part of its name)
  ./quick card bp "dark law"          card text, offline from the cache (short names work)
  ./quick precache                    fetch text for every deck card + opponents.txt into the cache
  ./quick names                       the short names you can type
"""
import difflib, hashlib, json, os, re, shutil, signal, subprocess, sys, tempfile
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

HERE = os.path.dirname(os.path.abspath(__file__))
LC = os.path.normpath(os.path.join(HERE, "..", "line-check"))
CACHE_DIR = os.path.expanduser("~/.cache/pww-quick")
sys.path.insert(0, HERE)

# Short names for typing fast. Lower case. Anything else: any unique part of the name works.
ALIASES = {
    "bp": "Rikka Black Princess", "black princess": "Rikka Black Princess",
    "rp": "Rikka Princess", "princess": "Rikka Princess",
    "petal": "Rikka Petal", "mudan": "Mudan the Rikka Fairy", "hellebore": "Hellebore the Rikka Fairy",
    "primrose": "Primrose the Rikka Fairy Duo", "primula": "Primula the Rikka Fairy",
    "konkon": "Rikka Konkon", "glamour": "Rikka Glamour", "moonlit": "Rikka Moonlit Waters",
    "mw": "Rikka Moonlit Waters", "sheet": "Rikka Sheet",
    "rqs": "Rikka Queen Strenna", "queen strenna": "Rikka Queen Strenna",
    "sqs": "Rikka Sacred Queen Strenna", "sacred queen": "Rikka Sacred Queen Strenna",
    "kanzashi": "Kanzashi the Rikka Queen", "teardrop": "Teardrop the Rikka Queen",
    "sacred teardrop": "Teardrop the Rikka Sacred Queen", "hyperyton": "Sacred Tree Beast, Hyperyton",
    "orea": "Orea, the Sylvan High Arbiter",
    "longi": "Predaplant Longinephila", "longinephila": "Predaplant Longinephila",
    "byblisp": "Predaplant Byblisp", "lilizard": "Predaplant Lilizard",
    "dracaena": "Princess Dracaena, the Thirsting Tree", "dra": "Princess Dracaena, the Thirsting Tree",
    "predap": "Predaprimitive", "prim": "Predaprimitive", "predaprimitive": "Predaprimitive",
    "if": "Instant Fusion", "instant": "Instant Fusion", "sp": "Super Polymerization",
    "super poly": "Super Polymerization", "superpoly": "Super Polymerization", "poly": "Polymerization",
    "ambulo": "Predaplant Ambulomelides", "bal teah": "Predaplant Bal Teah", "balteah": "Predaplant Bal Teah",
    "jasmine": "Aromaseraphy Jasmine", "daredevil": "Predaplant Daredevil",
    "venom": "Starving Venom Fusion Dragon", "svfd": "Starving Venom Fusion Dragon",
    "garura": "Garura, Wings of Resonant Life", "crystal wing": "Crystal Wing Synchro Dragon",
    "dancepione": "Sylvan Dancepione", "sylvan": "Sylvan Dancepione",
    "cactus": "Cactus Bouncer",
    "ash": "Ash Blossom & Joyous Spring", "droll": "Droll & Lock Bird", "maxx": "Maxx \"C\"",
    "maxx c": "Maxx \"C\"", "purulia": "Mulcharmy Purulia", "fuwalos": "Mulcharmy Fuwalos",
    "ttt": "Triple Tactics Talent", "droplet": "Forbidden Droplet", "em": "Evenly Matched",
    "evenly": "Evenly Matched", "dominus": "Dominus Impulse", "impulse": "Dominus Impulse",
    "imperm": "Infinite Impermanence", "foolish": "Foolish Burial", "crossout": "Crossout Designator",
    # opponents
    "dark law": "Masked HERO Dark Law", "chaos": "Contrast HERO Chaos", "wingman": "Elemental HERO Shining Neos Wingman",
    "dragoon": "Red-Eyes Dark Dragoon", "zero": "Sky Striker Ace = Zero", "widow": "Sky Striker Mecha - Widow Anchor",
    "widow anchor": "Sky Striker Mecha - Widow Anchor", "crown": "Forbidden Crown", "fortress": "Machina Fortress",
    "strelitzia": "Elfnote Seraphim Strelitzia", "baronne": "Baronne de Fleur", "little knight": "S:P Little Knight",
    "spl": "S:P Little Knight", "belle": "Ghost Belle & Haunted Mansion", "veiler": "Effect Veiler",
    "nibiru": "Nibiru, the Primal Being", "infinity": "Cyber Dragon Infinity",
}

LOCKS = {"plant": "Plants only", "plant_or_dragon": "Plants/Dragons only",
         "extra_plant_xyz": "Extra Deck: Plant Xyz only", "no_special": "no Special Summons"}


def die(msg):
    print(msg)
    sys.exit(2)


# ---------- CUE ----------

def cue_bin():
    for p in (shutil.which("cue"), os.path.expanduser("~/.local/bin/cue"), os.path.expanduser("~/go/bin/cue")):
        if p and os.path.exists(p):
            return p
    die("CUE isn't installed. Run ./quick setup (or: tools/coach/install-cue.sh).")


def cue_files(d):
    return sorted(f for f in os.listdir(d) if f.endswith(".cue"))


def export_lines(d=LC, use_cache=True):
    """All lines as JSON (with each line's violations). Cached by the .cue files' content."""
    h = hashlib.sha1()
    for f in cue_files(d):
        h.update(f.encode()); h.update(open(os.path.join(d, f), "rb").read())
    path = os.path.join(CACHE_DIR, h.hexdigest() + ".json")
    if use_cache and os.path.exists(path):
        return json.load(open(path))
    r = subprocess.run([cue_bin(), "export", ".", "-e", "lines", "--out", "json"], cwd=d, capture_output=True, text=True)
    if r.returncode:
        return {"__error__": clean_cue_err(r.stderr)}
    data = json.loads(r.stdout)
    if use_cache:
        os.makedirs(CACHE_DIR, exist_ok=True)
        json.dump(data, open(path, "w"))
    return data


def clean_cue_err(err):
    """CUE's errors, shorter: one line per bad field, steps counted from 1, allowed values listed."""
    lines = [l.rstrip() for l in err.splitlines() if l.strip()]
    allowed, bad, out = {}, {}, []
    for l in lines:
        m = re.match(r'^(.*?): conflicting values (\S+) and (\S+):?$', l)
        if m:
            field, a, b = m.groups()
            allowed.setdefault(field, []).append(a); bad[field] = b
            continue
        if re.match(r"^\s+\./[\w.]+:\d+:\d+$", l) or "errors in empty disjunction" in l:
            continue
        out.append(l)
    for f, vals in allowed.items():
        out.insert(0, f"{f}: {bad[f]} isn't allowed. Allowed: {', '.join(v.strip(chr(34)) for v in vals)}")
    text = "\n".join(out[:20]).replace(LC + "/", "")
    return re.sub(r"steps\.(\d+)", lambda m: f"step {int(m.group(1)) + 1}", text)


# ---------- names ----------

_NAMES = None


def known_names():
    """Card names the checker knows (cards.cue + decks) plus opponents.txt and the text cache."""
    global _NAMES
    if _NAMES is None:
        names = set()
        for f in ("cards.cue", "decks.cue"):
            names |= set(re.findall(r'^\s*"((?:[^"\\]|\\.)+)":\s*[{0-9]', open(os.path.join(LC, f)).read(), re.M))
        names = {n.replace('\\"', '"') for n in names} - {"PredaRikka", "RikkaM1"}
        opp = os.path.join(HERE, "opponents.txt")
        if os.path.exists(opp):
            names |= {l.strip() for l in open(opp) if l.strip() and not l.startswith("#")}
        cache = os.path.join(HERE, "cache")
        if os.path.isdir(cache):
            for f in os.listdir(cache):
                try:
                    for c in json.load(open(os.path.join(cache, f))):
                        names.add(c["name"])
                except Exception:
                    pass
        _NAMES = sorted(names)
    return _NAMES


def resolve(arg, pool=None):
    """Short or partial name -> full card name. Returns (name, None) or (None, error)."""
    pool = pool or known_names()
    a = arg.strip().lower()
    if a in ALIASES:
        return ALIASES[a], None
    exact = [n for n in pool if n.lower() == a]
    if exact:
        return exact[0], None
    sub = [n for n in pool if a in n.lower()]
    if len(sub) == 1:
        return sub[0], None
    starts = [n for n in sub if any(w.startswith(a) for w in re.split(r"[ ,&\-]+", n.lower()))]
    if len(starts) == 1:
        return starts[0], None
    if sub:
        return None, f"'{arg}' is ambiguous: " + " | ".join(sub[:6])
    close = difflib.get_close_matches(arg, pool, n=3, cutoff=0.5)
    return None, f"'{arg}' isn't a card I know" + (f" (did you mean: {' | '.join(close)}?)" if close else "")


def base(n):
    return n.split("#")[0]


def show_name(n):
    return re.sub(r"#(\d+)", lambda m: f" ({m.group(1)}nd copy)" if m.group(1) == "2" else f" (copy {m.group(1)})", n)


# ---------- lines ----------

def hand_needs(line):
    """Cards from the line's starting hand that the steps play from the hand (copies counted).
    Conservative: a hand-zone use of a card that the line also searched still counts as needed."""
    uses = {}
    for s in line["steps"]:
        for u in ([s["card"]] if s.get("zone") == "hand" else []) + list(s.get("fromHand", [])):
            uses[base(u)] = uses.get(base(u), 0) + 1
    in_hand = {}
    for h in line["hand"]:
        in_hand[base(h)] = in_hand.get(base(h), 0) + 1
    return {k: min(v, in_hand[k]) for k, v in uses.items() if k in in_hand}


def conditions(line):
    c = []
    if line.get("startField"):
        c.append("needs on your field: " + ", ".join(line["startField"]))
    if line.get("darkLaw"):
        c.append("under Dark Law")
    if line.get("drollFrom"):
        c.append(f"Droll lands at step {line['drollFrom']}")
    for l in line.get("startLocks", []):
        c.append("lock already on: " + LOCKS.get(l, l))
    if line.get("deckGone"):
        c.append("already gone from your Deck: " + ", ".join(f"{k}" + (f" x{v}" if v > 1 else "") for k, v in line["deckGone"].items()))
    if line.get("lethal"):
        c.append(f"lethal vs {line['lethal']['lp']} LP: " + ", ".join(line["lethal"]["attackers"]))
    return c


def step_text(s):
    c, a, z, e = show_name(s["card"]), s["action"], s.get("zone", "field"), s.get("effect", "")
    where = {"hand": " from hand", "gy": " from GY", "deck": " from Deck"}.get(z, "")
    mats = " + ".join(show_name(x).replace("opp:", "their ") for x in s.get("consumes", []))
    summ = {"normal_summon": "Normal Summon", "special_summon": "Special Summon", "xyz": "Xyz Summon",
            "synchro": "Synchro Summon", "link": "Link Summon", "fusion": "Fusion Summon", "set": "Set"}
    if a in summ:
        t = f"{summ[a]} {c}" + (where if a == "special_summon" else "")
        if mats:
            t += (" using " if a in ("xyz", "synchro", "link", "fusion") else ", Tributing ") + mats
        if s.get("rankUp"):
            t += " (on top of it)"
        if e and e not in ("summon_self",):
            t += f" [{e}]"
    elif a == "activate":
        t = f"Activate {c}" + (" from GY" if z == "gy" else "") + (f" [{e}]" if e and e != "activate" else "")
        if mats:
            t += f", Tributing {mats}"
    else:
        t = f"{c}" + (" in GY" if z == "gy" else " in hand" if z == "hand" else "") + f": {e or 'effect'}"
        if mats:
            t += f", Tributing/using {mats}"
    if s.get("detach"):
        t += f", detach {s['detach']}"
    if s.get("fromHand"):
        t += ", from hand: " + ", ".join(map(show_name, s["fromHand"]))
    if s.get("summons"):
        t += f" -> summon {show_name(s['summons'])}"
    if s.get("fromDeck"):
        t += " | Deck: " + ", ".join(map(show_name, s["fromDeck"]))
    if s.get("attach"):
        t += " | attach " + ", ".join(map(show_name, s["attach"]))
    if s.get("setLevel"):
        t += " | " + ", ".join(f"{show_name(k)} becomes Level {v}" for k, v in s["setLevel"].items())
    if s.get("sendsToGY"):
        t += " (send to GY)"
    if s.get("lock"):
        t += f" (lock: {LOCKS.get(s['lock'], s['lock'])})"
    if s.get("note"):
        t += f"  -- {s['note']}"
    return t


def print_line(name, line, header=True):
    st = line["status"].upper()
    if header:
        print(f"=== {name}  [{st}]")
    for c in conditions(line):
        print(f"    ({c})")
    for i, s in enumerate(line["steps"], 1):
        print(f"{i:>3}. {step_text(s)}")
    end = line.get("end", {})
    if end:
        print("    END: " + ", ".join(end.get("mmz", []) + end.get("emz", [])))
    if line.get("violations"):
        for v in line["violations"]:
            print(f"    !! {v}")


# ---------- commands ----------

def parse_flags(argv, flags, opts):
    rest, f, o = [], set(), {}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in flags:
            f.add(a)
        elif a in opts:
            o.setdefault(a, []).append(argv[i + 1]); i += 1
        else:
            rest.append(a)
        i += 1
    return rest, f, o


def split_cards(args):
    """Card tokens from the command line. Accepts commas, '2x ash', 'ash x2', and '2x' / 'x2' as separate words."""
    parts = [p.strip() for a in args for p in a.split(",") if p.strip()]
    out, mult = [], 1
    for p in parts:
        if re.fullmatch(r"\d+\s*x", p, re.I):
            mult = int(p[:-1]); continue
        if re.fullmatch(r"x\s*\d+", p, re.I) and out:
            out += [out[-1]] * (int(p[1:]) - 1); continue
        m = re.match(r"^(\d+)\s*x\s+(.+)$|^(.+?)\s+x\s*(\d+)$", p, re.I)
        if m:
            n, nm = (m.group(1), m.group(2)) if m.group(1) else (m.group(4), m.group(3))
            out += [nm] * int(n)
        else:
            out += [p] * mult
        mult = 1
    return out


def recheck(lines_by_name, deck):
    """Re-run the checker on lines with their deck switched (e.g. a pure-Rikka line in PredaRikka). ~0.2 s."""
    tmp = tempfile.mkdtemp(prefix="quickretarget-")
    try:
        for f in ("schema.cue", "cards.cue", "decks.cue"):
            shutil.copy(os.path.join(LC, f), tmp)
        body = {}
        for n, l in lines_by_name.items():
            l = {k: v for k, v in l.items() if k not in ("violations", "name")}
            l["deck"] = deck
            body[n] = l
        open(os.path.join(tmp, "retarget.cue"), "w").write("package lines\n\nlines: " + json.dumps(body, indent=1) + "\n")
        r = subprocess.run([cue_bin(), "export", ".", "-e", "lines", "--out", "json"], cwd=tmp, capture_output=True, text=True)
        return json.loads(r.stdout) if r.returncode == 0 else {}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cmd_find(argv):
    rest, flags, opts = parse_flags(argv, {"--droll", "--darklaw", "--cactus", "--late", "--all"}, {"--field", "--deck"})
    deck = opts.get("--deck", ["PredaRikka"])[0]
    hand, errs = {}, []
    for a in split_cards(rest):
        n, err = resolve(a)
        if err:
            errs.append(err)
        else:
            hand[n] = hand.get(n, 0) + 1
    field = []
    for a in split_cards(opts.get("--field", [])):
        n, err = resolve(a)
        errs.append(err) if err else field.append(n)
    if errs:
        print("\n".join("NAME: " + e for e in errs))
        if not hand:
            sys.exit(2)
    print("HAND: " + ", ".join(f"{k}" + (f" x{v}" if v > 1 else "") for k, v in hand.items()) +
          (f"   FIELD: {', '.join(field)}" if field else ""))
    lines = export_lines()
    if "__error__" in lines:
        die("The line files don't load:\n" + lines["__error__"])
    fits, near, traps, other = [], [], [], []
    for name, l in lines.items():
        need = hand_needs(l)
        miss = {k: v - hand.get(k, 0) for k, v in need.items() if hand.get(k, 0) < v}
        miss.update({f"on field: {x}": 1 for x in l.get("startField", []) if x not in field})
        if l["status"] == "known_bad":
            if not miss and l["deck"] == deck:
                traps.append((name, l))
            continue
        situation = []
        if l.get("darkLaw") != ("--darklaw" in flags):
            situation.append("Dark Law " + ("assumed" if l.get("darkLaw") else "NOT checked"))
        if bool(l.get("drollFrom")) != ("--droll" in flags):
            situation.append("Droll " + ("assumed" if l.get("drollFrom") else "NOT checked"))
        if ("no_special" in l.get("startLocks", [])) != ("--cactus" in flags):
            situation.append("Cactus lock " + ("assumed" if l.get("startLocks") else "NOT checked"))
        if bool(l.get("deckGone")) and "--late" not in flags:
            situation.append("late game only: assumes " + ", ".join(l["deckGone"]) + " gone from the Deck (use --late)")
        rank = (len(situation), -sum(need.values()), 0 if l["status"] == "proven" else 1)
        entry = (rank, name, l, need, miss, situation, l.get("violations", []))
        if l["deck"] != deck:
            if not miss:
                other.append(entry)
            continue
        (near if miss else fits).append(entry)
    other_report = []
    if other:  # lines written for the other deck: re-check them for this deck now (~0.2 s)
        re_l = recheck({e[1]: e[2] for e in other}, deck)
        for rank, name, l, need, miss, sit, _ in other:
            v = re_l.get(name, {}).get("violations", ["didn't load"])
            if v:
                other_report.append(f"  - {name} [{l['deck']} line]: FAILS in {deck}: " + "; ".join(v))
            else:
                fits.append((rank, name, {**re_l[name], "from_deck": l["deck"]}, need, miss, sit, []))
    fits.sort(key=lambda e: e[0])
    near.sort(key=lambda e: (sum(e[4].values()), e[0]))
    if traps:
        print("\nDON'T (known mistakes with this hand):")
        for name, l in traps:
            print(f"  x {name}: " + "; ".join(l.get("violations", [])))
    if fits:
        shown = fits if "--all" in flags else fits[:3]
        print(f"\n{len(fits)} checked line(s) fit. Best first:\n")
        for i, (_, name, l, need, _, sit, viol) in enumerate(shown):
            tag = f"; written for {l['from_deck']}, re-checked: PASS in {deck}" if l.get("from_deck") else ""
            print(f"=== {i+1}. {name}  [{l['status'].upper()}{tag}]")
            print("    uses from hand: " + ", ".join(f"{k}" + (f" x{v}" if v > 1 else "") for k, v in need.items()))
            if sit:
                print("    CHECK SITUATION: " + "; ".join(sit))
            if viol:
                print("    !! THIS LINE CURRENTLY FAILS THE CHECKER: " + "; ".join(viol))
            if i == 0 or "--all" in flags:
                print_line(name, l, header=False)
            print()
        if len(fits) > 1 and "--all" not in flags:
            print("(only the best line is printed in full: ./quick show NAME for another, or --all)")
    else:
        print("\nNO CHECKED LINE FITS THIS HAND. Don't improvise a long line: write one in CUE and run ./quick check, "
              "or give the shortest safe play and say it's unchecked.")
    if other_report:
        print("\nOther deck's lines that fit the hand but break here:")
        print("\n".join(other_report))
    if near and (not fits or "--all" in flags):
        print("\nClosest lines (missing cards):")
        for _, name, l, need, miss, sit, _ in near[:4]:
            print(f"  - {name} [{l['status']}]  missing: " + ", ".join(f"{k}" + (f" x{v}" if v > 1 else "") for k, v in miss.items()))


def cmd_show(argv):
    q = " ".join(argv).lower()
    lines = export_lines()
    hits = [k for k in lines if q in k.lower()]
    if not hits:
        die("No line matches. Lines:\n  " + "\n  ".join(lines))
    for k in hits[:3]:
        print_line(k, lines[k]); print()


def cmd_check(argv):
    if not argv:
        die("usage: ./quick check FILE.cue   (or - to read stdin)")
    text = sys.stdin.read() if argv[0] == "-" else open(argv[0]).read()
    text = re.sub(r"^\s*package\s+\w+\s*$", "", text, flags=re.M).strip()
    if not re.match(r"^\s*(//.*\n\s*)*lines\s*:", text):
        if text.startswith("{"):
            text = 'lines: "PASTED LINE": ' + text
        else:
            text = 'lines: "PASTED LINE": {\n' + text + "\n}"
    names = re.findall(r'lines\s*:\s*"([^"]+)"', text)
    tmp = tempfile.mkdtemp(prefix="quickcheck-")
    for f in ("schema.cue", "cards.cue", "decks.cue"):
        shutil.copy(os.path.join(LC, f), tmp)
    open(os.path.join(tmp, "pasted.cue"), "w").write("package lines\n\n" + text + "\n")
    # Unknown card names: the most common slip. Say which, with the closest real name.
    pool = known_names()
    checker_cards = set(re.findall(r'^\s*"((?:[^"\\]|\\.)+)":\s*\{', open(os.path.join(LC, "cards.cue")).read(), re.M))
    bad_names = []
    for m in re.finditer(r'(card|summons)\s*:\s*"([^"]+)"', text):
        n = base(m.group(2))
        if n not in checker_cards:
            close = difflib.get_close_matches(n, sorted(checker_cards), n=1, cutoff=0.4)
            bad_names.append(f"'{n}' isn't in cards.cue" + (f" (did you mean '{close[0]}'?)" if close else " (add it to cards.cue)"))
    r = subprocess.run([cue_bin(), "export", ".", "-e", "lines", "--out", "json"], cwd=tmp, capture_output=True, text=True)
    if r.returncode:
        print("DOESN'T LOAD (fix the syntax or field names first):")
        print(clean_cue_err(r.stderr).replace(tmp + "/", ""))
        for b in bad_names:
            print("NAME: " + b)
        sys.exit(1)
    lines = json.loads(r.stdout)
    bad = 0
    for n in names or list(lines):
        l = lines[n]
        v = l.get("violations", [])
        ok = (not v) if l["status"] != "known_bad" else bool(v)
        bad += not ok
        print(("PASS" if ok and not bad_names else "FAIL") + f" [{l['status']}] {n}")
        for b in bad_names:
            print("   - NAME: " + b)
        for x in v:
            print("   - " + x)
        print("\nReady to send:" if ok and not bad_names else "\nSteps as written (DON'T SEND until it passes):")
        print_line(n, {**l, "violations": []}, header=False)
    shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if bad or bad_names else 0)


def cmd_card(argv):
    import cardtext
    for a in split_cards(argv) if argv else []:
        n, err = resolve(a)
        if err and "ambiguous" in err:
            print(f"## {a}\n{err}\n"); continue
        if err:
            n = a  # not a known card: let cardtext try the network
        data = cardtext.lookup(n)
        if not data:
            print(f"## {a}\nNOT FOUND" + (f" ({err})" if err else "") + "\n")
        for c in data[:1]:
            cardtext.show(c)


def all_card_names():
    names = set(re.findall(r'^\s*"((?:[^"\\]|\\.)+)":\s*[{0-9]', open(os.path.join(LC, "cards.cue")).read() + open(os.path.join(LC, "decks.cue")).read(), re.M))
    names = {n.replace('\\"', '"') for n in names} - {"PredaRikka", "RikkaM1"}
    opp = os.path.join(HERE, "opponents.txt")
    names |= {l.strip() for l in open(opp) if l.strip() and not l.startswith("#")}
    return sorted(names)


def cmd_precache(argv):
    import cardtext
    missing = []
    for n in all_card_names():
        path = os.path.join(cardtext.CACHE, "".join(c if c.isalnum() else "_" for c in n) + ".json")
        if os.path.exists(path):
            continue
        try:
            data = cardtext.lookup(n)
        except Exception as e:  # network
            data = []
            print(f"  ? {n}: {e}")
        print(("  + " if data else "  - NOT FOUND: ") + n)
        if not data:
            missing.append(n)
    total = len(all_card_names())
    print(f"cache: {total - len(missing)}/{total} cards" + (f"; not found: {', '.join(missing)}" if missing else ""))


def cmd_names(argv):
    w = max(map(len, ALIASES))
    for k, v in sorted(ALIASES.items()):
        print(f"  {k:<{w}}  {v}")
    print("\nAny unique part of a card name also works (e.g. 'thirsting', 'ambulo'). '2x ash' or 'ash x2' for copies.")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        sys.exit(__doc__)
    cmd, argv = sys.argv[1], sys.argv[2:]
    cmds = {"find": cmd_find, "check": cmd_check, "show": cmd_show, "card": cmd_card, "cards": cmd_card,
            "precache": cmd_precache, "names": cmd_names}
    if cmd not in cmds:
        sys.exit(__doc__)
    cmds[cmd](argv)


if __name__ == "__main__":
    main()
