# EDOPro practice puzzles

Natasha's Horus Dragoon end board (a best guess from her 9 Nov decklist on the wiki) against Lewis's Yummy Dragoon, one file per opening hand.

**Her board (v2, 20 Nov):** Red-Eyes Dark Dragoon (Extra Monster Zone), Imsety, Duamutef, Qebehsenuef, Hapi · King's Sarcophagus, Shining Sarcophagus, set Future Silence, Walls of the Imperial Tomb · hand: Horus the Black Flame Deity (summons itself when a Son leaves the field), Ash, Droll, Dark Magician. `generate_natasha.py` rebuilds the files (needs ids.json of card IDs).

**Install:** copy the `.lua` files into EDOPro's `puzzles` folder, then open **Puzzles** in EDOPro. To change her board or your hand, use EDOPro's built-in **Puzzle Creator** puzzle.

Built 20 Nov 2026 with Project Ignis puzzle format (Master Rule 5). UNTESTED in EDOPro.

## v4: PredaRikka vs Natasha (21 Nov 2026)

`generate_natasha_rikka.py` → `v4/` and `Natasha_PredaRikka_puzzles_v4.zip`. Deck = the vs-Natasha PredaRikka list on the [Rikka](../../Writerside/topics/Master-duel/Rikka.md) page.

- **Going 1st drills (5):** one proven starter each (Predaprimitive, Instant Fusion, Moonlit Waters = Line A, Black Princess + Plant = Line B, Glamour → Petal). The proven line is in the puzzle message. She holds Imsety, Walls, Dark Hole, Forbidden Droplet and Ash, so your board gets tested on her turn.
- **Going 2nd (10):** random hands into her full end board; hand traps in your opening hand are treated as used on her turn.

UNTESTED in EDOPro. Card IDs cached in `ids_rikka.json`.
