import re, html
from playwright.sync_api import sync_playwright

import os, sys
VERSION = "1.1"
DATE = "14 Nov 2026"
# Run from repo root: python3 tools/invoked-cheatsheet/build.py
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Writerside", "images", "invoked-cheatsheet", "v" + VERSION)

def fmt(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = s.replace("→", '<span class="arr">→</span>')
    return s

LINES = [
 dict(id="1", title="Aleister + FIRE/WIND", tag="Sourced: Taffy (MDM)",
  needs=["Aleister", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "+1 spare card"],
  stages=[
   ("Get Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath (+1000)",
    "Sorath: revive Aleister"]),
   ("Crowley into Baybarron", [
    "Link Aleister + Artemis → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (it summons itself)",
    "Crowley: Crowley + Endymion → **Baybarron**",
    "Baybarron: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Sword**"]),
   ("Finish", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Aleister → **Mechaba**",
    "Madness: discard spare → search **Invocation**",
    "Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Mechaba · Virakam · set Sword"),

 dict(id="2", title="Aleister + any card", tag="Sourced: Taffy (MDM) · weakest line",
  needs=["Aleister", "+1 spare card"],
  stages=[
   ("Get Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Almiraj**",
    "Invocation: Aleister + Almiraj → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath",
    "Sorath: revive Aleister"]),
   ("Finish", [
    "Link Aleister + Sorath → **Madness**",
    "Sorath GY: Sorath + Aleister → **Baybarron**",
    "Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**, skip banish)",
    "Special Summon Virakam → set **Sword**",
    "Link Virakam + Baybarron → **Little Knight**",
    "Invocation: Madness + Virakam → **Mechaba**"]),
  ],
  end="Little Knight · Mechaba · set Sword"),

 dict(id="3", title="Reminiscent alone", tag="Sourced: Taffy (MDM)",
  needs=["Reminiscent", "+1 spare card"],
  stages=[
   ("Raidjin loop into Sorath", [
    "Normal Summon Reminiscent: banish **Raidjin** (Extra Deck) → search **Sword**",
    "Sword: Reminiscent + Raidjin (banished) → **Sorath**",
    "Sorath: revive Reminiscent",
    "Link Reminiscent → **Artemis**",
    "Sword GY: add Reminiscent to hand",
    "Reminiscent (hand): target Sorath → Special Summon itself"]),
   ("Crowley into Baybarron", [
    "Link Artemis + Reminiscent → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (it summons itself)",
    "Crowley: Crowley + Endymion → **Baybarron**",
    "Baybarron: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Sword**"]),
   ("Aeon finish", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)",
    "Link Aeon + Virakam → **Little Knight**",
    "Invocation: Madness + Aeon (GY) → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Little Knight · set Sword · up to 6 of hers banished"),

 dict(id="4", title="Aleister + Reminiscent", tag="Sourced: Taffy (MDM), Baronne branch · BEST LINE",
  needs=["Aleister (or Meltdown / Aiwass / Sacred Spirit Sword)", "Reminiscent", "+1 spare card"],
  stages=[
   ("1 · Two Links into Crowley", [
    "Normal Summon Aleister → search **Invocation**",
    "Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Sword**",
    "Link Aleister → **Artemis**",
    "Link Artemis + Reminiscent → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (summons itself). DON'T FUSE"]),
   ("2 · Chorozo, Baybarron, Sorath", [
    "Endymion + Artemis → **Chorozo** (contact fusion)",
    "Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish",
    "Special Summon Virakam → set **Sword**",
    "Sword (hand): Aleister + Raidjin (banished) → **Sorath**"]),
   ("3 · Baronne and Madness", [
    "Link Baybarron + Crowley → **Madness**",
    "Sorath: revive Crowley",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**"]),
   ("4 · Aeon finish", [
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)",
    "Link Aeon + Crowley → **Little Knight**",
    "Sword GY: add Invocation",
    "Invocation: Aleister + Endymion (GY) → **Mechaba**",
    "Invocation: Madness + Crowley → **Oceanus** (Extra Monster Zone)",
    "Invocation GY: add a banished Aleister"]),
  ],
  end="Baronne · Mechaba · Oceanus (EMZ) · Little Knight · Virakam · set Sword · Aleister in hand · up to 6 of hers banished",
  memo="Raidjin used 3× (cost → Sword → Aeon). Crowley used 3× (Madness → Little Knight → Oceanus)."),

 dict(id="5", title="Crowley or Spenta + Reminiscent + FIRE/WIND", tag="Sourced: Taffy (MDM)",
  needs=["Crowley (Normal Summon) or Spenta (discard → Crowley)", "Reminiscent", "FIRE/WIND monster", "+1 spare card"],
  stages=[
   ("Sorath and Madness", [
    "Crowley: Crowley + FIRE/WIND (hand) → **Sorath**",
    "Sorath: revive Crowley",
    "Reminiscent: target Sorath, summon itself; banish **Raidjin** → search **Sword**",
    "Link Reminiscent + Sorath → **Madness**",
    "Sorath GY: Reminiscent + Sorath → **Baybarron**",
    "Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**)"]),
   ("Aeon finish", [
    "Link Baybarron + Crowley → **Little Knight**: banish Baybarron from your GY",
    "Special Summon Virakam → set **Sword**",
    "Sword: Baybarron + Sorath + Raidjin (banished) → **Aeon**",
    "Aeon: banish up to 3 of hers, then pick 3 from her Extra Deck",
    "Sword GY: add Invocation",
    "Invocation: Crowley + Madness → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Little Knight · Aeon · Virakam · set Sword",
  memo="Taffy makes Elysium after Aeon. Add that step once you own Elysium."),

 dict(id="6", title="Sacred Spirit Sword opener", tag="Sourced: Dawnstar (MDM)",
  needs=["Sacred Spirit Sword (or Meltdown / Aiwass)"],
  stages=[
   ("Open", [
    "Sacred Spirit Sword: summon **Aiwass** from Deck (only Fusions attack this turn)",
    "Aiwass: banish it → search **Aleister** → Normal Summon it straight away",
    "Aleister → search **Invocation**"]),
   ("Then continue", [
    "Reminiscent in hand → **Line 4** from step 2",
    "FIRE/WIND in hand → **Line 1** from step 2",
    "Anything else → **Line 2** from step 2"]),
  ],
  end="Same board as the line you continue into",
  memo="Meltdown or Aiwass from hand open the same way but use your own Normal Summon."),

 dict(id="7", title="Zoroa or Spenta, no Aleister", tag="UNTESTED · built from card text",
  needs=["Zoroa, or Spenta (discard → Zoroa)"],
  stages=[
   ("Line", [
    "Spenta (if held): discard → search **Zoroa**",
    "Normal Summon Zoroa",
    "Zoroa: target itself, equip **Artemis** from Extra Deck",
    "Zoroa: Special Summon a Level 4 Spellcaster from hand/GY (Spenta)",
    "Artemis: search **Crowley** (it summons itself)",
    "Crowley + Zoroa (FIRE) → **Sorath**, or Crowley + Spenta (LIGHT) → **Mechaba**"]),
  ],
  end="1 Fusion + a spare body. Turns a brick into a board."),

 dict(id="8", title="Going 2nd into Natasha's Dragoon", tag="Built from card text · practise it",
  needs=["Aleister route", "Super Polymerization", "Imperm (ideal)"],
  stages=[
   ("Her turn", [
    "**Imperm Imsety** (stops her send-to-GY punish)"]),
   ("Your turn", [
    "**Meltdown** → Aleister (bait Dragoon's negate here)",
    "Normal Summon Aleister → search **Invocation**",
    "**Super Poly**: Aleister + Dragoon → **Oceanus** (she can't respond)",
    "Invocation: Dragoon (her GY) + Oceanus → **Aeon**",
    "Aeon: banish **King's Sarcophagus** + her best Horus",
    "Attack"]),
  ],
  end="Dragoon gone · Sarcophagus gone · Aeon 3800 on board",
  memo="Can't hit Timaeus the turn it lands. Ghost Ogre can't touch Shining Sarcophagus. Elysium (when crafted) banishes ALL her DARK monsters."),
]

INDEX = [
 ("Aleister + Reminiscent", "4", True),
 ("Meltdown / Sacred Spirit Sword / Aiwass + Reminiscent", "6→4", True),
 ("Reminiscent alone", "3", False),
 ("Crowley or Spenta + Reminiscent + FIRE/WIND", "5", False),
 ("Aleister + Ash / Droll / Fuwalos / Zoroa", "1", False),
 ("Aleister + any card", "2", False),
 ("Sacred Spirit Sword / Meltdown / Aiwass", "6", False),
 ("Zoroa or Spenta, no Aleister", "7", False),
 ("Going 2nd into Dragoon", "8", False),
]
RULES = [
 "Baybarron: say SKIP to the banish unless you've picked a target",
 "Madness needs a spare card to discard. Keep one",
 "Oceanus goes in the Extra Monster Zone",
 "Before any Link: is there a free zone?",
 "Read both GYs + banishment before Invocation",
 "Discard order: dead copies (2nd Meltdown, used Sword) → Fuwalos → Imperm → Crossout → Ghost Belle. KEEP Maxx C, Ash, Super Poly, Droll, Nibiru",
 "Mechaba: keep 1 monster + 1 Spell/Trap in hand if you can",
]

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#0e1220;font-family:Inter,'DejaVu Sans',sans-serif;color:#e8ecf5;width:720px}
.card{padding:28px 30px 26px;background:linear-gradient(180deg,#151b2e 0%,#0e1220 100%)}
.top{display:flex;align-items:center;gap:16px;margin-bottom:6px}
.num{flex:none;width:58px;height:58px;border-radius:14px;background:#d9a441;color:#1a1306;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center}
h1{font-size:27px;font-weight:800;line-height:1.15;letter-spacing:-.2px}
.tag{font-size:13px;color:#9aa6c4;margin:4px 0 16px;text-transform:uppercase;letter-spacing:.6px;font-weight:600}
.tag.warn{color:#f0a35e}
.needs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}
.chip{background:#23304f;border:1px solid #34446b;color:#cfe0ff;border-radius:999px;padding:6px 13px;font-size:15px;font-weight:600}
.stage{margin-bottom:14px;background:#151d33;border:1px solid #243154;border-radius:14px;padding:12px 16px 8px}
.sh{font-size:13px;font-weight:800;color:#d9a441;text-transform:uppercase;letter-spacing:.8px;margin-bottom:6px}
ol{list-style:none}
li{display:flex;gap:12px;padding:7px 0;border-top:1px solid #1f2a47;font-size:18px;line-height:1.35}
li:first-child{border-top:none}
.n{flex:none;width:28px;height:28px;border-radius:8px;background:#2b3a62;color:#fff;font-weight:700;font-size:15px;display:flex;align-items:center;justify-content:center;margin-top:1px}
b{color:#ffd77a;font-weight:700}
.arr{color:#7fb4ff;font-weight:700}
.end{margin-top:6px;background:#1d2f25;border:1px solid #2f5a40;border-radius:14px;padding:12px 16px;font-size:17px;line-height:1.4}
.end .k,.memo .k{font-size:12px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:#7fd39a;display:block;margin-bottom:3px}
.memo{margin-top:10px;background:#2a2238;border:1px solid #4a3a66;border-radius:14px;padding:12px 16px;font-size:16px;line-height:1.4}
.memo .k{color:#c9a8ff}
.foot{margin-top:14px;font-size:12px;color:#6c7899;text-align:right}
table{width:100%;border-collapse:separate;border-spacing:0 8px}
td{background:#151d33;border-top:1px solid #243154;border-bottom:1px solid #243154;padding:12px 14px;font-size:18px}
td:first-child{border-left:1px solid #243154;border-radius:12px 0 0 12px}
td:last-child{border-right:1px solid #243154;border-radius:0 12px 12px 0;width:110px;text-align:center;font-weight:800;color:#1a1306}
.pill{display:inline-block;background:#d9a441;border-radius:10px;padding:4px 12px;font-size:18px}
tr.best td{background:#2a2410;border-color:#6b5520}
.rules li{font-size:17px}
"""

def page(body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='card' id='c'>{body}</div></body></html>"

def line_html(L):
    warn = "warn" if "UNTESTED" in L["tag"] else ""
    h = f"<div class='top'><div class='num'>{L['id']}</div><h1>{fmt(L['title'])}</h1></div>"
    h += f"<div class='tag {warn}'>{fmt(L['tag'])}</div>"
    h += "<div class='needs'>" + "".join(f"<span class='chip'>{fmt(n)}</span>" for n in L["needs"]) + "</div>"
    i = 1
    for name, steps in L["stages"]:
        h += f"<div class='stage'><div class='sh'>{fmt(name)}</div><ol>"
        for s in steps:
            h += f"<li><span class='n'>{i}</span><span>{fmt(s)}</span></li>"; i += 1
        h += "</ol></div>"
    h += f"<div class='end'><span class='k'>End board</span>{fmt(L['end'])}</div>"
    if L.get("memo"):
        h += f"<div class='memo'><span class='k'>Remember</span>{fmt(L['memo'])}</div>"
    h += f"<div class='foot'>Invoked cheat sheet · v{VERSION} · {DATE}</div>"
    return page(h)

def index_html():
    h = "<div class='top'><div class='num'>?</div><h1>Which line? Read your hand</h1></div>"
    h += "<div class='tag'>Top row wins if more than one fits</div><table>"
    for hand, line, best in INDEX:
        h += f"<tr class='{'best' if best else ''}'><td>{fmt(hand)}</td><td><span class='pill'>Line {line}</span></td></tr>"
    h += "</table><div class='stage rules' style='margin-top:10px'><div class='sh'>Golden rules</div><ol>"
    for i, r in enumerate(RULES, 1):
        h += f"<li><span class='n'>{i}</span><span>{fmt(r)}</span></li>"
    h += "</ol></div>"
    h += f"<div class='foot'>Invoked cheat sheet · v{VERSION} · {DATE}</div>"
    return page(h)

import os
os.makedirs(OUT, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 720, "height": 800}, device_scale_factor=2)
    jobs = [("invoked-0-which-line", index_html())] + [(f"invoked-line-{L['id']}", line_html(L)) for L in LINES]
    for name, doc in jobs:
        pg.set_content(doc)
        pg.locator("#c").screenshot(path=f"{OUT}/{name}.png")
        print(name)
    b.close()
