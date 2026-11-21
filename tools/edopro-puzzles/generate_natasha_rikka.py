"""EDOPro puzzles: PredaRikka (vs-Natasha build) against Natasha's Horus Dragoon deck.
Going 2nd: 10 random hands into her end board. Going 1st: 5 drill hands (proven starters) with her
real opening hand waiting. Card IDs come from YGOPRODeck (cached in ids_rikka.json)."""
import json, os, random, urllib.request, urllib.parse, zipfile, glob
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "v4")
os.makedirs(OUT, exist_ok=True)
MAIN = {"Rikka Petal":1,"Predaplant Byblisp":1,"Predaplant Longinephila":2,"Princess Dracaena, the Thirsting Tree":3,
 'Maxx "C"':1,"Ash Blossom & Joyous Spring":3,"Predaplant Lilizard":1,"Rikka Princess":1,"Mulcharmy Fuwalos":2,
 "Mudan the Rikka Fairy":2,"Rikka Black Princess":3,"Hellebore the Rikka Fairy":1,"Primrose the Rikka Fairy Duo":1,
 "Instant Fusion":1,"Rikka Glamour":3,"Triple Tactics Talent":1,"Predaprimitive":3,"Rikka Moonlit Waters":3,
 "Rikka Konkon":1,"Super Polymerization":2,"Evenly Matched":1,"Rikka Sheet":1,"Dominus Impulse":3,
 "Droll & Lock Bird":2,"Cactus Bouncer":1,"Forbidden Droplet":1}
EXTRA = ["Predaplant Ambulomelides","Predaplant Daredevil","Garura, Wings of Resonant Life","Starving Venom Fusion Dragon",
 "Secreterion Dragon","Predaplant Bal Teah","Rikka Queen Strenna","Kanzashi the Rikka Queen","Rikka Sacred Queen Strenna",
 "Orea, the Sylvan High Arbiter","Teardrop the Rikka Queen","Teardrop the Rikka Queen","Sacred Tree Beast, Hyperyton",
 "Teardrop the Rikka Sacred Queen","Aromaseraphy Jasmine"]
HER_DECK = {"Dark Magician":1,"Droll & Lock Bird":2,'Maxx "C"':1,"Ash Blossom & Joyous Spring":2,"Ghost Mourner & Moonlit Chill":1,
 "Planet Pathfinder":3,"Silent Magician Zero":1,"Gadget Trio":1,"Dark Magician Girl the Magician's Apprentice":2,
 "Dark Magician the Magician of Black Magic":1,"Imsety, Glory of Horus":3,"Duamutef, Blessing of Horus":1,
 "Qebehsenuef, Protection of Horus":1,"Hapi, Guidance of Horus":1,"Horus the Black Flame Deity":1,"Dark Hole":1,
 "Dark Magical Curtain":1,"Triple Tactics Talent":1,"Triple Tactics Thrust":1,"Walls of the Imperial Tomb":3,
 "King's Sarcophagus":3,"Shining Sarcophagus":2,"Forbidden Droplet":1,"Future Silence":3,"The Gaze of Timaeus":2}
HER_EXTRA = ["Red-Eyes Dark Dragoon"]*3+["Dark Magician of Destruction"]*2
IDS_FILE = os.path.join(HERE, "ids_rikka.json")
ids = json.load(open(IDS_FILE)) if os.path.exists(IDS_FILE) else {}
for n in set(MAIN)|set(EXTRA)|set(HER_DECK)|set(HER_EXTRA):
    if n not in ids:
        u = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=" + urllib.parse.quote(n)
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        ids[n] = json.load(urllib.request.urlopen(req))["data"][0]["id"]
json.dump(ids, open(IDS_FILE, "w"), indent=1, sort_keys=True)

def add(n, p, loc, seq=0, pos="POS_FACEDOWN", proc=False):
    return f'Debug.AddCard({ids[n]},{p},{p},{loc},{seq},{pos}{",true" if proc else ""}) --{n}'
def header(msg):
    return [f"--[[message\n{msg}\n]]", 'Debug.SetAIName("Natasha (Horus Dragoon)")',
            "Debug.ReloadFieldBegin(DUEL_ATTACK_FIRST_TURN+DUEL_SIMPLE_AI,5)",
            "Debug.SetPlayerInfo(0,8000,0,0)", "Debug.SetPlayerInfo(1,8000,0,0)"]
def my_cards(hand, used=()):
    pool = [n for n, c in MAIN.items() for _ in range(c)]
    for h in list(hand) + list(used): pool.remove(h)
    random.Random(len(pool) + len(hand)).shuffle(pool)
    return (["--Your hand"] + [add(h, 0, "LOCATION_HAND") for h in hand] +
            ["--Your Main Deck"] + [add(n, 0, "LOCATION_DECK") for n in pool] +
            ["--Your Extra Deck"] + [add(n, 0, "LOCATION_EXTRA") for n in EXTRA])
