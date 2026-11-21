# Tournament decks (21 Nov 2026)

Which deck to play against each player at Lewis's home tournament, and what to change for that match. All 40 deck slots are full, so the plan uses **edits to existing decks**, not new ones. Live answers for each board are on the [Speed sheet](Speed-sheet.md).

## Summary

| Opponent | Deck | Changes |
| --- | --- | --- |
| **Rhino** (HERO) | **Invoked** | −2 Mulcharmy Purulia, −1 Crossout Designator, **+3 Forbidden Droplet** |
| **Natasha** (Horus · Dragoon) | **InvokedVsNatasha** | None needed. Optional: −2 Meowls, −1 Triple Tactics Thrust, +3 Forbidden Droplet |
| **Jack** (Cyber Dragon) | **Witchcrafter** | None |
| **Luke** (budget Sky Striker) | **Invoked** (practice) | None. He started Sky Striker on 21 Nov, so use the match to practise the Invoked lines you need for Rhino and Natasha |

Lewis owns 3 Forbidden Droplet, and the same card can sit in several decks.

**If you'd rather play one deck all day:** play Invoked against everyone (with the Rhino changes). You lose Witchcrafter's lower brick rate against Jack and Luke, but you keep one set of lines in your head.

## Rhino: Invoked + 3 Droplet

Same model as the [Natasha](Natasha.md) simulations: 30,000 random hands going second into his board (Chaos ×2, Sunrise, Dark Law). Full break %, with your hand traps working fully / half / not at all on his turn.

| Build | Full break % |
| --- | --- |
| Invoked (current) | 73 / 35 / 4 |
| +2 Droplet, −2 Ghost Ogre | 72 / 43 / 12 |
| +3 Droplet, −2 Ghost Ogre, −1 Crossout | 76 / 48 / 15 |
| **+3 Droplet, −2 Purulia, −1 Crossout** | **78 / 52 / 15** |
| +3 Droplet, −2 Ghost Ogre, −1 Maxx "C" | 74 / 48 / 15 |
| Witchcrafter (current) | 22 / 14 / 6 |
| Witchcrafter +2 Droplet, +1 Spell Power Mastery | 34 / 24 / 12 |

- **Why Droplet:** send a monster and he can't respond with a monster effect, so neither Chaos can stop it. It negates Dark Law and a Chaos without targeting.
- **Why Invoked over Witchcrafter here:** Witchcrafter runs through Walpurgis, and Chaos negates it. Dark Law also banishes everything Witchcrafter sends to the GY. Invoked has 2 Super Poly (no responses) and about 18 interaction cards.
- **New Main Deck (40):** Droll 2, Maxx "C" 1, Ghost Ogre 2, Ash 3, Virakam 1, Aleister 3, Fuwalos 3, Reminiscent 3, Aiwass 3, Invocation 2, Triple Tactics Talent 1, Sacred Spirit Sword Aiwass 3, Magical Meltdown 3, Super Polymerization 2, Invocation "Sword" 2, Infinite Impermanence 3, **Forbidden Droplet 3**.

## Natasha: InvokedVsNatasha

| Build | Full break % |
| --- | --- |
| Invoked (normal) | 30 / 29 / 24 |
| **InvokedVsNatasha** (Lewis's) | **35 / 34 / 31** |
| InvokedVsNatasha −2 Meowls, −TT Thrust, +3 Droplet | 36 / 35 / 33 |

- The Droplet swap gains 1–2 points, which is within the model's noise. Keep your list unless you want Droplet's non-targeting negate for Dragoon.
- Going first: Line 1, then **Imperm Imsety** on her turn. Going second: **Tip T2** (Super Poly on Dragoon). Both are in the [Invoked practice sheet](Invoked-practice.md).

## Jack: Witchcrafter

- **Record:** won going first against KHAOTICA's Cyber Dragon (21 Nov), with the full main line.
- **Brick rate going first:** Witchcrafter 10.2%, Invoked 14.9%.
- **Fewer Machines:** none of Witchcrafter's monsters are Machines unless Clockwork Night is up. Invoked's Mechaba is a Machine, and Chimeratech Fortress can eat it.
- **Keep:** Maxx "C" and Fuwalos. Cyber Dragon Special Summons a lot.
- **Watch:** Clockwork Night (destroy it first), Infinity's negate (bait it), and your Links in the Extra Monster Zone (Megafleet material).

## Luke: any deck (use it as Invoked practice)

Luke started Sky Striker on 21 Nov and isn't a threat. Play Invoked against him to rehearse Line 1 and the going-second lines before the Rhino and Natasha matches. Witchcrafter notes below in case you play it anyway.


- **Record:** 3–0 against him.
- **Keep Maxx "C".** Every Sky Striker Link, token and Zero is a Special Summon, so it still draws several cards. (An earlier version of this page suggested cutting it; that was wrong.)
- **If you want Droplet in:** cut Fuwalos and 1 Lacrima, not Maxx "C". Droplet with a monster sent stops Zero's Quick Effect from responding. **UNTESTED**
- **Watch:** Widow Anchor (bait it), and keep a monster on his side when you can: his Sky Striker Spells need an empty Main Monster Zone.

## How the numbers were made

Script: `tools/deck-sim/full.py`, the resource-exchange model from the [Natasha](Natasha.md) page. It isn't a game engine: each card gets a role from its text, the opponent uses its interruptions where they hurt most, and the model picks the best use of your hand traps. Use it to compare builds, not as a win rate.
