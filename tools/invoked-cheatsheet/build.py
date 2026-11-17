import re, html
from playwright.sync_api import sync_playwright

import os, sys
VERSION = "3.1"
DATE = "17 Nov 2026"
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
    dict(title="Opener + Spenta + Crowley", tag="Going 1st · Line 6 with Spenta finding the FIRE · UNTESTED, built from card text",
      needs=["Sacred Sword (or Meltdown / Aiwass)", "Spenta", "Crowley", "+1 spare card (Spenta #2 from Artemis covers it)"],
      stages=[
       ("Get Aleister and Zoroa", [
        "**Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister**, Normal Summon it straight away → search **Invocation**",
        "**Spenta:** discard → search **Zoroa** (FIRE)"]),
       ("Get Sorath", [
        "Link Aleister → **Artemis**",
        "Invocation: Aleister (GY) + Zoroa (hand) → **Sorath**",
        "Invocation GY: add the banished Aleister",
        "Discard Aleister on Sorath → Sorath revives Aleister"]),
       ("Crowley into Baybarron", [
        "Link Aleister + Artemis → **Endymion**, equip Artemis",
        "Artemis: search **Spenta #2**",
        "**Normal Summon Crowley:** Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish",
        "Special Summon Virakam → set **Invoke Sword**"]),
       ("Finish", [
        "Link Sorath + Baybarron → **Madness**",
        "Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard Spenta #2 → search **Invocation**",
        "Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)"]),
      ],
      end="Oceanus (EMZ) · Mechaba · Virakam · set Invoke Sword · Nibiru/Grail etc. still in hand",
      memo="If the game won't let you Normal Summon Crowley (Aiwass's summon may use up your Normal Summon): skip Endymion, Link Aleister + Sorath → Madness, Sorath GY: Sorath + Aleister → Baybarron (search Virakam), Madness discards Crowley → Invocation, Virakam → Invoke Sword, Invocation: Madness + Virakam → Mechaba."),
    _by["6"],
    _opened("6", "Opener + any card", [_OPEN, "+1 spare card"], ""),
    _by["7"], _by["8"], _by["9"],
    dict(title="Drolled before you got Invocation", tag="Going 1st · e.g. Aiwass/Meltdown search got Drolled · UNTESTED, built from card text",
      needs=["Aleister (on hand or field)", "Virakam, or Invocation already in hand", "Droll in her GY (it's WIND)", "Reminiscent helps (+ body)"],
      stages=[
       ("Droll rules", [
        "Droll blocks **adding from Deck to hand** (draws too). It does NOT block **Setting** from Deck, or adding from GY/banishment",
        "**TTT:** don't pick Draw 2. Pick look at her hand + shuffle 1 away"]),
       ("Get Sorath", [
        "Normal Summon Aleister. **SKIP** its search",
        "**Virakam:** Special Summon → **Set Invocation** from Deck (Normal Spell: usable this turn). Skip if Invocation is in hand",
        "Link Aleister → **Artemis**",
        "**Invocation:** Aleister (your GY) + **Droll (her GY, WIND)** → **Sorath**",
        "Invocation GY: add banished Aleister (from banishment: Droll can't stop it)",
        "Discard Aleister on Sorath → Sorath revives Aleister"]),
       ("Baronne and Mechaba", [
        "**Reminiscent:** target Sorath → Special Summon itself. **SKIP** its search",
        "Aleister + Artemis → **Chorozo**",
        "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
        "Sorath GY: Sorath + Aleister → **Mechaba**"]),
      ],
      end="Baronne · Mechaba · Virakam · Reminiscent",
      memo="No Virakam/Invocation/Grail/Crowley: NS Aleister (skip search), Reminiscent targets Aleister (skip search), Link Aleister → Artemis, Artemis + Reminiscent → S:P Little Knight. One interruption."),
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
S2["memo"] = "Open with Meltdown or Aiwass from hand, not Sacred Sword. After Sacred Sword only Fusions can attack, so Baronne and Virakam couldn't. Aleister's search Ash'd or Imperm'd? With an Invocation already in hand, play the line unchanged (Imperm leaves its name, so it still targets for Reminiscent and works as material)."

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