def her_cards(hand, field_used):
    pool = [n for n, c in HER_DECK.items() for _ in range(c)]
    for h in hand + field_used: pool.remove(h)
    random.Random(7).shuffle(pool)
    return (["--Her hand"] + [add(h, 1, "LOCATION_HAND") for h in hand] +
            ["--Her Deck"] + [add(n, 1, "LOCATION_DECK") for n in pool] +
            ["--Her Extra Deck"] + [add(n, 1, "LOCATION_EXTRA") for n in HER_EXTRA])
files = []

# ---- Going 1st drills: proven starter + filler; her real opening hand waits for her turn ----
HER_HAND = ["Imsety, Glory of Horus","Walls of the Imperial Tomb","Dark Hole","Forbidden Droplet","Ash Blossom & Joyous Spring"]
DRILLS = [
 ("1_Predaprimitive", ["Predaprimitive","Ash Blossom & Joyous Spring","Droll & Lock Bird","Dominus Impulse","Evenly Matched"],
  "Predaprimitive -> Byblisp to GY, add Instant Fusion; Byblisp adds Lilizard; Instant Fusion -> Ambulomelides (adds Longinephila); Lilizard SS; Ambulomelides tributes itself -> Longinephila (adds a Predap); Longinephila+Lilizard -> Bal Teah (revives Lilizard, draw 1); banish Longinephila: counter; Byblisp revives; Bal Teah+Lilizard -> Jasmine; Jasmine tributes Byblisp -> Petal; Petal sends Black Princess; Black Princess from GY, tributes Jasmine -> Mudan (adds Konkon); Konkon sets Glamour; Mudan+Black Princess -> Sacred Queen Strenna -> Kanzashi (+Primrose attached); Glamour tributing a spare Plant: Rikka Princess + Cactus Bouncer; Kanzashi revives Bal Teah, Strenna sets Sheet; Rikka Princess SS; Rikka Princess+Bal Teah -> Rikka Queen Strenna (detach: add Primrose); Normal Summon Cactus Bouncer."),
 ("2_InstantFusion", ["Instant Fusion",'Maxx "C"',"Ash Blossom & Joyous Spring","Forbidden Droplet","Dominus Impulse"],
  "Instant Fusion -> Ambulomelides (adds Predaprimitive); Predaprimitive sends Byblisp, adds Super Poly; Byblisp adds Lilizard; then the same as drill 1 from 'Lilizard SS'."),
 ("3_MoonlitWaters_LineA", ["Rikka Moonlit Waters","Ash Blossom & Joyous Spring","Droll & Lock Bird","Mulcharmy Fuwalos","Dominus Impulse"],
  "Line A: Moonlit (no Tribute) adds Mudan, sends Black Princess; Black Princess from GY, tributes herself -> Petal; Petal adds Primrose; Mudan tributes Petal (Mudan adds Konkon; Primrose -> Primrose + Hellebore); Konkon sets Glamour; Primrose: Hellebore -2; Mudan+Hellebore -> Sacred Queen Strenna -> Rikka Queen Strenna (+Rikka Princess); Hellebore from GY tributes Rikka Queen Strenna (Hyperyton; Sheet); Glamour tributing Sacred Queen Strenna, CHAIN Hyperyton attaching Moonlit Waters; add Rikka Princess + Cactus; SS Rikka Princess; Normal Summon Cactus."),
 ("4_BlackPrincess_Plant_LineB", ["Rikka Black Princess","Princess Dracaena, the Thirsting Tree","Ash Blossom & Joyous Spring","Droll & Lock Bird","Dominus Impulse"],
  "Line B: SS Black Princess; she tributes Dracaena from hand -> Mudan (adds Konkon); Konkon sets Glamour; Mudan+Black Princess -> Sacred Queen Strenna -> Rikka Queen Strenna (+Rikka Princess); Glamour tributing Rikka Queen Strenna: Rikka Princess + Cactus (Hyperyton; Sheet); SS Rikka Princess, chain Hyperyton attaching Mudan; Normal Summon Cactus."),
 ("5_Glamour_Petal", ["Rikka Glamour",'Maxx "C"',"Ash Blossom & Joyous Spring","Forbidden Droplet","Dominus Impulse"],
  "Glamour (no Tribute) adds Petal, then Line 1 on the Rikka page (Petal -> Black Princess -> Mudan -> Konkon -> Sacred Queen Strenna -> Rikka Queen Strenna -> Moonlit Primrose/Hellebore -> Hyperyton + Sheet -> Teardrop). Pick the Kanzashi finish."),
]
for name, hand, steps in DRILLS:
    msg = (f"PredaRikka vs Natasha, GOING FIRST drill {name}.\nYour hand: {', '.join(hand)}.\n"
           f"Target: Cactus Bouncer + Kanzashi or a Spell-material Hyperyton, set Rikka Sheet, Rikka Princess in the GY.\n"
           f"Proven line (Yusodus, MDM): {steps}\n"
           f"Her hand: {', '.join(HER_HAND)} (+1 draw). Win = she can't break your board and you win the duel.")
    L = header(msg) + my_cards(hand) + her_cards(HER_HAND, []) + ["", "Debug.ReloadFieldEnd()", 'Debug.ShowHint("Build the board, then survive her turn.")']
    f = os.path.join(OUT, f"Natasha_PredaRikka_1st_{name}.lua"); open(f, "w").write("\n".join(L) + "\n"); files.append(f)

