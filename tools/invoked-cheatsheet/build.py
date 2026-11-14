import re, html
from playwright.sync_api import sync_playwright

import os, sys
VERSION = "1.14"
DATE = "14 Nov 2026"
# Run from repo root: python3 tools/invoked-cheatsheet/build.py
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Writerside", "images", "invoked-cheatsheet", "v" + VERSION)

def fmt(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = s.replace("→", '<span class="arr">→</span>')
    return s

LINES = [
 dict(id="5", title="Aleister + FIRE/WIND", tag="Sourced: Taffy (MDM)",
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
    "Special Summon Virakam → set **Invoke Sword**"]),
   ("Finish", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Aleister → **Mechaba**",
    "Madness: discard spare → search **Invocation**",
    "Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Mechaba · Virakam · set Invoke Sword",
  memo="Going 2nd with a 2nd Invoke Sword in hand? Don't discard it at step 15: see Line 13 for the finishers."),

 dict(id="6", title="Aleister + any card", tag="Sourced: Taffy (MDM) · weakest line",
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
    "Special Summon Virakam → set **Invoke Sword**",
    "Link Virakam + Baybarron → **Little Knight**",
    "Invocation: Madness + Virakam → **Mechaba**"]),
  ],
  end="Little Knight · Mechaba · set Invoke Sword"),

 dict(id="3", title="Reminiscent alone", tag="Sourced: Taffy (MDM)",
  needs=["Reminiscent", "+1 spare card"],
  stages=[
   ("Raidjin loop into Sorath", [
    "Normal Summon Reminiscent: banish **Raidjin** (Extra Deck) → search **Invoke Sword**",
    "Invoke Sword: Reminiscent + Raidjin (banished) → **Sorath**",
    "Sorath: revive Reminiscent",
    "Link Reminiscent → **Artemis**",
    "Invoke Sword GY: add Reminiscent to hand",
    "Reminiscent (hand): target Sorath → Special Summon itself"]),
   ("Crowley into Baybarron", [
    "Link Artemis + Reminiscent → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (it summons itself)",
    "Crowley: Crowley + Endymion → **Baybarron**",
    "Baybarron: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Invoke Sword**"]),
   ("Aeon finish", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)",
    "Link Aeon + Virakam → **Little Knight**",
    "Invocation: Madness + Aeon (GY) → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Little Knight · set Invoke Sword · up to 6 of hers banished"),

 dict(id="1", title="Aleister + Reminiscent", tag="Sourced: Taffy (MDM), Baronne branch · BEST LINE",
  needs=["Aleister (or Meltdown / Aiwass / Sacred Sword)", "Reminiscent", "+1 spare card"],
  stages=[
   ("1 · Two Links into Crowley", [
    "Normal Summon Aleister → search **Invocation**",
    "Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**",
    "Link Aleister → **Artemis**",
    "Link Artemis + Reminiscent → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (summons itself). DON'T FUSE"]),
   ("2 · Chorozo, Baybarron, Sorath", [
    "Endymion + Artemis → **Chorozo** (contact fusion)",
    "Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish",
    "Special Summon Virakam → set **Invoke Sword**",
    "Invoke Sword (hand): Aleister + Raidjin (banished) → **Sorath**"]),
   ("3 · Baronne and Madness", [
    "Link Baybarron + Crowley → **Madness**",
    "Sorath: revive Crowley",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**"]),
   ("4 · Aeon finish", [
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)",
    "Link Aeon + Crowley → **Little Knight**",
    "Invoke Sword GY: add Invocation",
    "Invocation: Aleister + Endymion (GY) → **Mechaba**",
    "Invocation: Madness + Crowley → **Oceanus** (Extra Monster Zone)",
    "Invocation GY: add a banished Aleister"]),
  ],
  end="Baronne · Mechaba · Oceanus (EMZ) · Little Knight · Virakam · set Invoke Sword · Aleister in hand · up to 6 of hers banished",
  memo="Raidjin used 3× (cost → Invoke Sword → Aeon). Crowley used 3× (Madness → Little Knight → Oceanus)."),

 dict(id="4", title="Crowley or Spenta + Reminiscent + FIRE/WIND", tag="Sourced: Taffy (MDM)",
  needs=["Crowley (Normal Summon) or Spenta (discard → Crowley)", "Reminiscent", "FIRE/WIND monster", "+1 spare card"],
  stages=[
   ("Sorath and Madness", [
    "Crowley: Crowley + FIRE/WIND (hand) → **Sorath**",
    "Sorath: revive Crowley",
    "Reminiscent: target Sorath, summon itself; banish **Raidjin** → search **Invoke Sword**",
    "Link Reminiscent + Sorath → **Madness**",
    "Sorath GY: Reminiscent + Sorath → **Baybarron**",
    "Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**)"]),
   ("Aeon finish", [
    "Link Baybarron + Crowley → **Little Knight**: banish Baybarron from your GY",
    "Special Summon Virakam → set **Invoke Sword**",
    "Invoke Sword: Baybarron + Sorath + Raidjin (banished) → **Aeon**",
    "Aeon: banish up to 3 of hers, then pick 3 from her Extra Deck",
    "Invoke Sword GY: add Invocation",
    "Invocation: Crowley + Madness → **Oceanus** (Extra Monster Zone)"]),
  ],
  end="Oceanus (EMZ) · Little Knight · Aeon · Virakam · set Invoke Sword",
  memo="Taffy makes Elysium after Aeon. Add that step once you own Elysium."),

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

 dict(id="10", title="Going 2nd into Natasha's Dragoon", tag="Built from card text · practise it",
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
 dict(id="8", title="Aleister got Drolled", tag="Sourced: Taffy (MDM) · needs Chorozo",
  needs=["Aleister", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa"],
  stages=[
   ("No more searches needed", [
    "Normal Summon Aleister → search **Invocation** (Droll hits after this)",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**",
    "Invocation GY: add the banished Aleister (not from Deck, so Droll can't stop it)",
    "Discard Aleister on Sorath → Sorath revives Aleister",
    "Aleister + Artemis → **Chorozo**",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Sorath GY: Sorath + Aleister → **Mechaba**"]),
  ],
  end="Baronne · Mechaba"),

 dict(id="9", title="Reminiscent got Drolled", tag="Sourced: Taffy (MDM) · needs Chorozo",
  needs=["Reminiscent"],
  stages=[
   ("No more searches needed", [
    "Normal Summon Reminiscent: banish **Raidjin** → search **Invoke Sword** (Droll hits after this)",
    "Invoke Sword: Reminiscent + Raidjin (banished) → **Sorath**",
    "Sorath: revive Reminiscent",
    "Link Reminiscent → **Artemis**",
    "Invoke Sword GY: add Reminiscent (from GY, Droll can't stop it)",
    "Reminiscent: target Sorath → Special Summon itself",
    "Reminiscent + Artemis → **Chorozo**",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Sorath GY: Sorath + Raidjin + Chorozo → **Aeon** (banish up to 3, pick 3 from her Extra Deck)"]),
  ],
  end="Baronne · Aeon · up to 6 of hers banished"),

 dict(id="11", title="Going 2nd: finishers", tag="Built from card text · add to the end of any line",
  needs=["Use whatever you have left"],
  stages=[
   ("Remove her blocker", [
    "**Invoke Sword in hand** (Omega in Extra Deck): Aleister + a Fusion (both banished) → **Omega** → banish her monster",
    "**Super Poly:** Madness (counts as Aleister) + her monster → Fusion by her Attribute: LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**, DARK/WATER **Oceanus**",
    "Do Super Poly BEFORE Invocation uses Madness. Invocation can still use Madness from the GY"]),
   ("More damage", [
    "**Aleister in hand:** discard during battle → a Fusion gains 1000",
    "**Oceanus in GY:** banish it → one Fusion can attack directly",
    "**Little Knight:** SKIP its banish or you can't attack directly"]),
   ("Attack values", [
    "Aeon 3800 · Oceanus 3000 · Baronne 3000 · Omega 2800 · Mechaba 2500 · Baybarron 2450",
    "Raidjin 2200 · Madness 1800 · Sorath 1600 · Little Knight 1600 · Virakam 1000"]),
  ],
  end="Count to 8000 before you start the Battle Phase"),
]


import copy
_by = {L["id"]: L for L in LINES}

def _opened(base_id, title, needs, extra_memo):
    L = copy.deepcopy(_by[base_id])
    L["title"] = title
    L["needs"] = needs
    L["tag"] = L["tag"] + " · opener: Dawnstar (MDM)"
    L["stages"].insert(0, ("Get Aleister", [
        "**Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister** (Aiwass gives you an extra Normal Summon). With **Meltdown** or **Aiwass in hand**, just search Aleister"]))
    memo = "Sacred Sword: only Fusions can attack this turn." + (" " + extra_memo if extra_memo else "")
    L["memo"] = (L.get("memo", "") + " " + memo).strip()
    return L

_OPEN = "Sacred Sword, Meltdown or Aiwass"
_GET = ("Get Aleister", ["Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)"])
ATTR_SP = "by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**"

FIRST = [
    _by["1"],
    _opened("1", "Opener + Reminiscent", [_OPEN, "Reminiscent", "+1 spare card"], ""),
    _by["4"], _by["3"], _by["5"],
    _opened("5", "Opener + FIRE/WIND", [_OPEN, "FIRE/WIND (an Aiwass in hand counts: WIND)", "+1 spare card"],
            "If Sacred Sword opened, an Aiwass in hand is your WIND monster."),
    _by["6"],
    _opened("6", "Opener + any card", [_OPEN, "+1 spare card"], ""),
    _by["7"], _by["8"], _by["9"],
    dict(title="No starter: pass with hand traps", tag="Going 1st · brick hand · card text",
      needs=["No Aleister, Reminiscent, Meltdown, Aiwass, Sacred Sword, Spenta, Crowley or Zoroa"],
      stages=[
       ("Your turn", [
        "**Don't summon or set anything.** Fuwalos and Imperm from hand only work while you control no cards",
        "End your turn"]),
       ("Her turn", [
        "**Fuwalos:** early in her Main Phase. Draw 1 for each Deck/Extra Deck summon, to find a starter",
        "**Maxx \"C\":** her first Special Summon. **Ash / Droll / Imperm / Ghost Belle / Ghost Ogre:** see Line S1",
        "**Nibiru:** after her 5th summon this turn, tributes her whole board",
        "Fuwalos and Droll don't mix: Droll blocks your Fuwalos draws"]),
       ("Your next turn", [
        "Play the best line your new hand fits",
        "**TTT:** live if she activated a monster effect during your turn (e.g. a hand trap on you)"]),
      ],
      end="Nothing on board, but a full hand of interaction",
      memo="Don't Normal Summon Fuwalos or Nibiru: they're worth far more in hand."),
]
for _i, _L in enumerate(FIRST, 1):
    _L["id"] = str(_i)
    _L["when"] = "1st"

S1 = dict(title="Her turn: your hand traps", tag="Going 2nd · card text",
  needs=["Whatever hand traps you hold"],
  stages=[("Timing", [
    "**Maxx \"C\":** on her first Special Summon. Draw 1 for every Special Summon this turn",
    "**Ash:** on an effect that searches, sends from her Deck, or summons from her Deck",
    "**Droll:** right after her first search, so the rest are blocked. Not in the same turn as Fuwalos",
    "**Imperm** (from hand, you control no cards): her starter monster on the field",
    "**Fuwalos:** early in her Main Phase, only while you control no cards",
    "**Ghost Belle:** her GY effects. **Ghost Ogre:** a card effect on the field (never Shining Sarcophagus)",
    "**Nibiru:** after her 5th summon this turn"])],
  end="Keep Super Poly for your turn",
  memo="Her deck tells you the order: search-heavy → Droll; summon-heavy → Maxx \"C\".")

S2 = copy.deepcopy(_by["1"])
S2.update(title="Aleister or opener + Reminiscent", tag="Going 2nd · Taffy's Line 1 with going-2nd changes (marked)",
  needs=["Aleister, Meltdown or Aiwass", "Reminiscent", "+1 spare card"])
_st = [list(x) for x in S2["stages"]]
_st[3][1] = [
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon: banish her **3 best cards on the field**, then pick 3 from her Extra Deck",
    "**Going-2nd change:** don't make Little Knight. Keep **Aeon** to attack",
    "Invoke Sword GY: add Invocation",
    "Invocation: Aleister + Endymion (GY) → **Mechaba**",
    "Invocation: Madness + Crowley (both on field) → **Oceanus** (Extra Monster Zone)",
    "**Baronne:** destroy 1 more of her cards (targets)",
    "**Battle:** Aeon 3800 + Baronne 3000 + Oceanus 3000 + Mechaba 2500 + Virakam 1000 = **13,300**"]
S2["stages"] = [_GET] + [tuple(x) for x in _st]
S2["end"] = "Her field cleared, 13,300 damage if nothing stops it"
S2["memo"] = "Open with Meltdown or Aiwass from hand, not Sacred Sword. After Sacred Sword only Fusions can attack, so Baronne and Virakam couldn't."

S3 = dict(title="Aleister or opener + FIRE/WIND + Super Poly", tag="Going 2nd · Taffy's Aleister line + Super Poly (card text)",
  needs=["Aleister, Meltdown or Aiwass", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Super Poly", "+2 spare cards"],
  stages=[_GET,
   ("Get Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath → Sorath revives Aleister"]),
   ("Crowley into Baybarron", [
    "Link Aleister + Artemis → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (it summons itself)",
    "Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Invoke Sword**"]),
   ("Break her board", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard spare → search **Invocation**",
    "**Super Poly** (discard spare): Madness + her best monster → " + ATTR_SP,
    "Invocation: Madness (GY) + Crowley (GY) → **Oceanus** (EMZ). If Super Poly made Oceanus, keep this Invocation",
    "**Invoke Sword in hand** (Omega in Extra Deck): Aleister + Sorath (banished) → **Omega** → banish another of her monsters",
    "**Battle:** Oceanus 3000 + Mechaba 2500 + Super Poly Fusion (+ Omega 2800, + Virakam 1000 if no Sacred Sword)"]),
  ],
  end="Her best monster gone, 5,500+ damage",
  memo="Super Poly MUST come before Invocation uses Madness. Once activated, Super Poly can't be cancelled.")

S4 = dict(title="Aleister or opener + any card + Super Poly", tag="Going 2nd · Taffy's weakest line + Super Poly (card text)",
  needs=["Aleister, Meltdown or Aiwass", "Super Poly", "+2 spare cards"],
  stages=[_GET,
   ("Get Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Almiraj**",
    "Invocation: Aleister + Almiraj → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath → Sorath revives Aleister"]),
   ("Break her board", [
    "Link Aleister + Sorath → **Madness**",
    "Sorath GY: Sorath + Aleister → **Baybarron**. Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**, skip banish)",
    "Special Summon Virakam → set **Invoke Sword**",
    "**Super Poly** (discard spare): Madness + her best monster → " + ATTR_SP,
    "Invocation: Madness (GY) + Virakam → **Mechaba**",
    "**Battle:** Baybarron 2450 + Mechaba 2500 + Super Poly Fusion"]),
  ],
  end="Her best monster gone, about 7,000 damage")

S3C = dict(title="Super Poly into Chorozo: steal 2", tag="Going 2nd · found by Lewis, won with it in Solo 14 Nov · order checked against card text",
  needs=["Aleister, Meltdown or Aiwass", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Super Poly", "+1 spare card",
         "She controls an Extra Deck monster (Fusion/Synchro/Xyz/Link) + a Spellcaster"],
  stages=[
   ("Get Aleister", ["**Aiwass from hand:** banish it → add **Aleister** (best: banished Aiwass is WIND material for the finish). Or Meltdown → Aleister"]),
   ("Take her two monsters", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "**Super Poly** (discard spare): her Extra Deck monster + her Spellcaster → **Chorozo**",
    "Artemis: equip to Chorozo → search **Crowley**. It summons itself, then fuse: Crowley + FIRE/WIND (hand) → **Sorath**"]),
   ("Baronne and Aeon", [
    "Sorath: revive Crowley",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Invocation: **Sorath + Chorozo (both in GY)** → **Aeon**: banish 2 of her cards",
    "**Baronne:** destroy 1 more of her cards"]),
   ("Finish", [
    "**Invoke Sword in hand** (optional): Crowley (field) + Aiwass (banished, WIND) → **Raidjin**",
    "**Battle:** Aeon 3800 + Baronne 3000 + Crowley 1800 = **8,600** (Raidjin instead of Crowley: 9,000)"]),
  ],
  end="Her 2 monsters gone + 3 more of her cards removed · Aeon · Baronne · Crowley or Raidjin",
  memo="Aeon needs no Aleister: 2 Fusions with different Attributes from your GY are enough. Exosister and Dark Magician decks are full of Spellcasters.")

S5B = dict(title="Spenta or Crowley + FIRE/WIND + Invocation + Invoke Sword", tag="Going 2nd · no Aleister needed · UNTESTED, built from card text",
  needs=["Spenta or Crowley", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Invocation", "Invoke Sword"],
  stages=[
   ("Sorath into Madness", [
    "**Spenta:** discard → search **Crowley** (it summons itself). Or Normal Summon Crowley from hand. Crowley + FIRE/WIND (hand) → **Sorath**",
    "Sorath: revive **Crowley**",
    "Link Crowley + Sorath → **Madness** (counts as Aleister on field and in GY)"]),
   ("Aeon", [
    "**Invocation:** Madness + Sorath (GY) → **Baybarron**: search **Virakam**, SKIP the banish",
    "**Invoke Sword:** Baybarron + Sorath (banished) → **Aeon** (FIRE + LIGHT)",
    "**Aeon:** banish her best monster + 1 more of her cards",
    "**Battle:** Aeon 3800"]),
  ],
  end="Aeon · her 2 best cards banished",
  memo="TTT goes live if she activates a monster effect on your turn. Crowley counts as Aleister only while face-up, so a Crowley revived by Sorath (negated) doesn't.")

S5G = dict(title="Spenta or Crowley + FIRE/WIND + Grail + Invocation", tag="Going 2nd · no Aleister needed · UNTESTED, built from card text",
  needs=["Spenta or Crowley", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Grail", "Invocation", "She has a face-up monster"],
  stages=[
   ("Sorath into Madness", [
    "**Crowley:** Normal Summon it (or Spenta: discard → search Crowley, it summons itself). Crowley + FIRE/WIND (hand) → **Sorath**",
    "Sorath: revive **Crowley**",
    "Link Crowley + Sorath → **Madness** (counts as Aleister, turns on Grail)"]),
   ("Take her monster, then Aeon", [
    "**Grail mode 2:** Madness + her face-up monster → by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, WIND **Raidjin**. (Extra Deck monster of any Attribute → **Omega**)",
    "**Invocation:** that Fusion + Sorath (GY) → **Aeon** (different Attributes)",
    "**Aeon:** banish her 2 other cards",
    "**Battle:** Aeon 3800"]),
  ],
  end="Her whole field gone (up to 3 cards) · Aeon",
  memo="Grail doesn't target, so it gets round Dragoon. If her monster is FIRE, Sorath is already used: play S8 instead if you have Invoke Sword.")

S3G = dict(title="Aleister or opener + FIRE/WIND + Grail", tag="Going 2nd · Taffy's Aleister line + Grail · UNTESTED, built from card text",
  needs=["Aleister, Meltdown or Aiwass", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Grail", "Invocation or a spare card"],
  stages=[_GET,
   ("Get Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath → Sorath revives Aleister"]),
   ("Crowley into Baybarron", [
    "Link Aleister + Artemis → **Endymion**, equip Artemis",
    "Artemis: search **Crowley** (it summons itself). Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Invoke Sword**"]),
   ("Grail, then Aeon", [
    "Link Sorath + Baybarron → **Madness**",
    "Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard spare (TTT) → search **Invocation**",
    "**Grail mode 2:** Madness + her best monster (tap it for its Attribute): DARK/WATER **Oceanus**, WIND **Raidjin**. LIGHT/EARTH/FIRE: use another of her monsters",
    "**Invocation:** Mechaba + the Grail Fusion → **Aeon**: banish her other monster + her set card",
    "**Battle:** Aeon 3800 + Virakam 1000"]),
  ],
  end="Her 3 cards gone · Aeon · Virakam · set Invoke Sword",
  memo="Grail doesn't target, so it gets round Dragoon.")

S6I = dict(title="Aleister got Imperm'd + FIRE/WIND + Grail", tag="Going 2nd · UNTESTED, built from card text",
  needs=["Aleister on field (search negated)", "FIRE/WIND: Ash, Droll, Fuwalos, Zoroa", "Invocation", "Grail"],
  stages=[
   ("Imperm doesn't stop its name", [
    "**Invocation:** Aleister (field) + FIRE/WIND (hand) → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath (+1000) → Sorath revives Aleister (Defence)"]),
   ("Take her monster", [
    "**Grail mode 2:** Aleister + her best monster (tap it for its Attribute): DARK/WATER **Oceanus**, WIND **Raidjin**, LIGHT **Mechaba**, EARTH **Baybarron**. If it's FIRE, take another of hers",
    "**Battle:** the Grail Fusion + Sorath 2600"]),
  ],
  end="Her best monster gone · Sorath · Grail Fusion",
  memo="Imperm negates Aleister's search, not its name, so Invocation and Grail still work.")

SECOND = [S1, S2, S3C, S3G, S3, S4, S5G, S5B, S6I]
TIPS = [copy.deepcopy(_by["10"]), copy.deepcopy(_by["11"])]
TIPS[1]["memo"] = "Every going-2nd line already includes these where they fit."
for _i, _L in enumerate(SECOND, 1):
    _L["id"] = "S" + str(_i)
    _L["when"] = "2nd"
for _i, _L in enumerate(TIPS, 1):
    _L["id"] = "T" + str(_i)
    _L["when"] = "tips"
for _L in FIRST:
    if _L.get("memo"):
        _L["memo"] = _L["memo"].replace("see Line 13 for the finishers", "see Tip T2 for the finishers")

LINES = FIRST + SECOND + TIPS

INDEX1 = [
 ("Aleister + Reminiscent", "1", True),
 ("Sacred Sword / Meltdown / Aiwass + Reminiscent", "2", True),
 ("Crowley or Spenta + Reminiscent + FIRE/WIND", "3", False),
 ("Reminiscent alone", "4", False),
 ("Aleister + Ash / Droll / Fuwalos / Zoroa", "5", False),
 ("Sacred Sword / Meltdown / Aiwass + FIRE/WIND", "6", False),
 ("Aleister + any card", "7", False),
 ("Sacred Sword / Meltdown / Aiwass + any card", "8", False),
 ("Zoroa or Spenta, no Aleister", "9", False),
 ("Got Drolled after Aleister's search", "10", False),
 ("Got Drolled after Reminiscent's search", "11", False),
 ("No starter at all (brick)", "12", False),
]
INDEX2 = [
 ("Her turn first: which hand trap, when", "S1", False),
 ("Aleister or opener + Reminiscent", "S2", True),
 ("Super Poly: she has an Extra Deck monster + a Spellcaster", "S3", True),
 ("Aleister or opener + FIRE/WIND + Grail", "S4", True),
 ("Aleister or opener + FIRE/WIND + Super Poly", "S5", True),
 ("Aleister or opener + any card + Super Poly", "S6", False),
 ("Spenta or Crowley + FIRE/WIND + Grail + Invocation", "S7", False),
 ("Spenta or Crowley + FIRE/WIND + Invocation + Invoke Sword", "S8", False),
 ("Aleister got Imperm'd + FIRE/WIND + Grail", "S9", False),
]
INDEX3 = [
 ("Going 2nd into Natasha's Dragoon", "T1", False),
 ("Finish the turn: damage tricks and attack values", "T2", False),
]
INDEX = INDEX1
RULES = [
 "Baybarron: say SKIP to the banish unless you've picked a target",
 "Madness needs a spare card to discard. Keep one",
 "Oceanus goes in the Extra Monster Zone",
 "Before any Link: is there a free zone?",
 "Read both GYs + banishment before Invocation. Invocation can use a FIRE/WIND (or any) monster from EITHER GY: use that before spending a card from hand",
 "Discard order: dead copies (2nd Meltdown, used Invoke Sword) → Fuwalos → Imperm → Crossout → Ghost Belle. KEEP Maxx C, Ash, Super Poly, Droll, Nibiru",
 "Mechaba: keep 1 monster + 1 Spell/Trap in hand if you can",
 "Imperm on Aleister or Crowley: Aleister keeps its name (Invocation/Grail still work); Crowley does not",
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
    for label, idx in (("Going 1st", INDEX1), ("Going 2nd", INDEX2), ("Tips & tricks", INDEX3)):
        h += f"<div class='tag' style='margin-top:14px'>{label} · top row wins</div><table>"
        for hand, line, best in idx:
            h += f"<tr class='{'best' if best else ''}'><td>{fmt(hand)}</td><td><span class='pill'>Line {line}</span></td></tr>"
        h += "</table>"
    h += "<div class='stage rules' style='margin-top:10px'><div class='sh'>Golden rules</div><ol>"
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