S2X = copy.deepcopy(S2)
S2X.update(title="Aleister's search stopped + Reminiscent + Invocation", tag="Going 2nd · S1 with Aleister Imperm'd or Ash'd · card text",
  needs=["Aleister on field (search negated by Imperm/Ash)", "Reminiscent", "Invocation already in hand", "+1 spare card"],
  memo="Imperm doesn't change Aleister's name: Reminiscent can still target it and it still counts as Aleister for Fusions. If Imperm was SET, it also negates Spell/Trap effects in its column this turn: put your Spells in another column.")
_st = [list(x) for x in S2X["stages"]][1:]
_st[0][1] = ["Aleister's search was stopped: you already hold **Invocation**, so carry on"] + _st[0][1][1:]
S2X["stages"] = [tuple(x) for x in _st]

SECOND = [S2, S2X, S3C, S3G, S3, S4, S5G, S5B, S6I]
T_AEON = dict(title="Clear her board with Aeon (no Normal Summon left)", tag="Tip · card text · UNTESTED",
  needs=["A Fusion on your field", "Grail", "Invocation (or Reminiscent to search it)", "Aleister in hand (or Meltdown)"],
  stages=[("Line", [
    "**Meltdown** (if held): search **Aleister**. Your Fusions can't be negated",
    "**Reminiscent** (if held): Special Summon it targeting your Fusion. Banish De Anima → search **Invocation**",
    "**Grail mode 1:** Aleister (hand) + a Deck monster → a Fusion with a **different Attribute** from the one on your field (e.g. Crowley DARK → **Oceanus**, Droll/Aiwass WIND → **Raidjin**)",
    "**Invocation:** both Fusions → **Aeon**: banish 2 of her cards",
    "Attack"])],
  end="Her 2 best cards gone · Aeon 3800",
  memo="Aeon needs different Attributes: Sorath and Mechaba are both LIGHT.")

T_PR = dict(title="Planet Run deck: what's different", tag="Side deck · secondary",
  needs=["Planet Run event deck"],
  stages=[("Differences from the ranked deck", [
    "**No Zoroa:** FIRE/WIND material is Ash, Droll, Fuwalos or a banished Aiwass",
    "**No Ghost Ogre:** for Grail mode 1 LIGHT material use Spenta or Nibiru from the Deck",
    "Every other line works the same"])],
  end="Ranked lines first; check this before naming Deck monsters in Planet Run",
  memo="Send the Planet Run list after any change so this stays right.")

TIPS = [S1, copy.deepcopy(_by["10"]), copy.deepcopy(_by["11"]), T_AEON, T_PR]
TIPS[2]["memo"] = "Every going-2nd line already includes these where they fit."
for _i, _L in enumerate(SECOND, 1):
    _L["id"] = "S" + str(_i)
    _L["when"] = "2nd"
for _i, _L in enumerate(TIPS, 1):
    _L["id"] = "T" + str(_i)
    _L["when"] = "tips"
for _L in FIRST:
    if _L.get("memo"):
        _L["memo"] = _L["memo"].replace("see Line 13 for the finishers", "see Tip T3 for the finishers")

# ---------------------------------------------------------------------------
# v3.0: the sheet follows Lewis's new Invoked deck (16 Nov 2026).
# Main: Droll 2, Maxx "C" 1, Ghost Ogre 2, Ash 3, Virakam 1, Aleister 3, Fuwalos 3, Purulia 2,
#       Reminiscent 3, Aiwass 3, Invocation 2, TTT 1, Sacred Sword 3, Meltdown 3, Super Poly 2,
#       Crossout 1, Invoke Sword 2, Imperm 3.
# Extra: Borreload Savage Dragon, Chorozo, Raidjin, Sorath, Baybarron, Madness (in for Omega),
#       De Anima, Mechaba, Oceanus, Elysium, Aeon 2, Baronne, Artemis, Little Knight.
# No Crowley, Spenta, Zoroa, Grail, Nibiru, Gamma Summon, Endymion or Almiraj.
# The old InvokedRD lines are kept below as the archive (ids A1...).
# ---------------------------------------------------------------------------