# ---- Going 2nd: 10 random hands into her end board ----
HT = ["Ash Blossom & Joyous Spring","Droll & Lock Bird",'Maxx "C"',"Mulcharmy Fuwalos","Dominus Impulse"]
PIECES = [("Dragoon", add("Red-Eyes Dark Dragoon",1,"LOCATION_MZONE",5,"POS_FACEUP_ATTACK",True), "Red-Eyes Dark Dragoon"),
          ("Shining Sarcophagus", add("Shining Sarcophagus",1,"LOCATION_SZONE",1,"POS_FACEUP"), "Shining Sarcophagus"),
          ("Hapi", add("Hapi, Guidance of Horus",1,"LOCATION_MZONE",3,"POS_FACEUP_ATTACK",True), "Hapi, Guidance of Horus"),
          ("Duamutef", add("Duamutef, Blessing of Horus",1,"LOCATION_MZONE",1,"POS_FACEUP_ATTACK",True), "Duamutef, Blessing of Horus"),
          ("Qebehsenuef", add("Qebehsenuef, Protection of Horus",1,"LOCATION_MZONE",2,"POS_FACEUP_ATTACK",True), "Qebehsenuef, Protection of Horus")]
FIXED = [add("Imsety, Glory of Horus",1,"LOCATION_MZONE",0,"POS_FACEUP_ATTACK",True),
         add("King's Sarcophagus",1,"LOCATION_SZONE",0,"POS_FACEUP"),
         add("Future Silence",1,"LOCATION_SZONE",2,"POS_FACEDOWN"),
         add("Walls of the Imperial Tomb",1,"LOCATION_FZONE",0,"POS_FACEUP")]
FIXED_NAMES = ["Imsety, Glory of Horus","King's Sarcophagus","Future Silence","Walls of the Imperial Tomb"]
pool = [n for n, c in MAIN.items() for _ in range(c)]
rng = random.Random(20261121)
for i in range(1, 11):
    p = pool[:]; rng.shuffle(p); hand0 = p[:5]
    used = [h for h in hand0 if h in HT][:len(PIECES)]
    hand = list(hand0)
    for u in used: hand.remove(u)
    gone = [n for n, _, _ in PIECES[:len(used)]]
    keep = PIECES[len(used):]
    msg = (f"PredaRikka vs Natasha, GOING SECOND, random hand {i}/10.\nOpening hand: {', '.join(hand0)} (+1 draw).\n"
           f"Hand traps used on her turn: {', '.join(used) or 'none'} -> she lost: {', '.join(gone) or 'nothing'}.\n"
           "Plan: Droplet first (send a monster), remove with Tributes, answer Horus the Black Flame Deity with Rikka Princess or Dominus, "
           "Super Poly Dragoon + your DARK Predaplant, Evenly Matched after battle. Win within 2 of your turns.")
    her_field = [c[2] for c in keep] + FIXED_NAMES
    L = (header(msg) + my_cards(hand, used) + ["--Your hand traps already used on her turn"] +
         [add(u, 0, "LOCATION_GRAVE", 0, "POS_FACEUP") for u in used] + ["--Her board"] + [c[1] for c in keep] + FIXED +
         her_cards(["Horus the Black Flame Deity","Ash Blossom & Joyous Spring","Droll & Lock Bird","Dark Magician"],
                   [n for n in her_field if n in HER_DECK]) +
         ["", "Debug.ReloadFieldEnd()", 'Debug.ShowHint("Win within 2 of your turns.")'])
    f = os.path.join(OUT, f"Natasha_PredaRikka_2nd_hand{i:02d}.lua"); open(f, "w").write("\n".join(L) + "\n"); files.append(f)
    print(i, hand0, "used:", used)
z = zipfile.ZipFile(os.path.join(HERE, "Natasha_PredaRikka_puzzles_v4.zip"), "w")
for f in sorted(files): z.write(f, os.path.basename(f))
z.close(); print(len(files), "files")