OLD = [copy.deepcopy(L) for L in FIRST + SECOND + TIPS]
_old_map = {}
for _i, _L in enumerate(OLD, 1):
    _old_map[(_L["when"], _L["id"])] = "A" + str(_i)
    _L["id"] = "A" + str(_i)
    _L["tag"] = "Old deck (InvokedRD) · " + _L["tag"]
    _L["old_when"] = _L["when"]
    _L["when"] = "old"

N_GET = ("Get Aleister", ["Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)"])
N_OPEN = "Sacred Sword, Meltdown or Aiwass"
N_OPEN_STAGE = ("Get Aleister", [
    "**Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister** → Normal Summon it straight away. **Aiwass from hand:** banish it → add Aleister. **Meltdown:** add Aleister"])

N1 = dict(title="Aleister + Reminiscent", tag="Taffy's Line 1 with Reminiscent doing Crowley's jobs · UNTESTED, built from card text · BEST LINE",
  needs=["Aleister", "Reminiscent", "+1 spare card"],
  stages=[
   ("1 · Searches", [
    "Normal Summon Aleister → search **Invocation**",
    "Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**"]),
   ("2 · Chorozo and Baybarron", [
    "Link Aleister → **Artemis**",
    "Artemis + Reminiscent → **Chorozo** (contact fusion: send both)",
    "Invocation: Aleister (GY) + Artemis (GY, LIGHT) → **Baybarron**: search **Virakam**, SKIP the banish",
    "Special Summon Virakam → set **Invoke Sword #2** (for her turn)"]),
   ("3 · Sorath, Madness, Baronne", [
    "Invoke Sword (hand): Aleister + Raidjin (both banished) → **Sorath**",
    "Sorath: revive **Reminiscent** (Defence)",
    "Link Baybarron + Reminiscent → **Madness** (Extra Monster Zone)",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**. Don't put it where Madness's arrows point"]),
   ("4 · Aeon finish", [
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon (banish 3 from her Extra Deck)",
    "Link Aeon + Virakam → **Little Knight** (in a zone Madness points to). SKIP its banish",
    "Invoke Sword GY: add **Invocation**",
    "Invocation: Aleister (GY) + Virakam (GY, LIGHT) → **Mechaba**",
    "Invocation: Madness + Reminiscent (GY, DARK) → **Oceanus** (Extra Monster Zone)",
    "Invocation GY: add the banished **Aleister**"]),
  ],
  end="Baronne · Mechaba · Oceanus (EMZ) · Little Knight · set Invoke Sword · Aleister in hand · 3 of her Extra Deck banished",
  memo="Madness can't be Baybarron + Virakam: both are Illusion. Raidjin is used 3 times (cost → Invoke Sword → Aeon).")

N2 = copy.deepcopy(N1)
N2.update(title="Opener + Reminiscent", tag=N1["tag"].replace(" · BEST LINE", "") + " · opener: Dawnstar (MDM)",
  needs=[N_OPEN, "Reminiscent", "+1 spare card"])
N2["stages"] = [N_OPEN_STAGE] + N2["stages"]
N2["memo"] = "Aleister already in hand? Sacred Sword or Aiwass can search **Reminiscent** instead, then play this line. " + N1["memo"]

N3 = dict(title="Aleister + FIRE/WIND", tag="Sourced: Taffy (MDM) Droll combo · works with this deck",
  needs=["Aleister", "FIRE/WIND: Ash, Droll, Fuwalos (or a WIND/FIRE in either GY)", "+1 spare card"],
  stages=[
   ("Sorath", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + FIRE/WIND → **Sorath**",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Sorath → Sorath revives Aleister"]),
   ("Baronne and Mechaba", [
    "Aleister + Artemis → **Chorozo** (contact fusion)",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Sorath GY: Sorath + Aleister → **Mechaba**"]),
  ],
  end="Baronne · Mechaba · spare card for Mechaba's cost",
  memo="Got Drolled after Aleister's search? Same line: nothing here searches. Droll in her GY is WIND, so Invocation can use it instead of a hand card.")

N4 = copy.deepcopy(N3)
N4.update(title="Opener + FIRE/WIND", tag=N3["tag"] + " · opener: Dawnstar (MDM)",
  needs=[N_OPEN, "FIRE/WIND (an Aiwass in hand counts: WIND)", "+1 spare card"])
N4["stages"] = [N_OPEN_STAGE] + N4["stages"]
N4["memo"] = "If Sacred Sword opened, an Aiwass still in hand is your WIND monster. " + N3["memo"]

N5 = dict(title="Reminiscent alone", tag="Sourced: Taffy (MDM) Reminiscent Droll combo",
  needs=["Reminiscent"],
  stages=[
   ("Sorath", [
    "Normal Summon Reminiscent: banish **Raidjin** → search **Invoke Sword**",
    "Invoke Sword: Reminiscent + Raidjin (banished) → **Sorath**",
    "Sorath: revive Reminiscent",
    "Link Reminiscent → **Artemis**",
    "Invoke Sword GY: add Reminiscent to hand",
    "Reminiscent: target Sorath → Special Summon itself"]),
   ("Baronne and Aeon", [
    "Reminiscent + Artemis → **Chorozo** (contact fusion)",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Sorath GY: Sorath + Raidjin + Chorozo → **Aeon**: banish 3 from her Extra Deck"]),
  ],
  end="Baronne · Aeon · 3 of her Extra Deck banished",
  memo="Got Drolled after Reminiscent's search? Same line: nothing else searches.")

N6 = dict(title="Aleister + any card", tag="UNTESTED · built from card text (Artemis is the LIGHT for Baybarron)",
  needs=["Aleister", "+1 spare card (Mechaba's cost)"],
  stages=[
   ("Baybarron", [
    "Normal Summon Aleister → search **Invocation**",
    "Link Aleister → **Artemis**",
    "Invocation: Aleister (GY) + Artemis (GY, LIGHT) → **Baybarron**: search **Virakam**, SKIP the banish",
    "Invocation GY: add the banished Aleister",
    "Discard Aleister on Baybarron (+1000) → it's in your GY"]),
   ("Mechaba", [
    "Special Summon Virakam → set **Invocation** (Normal Spell: use it now)",
    "Invocation: Aleister (GY) + Virakam (LIGHT) → **Mechaba**"]),
  ],
  end="Baybarron · Mechaba",
  memo="Holding a WATER (Purulia) or DARK (Reminiscent) instead? Aleister + it → Oceanus. Reminiscent: play Line 1.")

N7 = copy.deepcopy(N6)
N7.update(title="Opener + any card", tag=N6["tag"], needs=[N_OPEN, "+1 spare card (Mechaba's cost)"])
N7["stages"] = [N_OPEN_STAGE] + N7["stages"]
N7["memo"] = "Sacred Sword or Aiwass: if Aleister's already in hand, search Reminiscent and play Line 1."

N8 = copy.deepcopy([L for L in FIRST if L["title"] == "Drolled before you got Invocation"][0])
N8["memo"] = "No Virakam or Invocation: Normal Summon Aleister (skip search), Reminiscent targets Aleister (skip search), Link Aleister → Artemis, Artemis + Reminiscent → S:P Little Knight. One interruption."
N8["needs"] = ["Aleister (in hand or on field)", "Virakam, or Invocation already in hand", "Droll in her GY (it's WIND)", "Reminiscent"]

N9 = dict(title="No starter: pass with hand traps", tag="Going 1st · brick hand · card text",
  needs=["No Aleister, Reminiscent, Meltdown, Aiwass or Sacred Sword"],
  stages=[
   ("Your turn", [
    "**Don't summon or set anything.** Fuwalos, Purulia and Imperm from hand only work while you control no cards",
    "End your turn"]),
   ("Her turn", [
    "**Fuwalos:** early in her Main Phase. Draws for her Deck/Extra Deck summons, to find a starter",
    "**Maxx \"C\":** her first Special Summon. **Ash / Droll / Imperm / Ghost Ogre:** see Tip T1",
    "Fuwalos and Droll don't mix: Droll blocks your draws"]),
   ("Your next turn", [
    "Play the best line your new hand fits",
    "**TTT:** live if she activated a monster effect during your turn (e.g. a hand trap on you)"]),
  ],
  end="Nothing on board, but a full hand of interaction",
  memo="Don't Normal Summon Fuwalos or Purulia: they're worth far more in hand.")

NEW_FIRST = [N1, N2, N3, N4, N5, N6, N7, N8, N9]
for _i, _L in enumerate(NEW_FIRST, 1):
    _L["id"] = str(_i)
    _L["when"] = "1st"

# ---- Going 2nd ----
M1 = copy.deepcopy(N1)
M1.update(title="Aleister or opener + Reminiscent", tag="Going 2nd · Line 1 with going-2nd changes (marked) · UNTESTED",
  needs=["Aleister, Meltdown or Aiwass", "Reminiscent", "+1 spare card"])
_st = [list(x) for x in M1["stages"]]
_st[3][1] = [
    "Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**",
    "Chain: Madness (discard spare → **Invocation**) + Aeon: banish her **3 best cards on the field**, then 3 from her Extra Deck",
    "**Going-2nd change:** no Little Knight. Keep **Aeon** to attack",
    "Invoke Sword GY: add **Invocation**",
    "Invocation: Aleister (GY) + Virakam (field, LIGHT) → **Mechaba**",
    "Invocation: Madness + Reminiscent (GY, DARK) → **Oceanus**",
    "**Baronne:** destroy 1 more of her cards (targets)",
    "**Battle:** Aeon 3800 + Baronne 3000 + Oceanus 3000 + Mechaba 2500 = **12,300**"]
M1["stages"] = [N_GET] + [tuple(x) for x in _st]
M1["end"] = "Her field cleared, 12,300 damage if nothing stops it"
M1["memo"] = "Opened with Sacred Sword? Only Fusions can attack: Aeon + Oceanus + Mechaba = 9,300, still lethal. Aleister's search Ash'd or Imperm'd with Invocation already in hand: play it unchanged (Imperm leaves its name)."

M2 = copy.deepcopy(N3)
M2.update(title="Aleister or opener + FIRE/WIND + Super Poly", tag="Going 2nd · Taffy's Droll combo + Super Poly into Elysium · UNTESTED, built from card text",
  needs=["Aleister, Meltdown or Aiwass", "FIRE/WIND: Ash, Droll, Fuwalos", "Super Poly", "+1 spare card",
         "She has an Extra Deck monster"])
M2["stages"] = [N_GET] + M2["stages"] + [
   ("Wipe her board", [
    "**Super Poly** (discard spare): Mechaba + her Extra Deck monster → **Elysium**. She can't respond",
    "**Elysium:** target **Elysium itself** → banish it and **all her monsters** (it has every Attribute). Or target an Invoked in your GY to banish only that Attribute and keep Elysium",
    "**Baronne:** destroy her best Spell/Trap",
    "**Battle:** Baronne 3000 (+ Elysium 3200 if you kept it)"])]
M2["end"] = "Her monsters gone, her best Spell/Trap gone · Baronne"
M2["memo"] = "Elysium doesn't target her monsters, so it gets round Dragoon. It does nothing to Timaeus the turn it lands."

M3 = dict(title="Aleister or opener + Super Poly (she has a Fusion)", tag="Going 2nd · built from card text · UNTESTED",
  needs=["Aleister, Meltdown or Aiwass", "Super Poly", "+1 spare card", "She controls a Fusion Monster (e.g. Dragoon)"],
  stages=[N_GET,
   ("Take her Fusion", [
    "Normal Summon Aleister → search **Invocation**",
    "**Super Poly** (discard spare): Aleister + her Fusion → " + "by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, FIRE/WIND **Sorath** (not Raidjin: Aeon needs different Attributes)"]),
   ("Aeon", [
    "Invocation: her Fusion (her GY) + your Fusion → **Aeon** (different Attributes): banish her 2 best cards",
    "Invocation GY: add the banished Aleister",
    "**Battle:** discard Aleister on Aeon → **4,800**"]),
  ],
  end="Her Fusion + 2 more of her cards gone · Aeon",
  memo="Made Baybarron? Search Virakam first: Virakam → set Invoke Sword for her turn.")

M4 = copy.deepcopy(N5)
M4.update(title="Reminiscent alone", tag="Going 2nd · Taffy's Reminiscent Droll combo · going-2nd changes marked")
_st = [list(x) for x in M4["stages"]]
_st[1][1] = [
    "Reminiscent + Artemis → **Chorozo** (contact fusion)",
    "Synchro: Chorozo + Sorath → **Baronne de Fleur**",
    "Sorath GY: Sorath + Raidjin + Chorozo → **Aeon**: banish her **3 best cards on the field**, then 3 from her Extra Deck",
    "**Baronne:** destroy 1 more of her cards",
    "**Battle:** Aeon 3800 + Baronne 3000 = **6,800**"]
M4["stages"] = [tuple(x) for x in _st]
M4["end"] = "4 of her cards gone · 6,800 damage"
M4["memo"] = "Super Poly in hand too? See Tip T3."

M5 = copy.deepcopy(N3)
M5.update(title="Aleister or opener + FIRE/WIND", tag="Going 2nd · Taffy's Droll combo + attack",
  needs=["Aleister, Meltdown or Aiwass", "FIRE/WIND: Ash, Droll, Fuwalos", "+1 spare card"])
M5["stages"] = [N_GET] + M5["stages"] + [("Attack", [
    "**Baronne:** destroy her best card",
    "**Battle:** Baronne 3000 + Mechaba 2500 = **5,500**"])]
M5["end"] = "1 of her cards gone · 5,500 damage · Mechaba up"
M5["memo"] = "Sacred Sword opener: only Fusions attack, so Baronne can't (2,500)."

M6 = copy.deepcopy(N6)
M6.update(title="Aleister or opener + any card", tag="Going 2nd · UNTESTED, built from card text",
  needs=["Aleister, Meltdown or Aiwass", "+1 spare card"])
M6["stages"] = [N_GET] + M6["stages"] + [("Attack", ["**Battle:** Baybarron 2450 + Mechaba 2500 = **4,950**"])]
M6["end"] = "Baybarron · Mechaba · 4,950 damage"
M6["memo"] = "Her monster in the way? Banish Baybarron from your GY later to shrink her monsters (Tip T3)."

NEW_SECOND = [M1, M2, M3, M4, M5, M6]
for _i, _L in enumerate(NEW_SECOND, 1):
    _L["id"] = "S" + str(_i)
    _L["when"] = "2nd"

# ---- Tips ----
P1 = dict(title="Her turn: your hand traps", tag="Going 2nd · card text",
  needs=["Whatever hand traps you hold"],
  stages=[("Timing", [
    "**Maxx \"C\":** on her first Special Summon. Draw 1 for every Special Summon this turn",
    "**Ash:** on an effect that searches, sends from her Deck, or summons from her Deck",
    "**Droll:** right after her first search, so the rest are blocked. Not in the same turn as Fuwalos",
    "**Imperm** (from hand, you control no cards): her starter monster on the field",
    "**Fuwalos / Purulia:** early in her Main Phase, only while you control no cards",
    "**Ghost Ogre:** a card effect on the field (never Shining Sarcophagus)",
    "**Crossout Designator:** your turn, before you combo: name the hand trap she's likely to hold (Ash, Maxx \"C\")"])],
  end="Keep Super Poly for your turn",
  memo="Her deck tells you the order: search-heavy → Droll; summon-heavy → Maxx \"C\".")

P2 = dict(title="Going 2nd into Natasha's Dragoon", tag="Built from card text · practise it",
  needs=["Aleister route", "Super Poly", "Imperm (ideal)"],
  stages=[
   ("Her turn", ["**Imperm Imsety** (stops her send-to-GY punish)"]),
   ("Plan A: Aleister + Super Poly", [
    "Meltdown → Aleister (bait Dragoon's negate here)",
    "Normal Summon Aleister → search **Invocation**",
    "**Super Poly:** Aleister + Dragoon → **Oceanus** (she can't respond)",
    "Invocation: Dragoon (her GY) + Oceanus → **Aeon**: banish **King's Sarcophagus** + her best Horus",
    "Attack"]),
   ("Plan B: an Invoked already out", [
    "**Super Poly:** your Invoked (e.g. Sorath) + Dragoon → **Elysium**",
    "**Elysium:** target itself → banish all her monsters"]),
  ],
  end="Dragoon gone · Sarcophagus or her whole field gone",
  memo="Can't touch Timaeus the turn it lands or her next turn. Ghost Ogre can't touch Shining Sarcophagus.")

P3 = dict(title="Going 2nd: finishers", tag="Built from card text · add to the end of any line",
  needs=["Use whatever you have left"],
  stages=[
   ("Remove her blocker", [
    "**Super Poly + an Invoked you control + her Extra Deck monster → Elysium.** Elysium targets itself → all her monsters banished",
    "**Super Poly:** Madness or Aleister + her monster → by her Attribute: LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**, DARK/WATER **Oceanus**",
    "Do Super Poly BEFORE Invocation uses Madness. Invocation can still use Madness from the GY"]),
   ("More damage", [
    "**Aleister in hand:** discard during battle → a Fusion gains 1000",
    "**Oceanus in GY:** banish it → one Fusion can attack directly",
    "**Baybarron in GY:** banish it, target your Fusion → her monsters lose that much ATK",
    "**Little Knight:** SKIP its banish or you can't attack directly"]),
   ("Attack values", [
    "Aeon 3800 · Elysium 3200 · Oceanus 3000 · Baronne 3000 · Borreload 3000+ · Mechaba 2500 · Baybarron 2450",
    "Raidjin 2200 · Madness 1800 · Sorath 1600 · Little Knight 1600 · Virakam 1000 · Artemis 800"]),
  ],
  end="Count to 8000 before you start the Battle Phase",
  memo="Every going-2nd line already includes these where they fit.")

P4 = dict(title="Borreload Savage Dragon instead of Baronne", tag="Card text · UNTESTED",
  needs=["Chorozo + a Level 4 (Aleister or Reminiscent) on your field", "A Link in your GY (Madness best)"],
  stages=[("Line", [
    "Synchro: Chorozo (Level 4 Tuner) + Aleister or Reminiscent (Level 4) → **Borreload Savage Dragon**",
    "On summon: equip a Link from your GY. **Madness** = 2 counters, 3900 ATK. **Little Knight** = 2 counters, 3800. **Artemis** = 1 counter, 3400",
    "Her turn: remove 1 counter → negate her card or effect (once per turn)"])],
  end="An omni-negate that lasts as many turns as it has counters",
  memo="You have 1 Chorozo: Baronne (Chorozo + Sorath, Level 6) OR Borreload (Chorozo + a Level 4). Use Borreload when Sorath is needed for something else.")

P5 = dict(title="Saturday gauntlet: who you're facing", tag="Matchup notes · card text + MDM",
  needs=["10–20 games back to back"],
  stages=[
   ("Labrynth / Starter Decks", [
    "Play a **short line** (3 or 5). Baronne + Mechaba or Baronne + Aeon is plenty. Saves the timer and your head",
    "**Ghost Ogre** and **Droplet** are good into Labrynth's traps and Furniture"]),
   ("Natasha (Shining Sarcophagus · Dragoon · Horus)", [
    "Going 1st: **Line 1**. Her turn: **Imperm Imsety**, **Ash** her Sarcophagus search, Droll after her first search",
    "Going 2nd: **S2** (Elysium wipe), **Super Poly** on Dragoon (Tip T2), or **Forbidden Droplet** (doesn't target)",
    "**Ghost Ogre** can't touch Shining Sarcophagus. Nothing targets Dragoon"]),
   ("Jack (Cyber Dragon · Chimeratech)", [
    "**Chimeratech Fortress Dragon** sends Machines from **either** field: **Mechaba is a Machine**, so he can eat it",
    "Fortress is summoned by sending, not activated: **Baronne and Mechaba can't negate it**. Save negates for **Overload Fusion / Super Poly / Cyber Emergency**",
    "**Nibiru** and **Maxx \"C\"** punish his summon chains"]),
  ],
  end="Long line only into Natasha and Jack",
  memo="Timer: if under 60 seconds, stop extending and pass. A finished small board beats an unfinished big one.")

NEW_TIPS = [P1, P2, P3, P4, P5]
for _i, _L in enumerate(NEW_TIPS, 1):
    _L["id"] = "T" + str(_i)
    _L["when"] = "tips"

LINES = NEW_FIRST + NEW_SECOND + NEW_TIPS + OLD

INDEX1 = [
 ("Aleister + Reminiscent", "1", True),
 ("Aleister + Sacred Sword or Aiwass (they search Reminiscent)", "1", True),
 ("Sacred Sword / Meltdown / Aiwass + Reminiscent", "2", True),
 ("Aleister + Ash / Droll / Fuwalos", "3", False),
 ("Sacred Sword / Meltdown / Aiwass + FIRE/WIND", "4", False),
 ("Reminiscent alone", "5", False),
 ("Aleister + any card", "6", False),
 ("Sacred Sword / Meltdown / Aiwass + any card", "7", False),
 ("Got Drolled after Aleister's search (Droll in her GY is WIND)", "3", False),
 ("Got Drolled after Reminiscent's search", "5", False),
 ("Got Drolled before Invocation (opener's search hit)", "8", False),
 ("No starter at all (brick)", "9", False),
]
INDEX2 = [
 ("Aleister or opener + Reminiscent", "S1", True),
 ("Aleister or opener + FIRE/WIND + Super Poly (her Extra Deck monster)", "S2", True),
 ("Aleister or opener + Super Poly (she has a Fusion)", "S3", True),
 ("Reminiscent alone", "S4", False),
 ("Aleister or opener + FIRE/WIND", "S5", False),
 ("Aleister or opener + any card", "S6", False),
]
INDEX3 = [
 ("Her turn: which hand trap, when", "T1", False),
 ("Going 2nd into Natasha's Dragoon", "T2", False),
 ("Finish the turn: damage tricks and attack values", "T3", False),
 ("Borreload Savage Dragon instead of Baronne", "T4", False),
 ("Saturday gauntlet: Labrynth, Natasha, Jack", "T5", True),
]
INDEX4 = [((("1st: " if L["old_when"] == "1st" else "2nd: " if L["old_when"] == "2nd" else "Tip: ") + L["title"]), L["id"], False) for L in OLD]
INDEX = INDEX1
RULES = [
 "Baybarron: say SKIP to the banish unless you've picked a target",
 "Madness needs a spare card to discard. Keep one",
 "Madness needs 2 monsters with different Types AND Attributes. Baybarron + Virakam are both Illusion: no",
 "Before any Link: is there a free zone? With Madness in the Extra Monster Zone, the next Link goes where its arrows point (down-left, down-right). Keep one of those empty",
 "Oceanus goes in the Extra Monster Zone",
 "Read both GYs + banishment before Invocation. Invocation can use a FIRE/WIND (or any) monster from EITHER GY: use that before spending a card from hand",
 "Sacred Sword and Aiwass search any \"Aleister\" monster. Aleister already in hand? Take Reminiscent",
 "Discard order: dead copies (2nd Meltdown, 2nd Sacred Sword) → Fuwalos/Purulia → Imperm → Crossout → Ghost Ogre. KEEP Maxx \"C\", Ash, Super Poly, Droll",
 "Mechaba: keep 1 monster + 1 Spell/Trap in hand if you can",
 "Imperm on Aleister: it keeps its name (Invocation still works). Search stopped but Invocation in hand? Play the line unchanged",
 "Main Phase 2: link 2 spare small monsters into S:P Little Knight. It's an interruption on her turn",
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
