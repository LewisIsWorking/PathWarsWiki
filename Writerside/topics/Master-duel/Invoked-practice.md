# Invoked practice sheet

Lines to learn before the 21 Nov tournament so you can play them from memory under the timer. Every line only uses cards Lewis owns.

- **Sourced** lines come from Taffy's [Invoked combo spreadsheet](https://www.masterduelmeta.com/spreadsheet/6ac95807501c79d600eec076) on Master Duel Meta (Sept–Oct 2026) and are copied step for step.
- **Untested** lines were built from card text by Claude. Each step was checked against the card, but nobody has played them in a tournament.
- Chorozo crafted 14 Nov, so Line 1 now uses Taffy's Baronne branch.

## Cheat sheet images

One image per line, for your phone during games. **Easier on a phone:** the one-page version at https://claude.ai/artifact/QN9EBixbg3USELrswv3fw3 always shows the latest lines (add it to your home screen). **Current version: v2.5 (15 Nov 2026).** Version and date are printed in each image's footer.

To update: edit the line data in `tools/invoked-cheatsheet/build.py`, bump `VERSION` and `DATE`, run `python3 tools/invoked-cheatsheet/build.py` from the repo root, point the links below at the new folder, and add a changelog entry. Older versions stay in their own folders.

### Changelog

- **v2.5 (15 Nov 2026):** new going-1st Line 13 "Drolled before you got Invocation" (untested): Virakam Sets Invocation, Droll in her GY is the WIND for Sorath. Brick is now Line 14.
- **v2.4 (15 Nov 2026):** new going-1st Line 7 "Opener + Spenta + Crowley" (untested). Old Lines 7–12 are now 8–13.
- **v2.3 (14 Nov 2026):** new going-2nd Line S2 "Aleister's search stopped + Reminiscent + Invocation" (S1 written out for when Aleister is Imperm'd or Ash'd). Old S2–S8 are now S3–S9.
- **v2.2 (14 Nov 2026):** S1 and the Imperm golden rule now say: if Aleister's search is stopped but you already hold an Invocation, play the line unchanged.
- **v2.1 (14 Nov 2026):** the hand-trap timing line moved from going-2nd S1 to Tip T1. Going-2nd lines renumbered S1–S8 (old S2 → S1, etc.); tips are now T1–T5.
- **v2.0 (14 Nov 2026):** the sheet is now built for the **ranked deck (InvokedRD)**. Planet Run is secondary: its differences (no Zoroa, no Ghost Ogre) are in Tip T4.
- **v1.16 (14 Nov 2026):** golden rule: in Main Phase 2, link 2 spare small monsters into S:P Little Knight for an interruption on her turn.
- **v1.15 (14 Nov 2026):** new Tip T3 "Clear her board with Aeon": Grail mode 1 makes a second Fusion from hand + Deck, then Invocation turns both into Aeon. Untested.
- **v1.14 (14 Nov 2026):** golden rule 5 now says to use GY monsters as Invocation material before hand cards (Lewis spent Ash when Fuwalos was already in the GY).
- **v1.13 (14 Nov 2026):** new going-2nd Line S9 "Aleister got Imperm'd + FIRE/WIND + Grail" (untested) and a golden rule: Imperm on Aleister leaves its name, so Invocation and Grail still work; Imperm on Crowley stops it counting as Aleister.
- **v1.12 (14 Nov 2026):** new going-2nd Line S4 "Aleister or opener + FIRE/WIND + Grail" (untested). Old S4–S7 are now S5–S8.
- **v1.11 (14 Nov 2026):** new going-2nd Line S6 "Spenta or Crowley + FIRE/WIND + Grail + Invocation" (untested). The Spenta Invoke Sword line is now S7 and also starts from a Crowley in hand. Natasha's Dragoon plan and the finishers moved to a new **Tips & tricks** list (T1, T2).
- **v1.10 (14 Nov 2026):** new going-2nd Line S6 "Spenta + FIRE/WIND + Invocation + Invoke Sword" (no Aleister needed; ends on Aeon). Untested. Old S6–S7 are now S7–S8.
- **v1.9 (14 Nov 2026):** added going-1st Line 12 "No starter: pass with hand traps" for brick hands.
- **v1.8 (14 Nov 2026):** fixed S3. The old finish needed an Aleister for Oceanus, but the line leaves Aleister unavailable; it now finishes with Invocation → **Aeon from Sorath + Chorozo in the GY** (what won the Solo game), plus an optional Invoke Sword → Raidjin.
- **v1.7 (14 Nov 2026):** new going-2nd Line S3 "Super Poly into Chorozo", found live by Lewis vs Exosister: Super Poly her Extra Deck monster + her Spellcaster into Magistus Chorozo; Artemis equips to it and searches Crowley. Old S3–S6 are now S4–S7.
- **v1.6 (14 Nov 2026):** both lists ordered strictly by end-board strength, so the first line your hand can do is the best one. Swapped Lines 3 and 4: Crowley/Spenta + Reminiscent + FIRE/WIND (Oceanus, Little Knight, Aeon, Virakam, Invoke Sword) is now Line 3, above Reminiscent alone (Line 4).
- **v1.5 (14 Nov 2026):** split into **Going 1st** (Lines 1–11) and **Going 2nd** (Lines S1–S6). New going-2nd lines: S1 hand-trap timing on her turn, S2 Reminiscent line kept for 13,300 damage, S3/S4 with **Super Poly** built in. Names standardised: **Invoke Sword** (Invocation "Sword") and **Sacred Sword** (Sacred Spirit Sword Aiwass). `page.py` now also rewrites the line sections and hand table on this page.
- **v1.4 (14 Nov 2026):** every hand now has its own complete line, with no "continue from Line X". The opener (Sacred Spirit Sword / Meltdown / Aiwass) is built into Lines 2, 6 and 8. 13 lines. Line sections on this page are now generated from the same data as the images and phone page.
- **v1.3 (14 Nov 2026):** lines renumbered so the picker reads 1 → 11 top to bottom (old numbers: 4→1, 6→2, 3→3, 5→4, 1→5, 2→6, 7→7, 9→8, 10→9, 8→10, 11→11). The two opener rows are merged into Line 2. Entries below have been updated to the new numbers.
- **v1.2 (14 Nov 2026):** added Line 8 (Aleister got Drolled) and Line 9 (Reminiscent got Drolled) from Taffy, both now possible with Chorozo; Line 11 going-second finishers (spare Sword → Omega, Super Poly with Madness, damage tricks, attack values). Line 5 notes the Omega finish.
- **v1.1 (14 Nov 2026):** added a discard priority and a Mechaba hand rule to the "Which line?" golden rules.
- **v1.0 (14 Nov 2026):** first version. Lines 1–8 plus the "Which line?" picker. Line 1 is Taffy's Baronne branch (Chorozo crafted). Deck: 1 Reminiscent, 2 Aiwass, 2 Spenta, 1 Crowley, 1 Zoroa, Omega + 1 Aeon + De Anima in the Extra Deck.
- **Planned:** add Elysium to Line 4 and the going-second plan once crafted; add Gamma Summon; recheck lines when Reminiscent #2–3 arrive.

![invoked-0-which-line](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-0-which-line.png)
![invoked-line-1](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-1.png)
![invoked-line-2](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-2.png)
![invoked-line-3](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-3.png)
![invoked-line-4](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-4.png)
![invoked-line-5](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-5.png)
![invoked-line-6](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-6.png)
![invoked-line-7](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-7.png)
![invoked-line-8](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-8.png)
![invoked-line-9](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-9.png)
![invoked-line-10](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-10.png)
![invoked-line-11](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-11.png)
![invoked-line-12](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-12.png)
![invoked-line-13](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-13.png)
![invoked-line-14](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-14.png)
![invoked-line-S1](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S1.png)
![invoked-line-S2](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S2.png)
![invoked-line-S3](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S3.png)
![invoked-line-S4](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S4.png)
![invoked-line-S5](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S5.png)
![invoked-line-S6](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S6.png)
![invoked-line-S7](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S7.png)
![invoked-line-S8](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S8.png)
![invoked-line-S9](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-S9.png)
![invoked-line-T1](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-T1.png)
![invoked-line-T2](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-T2.png)
![invoked-line-T3](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-T3.png)
![invoked-line-T4](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-T4.png)
![invoked-line-T5](https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v2.5/invoked-line-T5.png)

Which line to play:

| Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Going | Your hand has | Play |
| --- | --- | --- |
| 1st | Aleister + Reminiscent | Line 1 (best) |
| 1st | Sacred Sword / Meltdown / Aiwass + Reminiscent | Line 2 (best) |
| 1st | Crowley or Spenta + Reminiscent + FIRE/WIND | Line 3 |
| 1st | Reminiscent alone | Line 4 |
| 1st | Aleister + Ash / Droll / Fuwalos / Zoroa | Line 5 |
| 1st | Sacred Sword / Meltdown / Aiwass + FIRE/WIND | Line 6 |
| 1st | Sacred Sword / Meltdown / Aiwass + Spenta + Crowley | Line 7 |
| 1st | Aleister + any card | Line 8 |
| 1st | Sacred Sword / Meltdown / Aiwass + any card | Line 9 |
| 1st | Zoroa or Spenta, no Aleister | Line 10 |
| 1st | Got Drolled after Aleister's search | Line 11 |
| 1st | Got Drolled after Reminiscent's search | Line 12 |
| 1st | Got Drolled before Invocation (Aiwass/Meltdown search hit) | Line 13 |
| 1st | No starter at all (brick) | Line 14 |
| 2nd | Aleister or opener + Reminiscent | Line S1 (best) |
| 2nd | Aleister's search Imperm'd/Ash'd + Reminiscent + Invocation | Line S2 (best) |
| 2nd | Super Poly: she has an Extra Deck monster + a Spellcaster | Line S3 (best) |
| 2nd | Aleister or opener + FIRE/WIND + Grail | Line S4 (best) |
| 2nd | Aleister or opener + FIRE/WIND + Super Poly | Line S5 (best) |
| 2nd | Aleister or opener + any card + Super Poly | Line S6 |
| 2nd | Spenta or Crowley + FIRE/WIND + Grail + Invocation | Line S7 |
| 2nd | Spenta or Crowley + FIRE/WIND + Invocation + Invoke Sword | Line S8 |
| 2nd | Aleister got Imperm'd + FIRE/WIND + Grail | Line S9 |
| tips | Her turn: which hand trap, when | Line T1 |
| tips | Going 2nd into Natasha's Dragoon | Line T2 |
| tips | Finish the turn: damage tricks and attack values | Line T3 |
| tips | Clear her board with Aeon (no Normal Summon left) | Line T4 |
| tips | Planet Run deck: what's different | Line T5 |

## Line 1: Aleister + Reminiscent (going 1st; Sourced: Taffy (MDM), Baronne branch · BEST LINE)

Needs: Aleister (or Meltdown / Aiwass / Sacred Sword), Reminiscent, +1 spare card.

**1 · Two Links into Crowley**
1. Normal Summon Aleister → search **Invocation**
2. Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**
3. Link Aleister → **Artemis**
4. Link Artemis + Reminiscent → **Endymion**, equip Artemis
5. Artemis: search **Crowley** (summons itself). DON'T FUSE

**2 · Chorozo, Baybarron, Sorath**
6. Endymion + Artemis → **Chorozo** (contact fusion)
7. Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish
8. Special Summon Virakam → set **Invoke Sword**
9. Invoke Sword (hand): Aleister + Raidjin (banished) → **Sorath**

**3 · Baronne and Madness**
10. Link Baybarron + Crowley → **Madness**
11. Sorath: revive Crowley
12. Synchro: Chorozo + Sorath → **Baronne de Fleur**

**4 · Aeon finish**
13. Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**
14. Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)
15. Link Aeon + Crowley → **Little Knight**
16. Invoke Sword GY: add Invocation
17. Invocation: Aleister + Endymion (GY) → **Mechaba**
18. Invocation: Madness + Crowley → **Oceanus** (Extra Monster Zone)
19. Invocation GY: add a banished Aleister

**End:** Baronne · Mechaba · Oceanus (EMZ) · Little Knight · Virakam · set Invoke Sword · Aleister in hand · up to 6 of hers banished

**Remember:** Raidjin used 3× (cost → Invoke Sword → Aeon). Crowley used 3× (Madness → Little Knight → Oceanus).

## Line 2: Opener + Reminiscent (going 1st; Sourced: Taffy (MDM), Baronne branch · BEST LINE · opener: Dawnstar (MDM))

Needs: Sacred Sword, Meltdown or Aiwass, Reminiscent, +1 spare card.

**Get Aleister**
1. **Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister** (Aiwass gives you an extra Normal Summon). With **Meltdown** or **Aiwass in hand**, just search Aleister

**1 · Two Links into Crowley**
2. Normal Summon Aleister → search **Invocation**
3. Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**
4. Link Aleister → **Artemis**
5. Link Artemis + Reminiscent → **Endymion**, equip Artemis
6. Artemis: search **Crowley** (summons itself). DON'T FUSE

**2 · Chorozo, Baybarron, Sorath**
7. Endymion + Artemis → **Chorozo** (contact fusion)
8. Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish
9. Special Summon Virakam → set **Invoke Sword**
10. Invoke Sword (hand): Aleister + Raidjin (banished) → **Sorath**

**3 · Baronne and Madness**
11. Link Baybarron + Crowley → **Madness**
12. Sorath: revive Crowley
13. Synchro: Chorozo + Sorath → **Baronne de Fleur**

**4 · Aeon finish**
14. Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**
15. Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)
16. Link Aeon + Crowley → **Little Knight**
17. Invoke Sword GY: add Invocation
18. Invocation: Aleister + Endymion (GY) → **Mechaba**
19. Invocation: Madness + Crowley → **Oceanus** (Extra Monster Zone)
20. Invocation GY: add a banished Aleister

**End:** Baronne · Mechaba · Oceanus (EMZ) · Little Knight · Virakam · set Invoke Sword · Aleister in hand · up to 6 of hers banished

**Remember:** Raidjin used 3× (cost → Invoke Sword → Aeon). Crowley used 3× (Madness → Little Knight → Oceanus). Sacred Sword: only Fusions can attack this turn.

## Line 3: Crowley or Spenta + Reminiscent + FIRE/WIND (going 1st; Sourced: Taffy (MDM))

Needs: Crowley (Normal Summon) or Spenta (discard → Crowley), Reminiscent, FIRE/WIND monster, +1 spare card.

**Sorath and Madness**
1. Crowley: Crowley + FIRE/WIND (hand) → **Sorath**
2. Sorath: revive Crowley
3. Reminiscent: target Sorath, summon itself; banish **Raidjin** → search **Invoke Sword**
4. Link Reminiscent + Sorath → **Madness**
5. Sorath GY: Reminiscent + Sorath → **Baybarron**
6. Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**)

**Aeon finish**
7. Link Baybarron + Crowley → **Little Knight**: banish Baybarron from your GY
8. Special Summon Virakam → set **Invoke Sword**
9. Invoke Sword: Baybarron + Sorath + Raidjin (banished) → **Aeon**
10. Aeon: banish up to 3 of hers, then pick 3 from her Extra Deck
11. Invoke Sword GY: add Invocation
12. Invocation: Crowley + Madness → **Oceanus** (Extra Monster Zone)

**End:** Oceanus (EMZ) · Little Knight · Aeon · Virakam · set Invoke Sword

**Remember:** Taffy makes Elysium after Aeon. Add that step once you own Elysium.

## Line 4: Reminiscent alone (going 1st; Sourced: Taffy (MDM))

Needs: Reminiscent, +1 spare card.

**Raidjin loop into Sorath**
1. Normal Summon Reminiscent: banish **Raidjin** (Extra Deck) → search **Invoke Sword**
2. Invoke Sword: Reminiscent + Raidjin (banished) → **Sorath**
3. Sorath: revive Reminiscent
4. Link Reminiscent → **Artemis**
5. Invoke Sword GY: add Reminiscent to hand
6. Reminiscent (hand): target Sorath → Special Summon itself

**Crowley into Baybarron**
7. Link Artemis + Reminiscent → **Endymion**, equip Artemis
8. Artemis: search **Crowley** (it summons itself)
9. Crowley: Crowley + Endymion → **Baybarron**
10. Baybarron: search **Virakam**, SKIP the banish
11. Special Summon Virakam → set **Invoke Sword**

**Aeon finish**
12. Link Sorath + Baybarron → **Madness**
13. Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**
14. Chain: Madness (discard spare → **Invocation**) + Aeon (banish up to 3, then pick 3 from her Extra Deck)
15. Link Aeon + Virakam → **Little Knight**
16. Invocation: Madness + Aeon (GY) → **Oceanus** (Extra Monster Zone)

**End:** Oceanus (EMZ) · Little Knight · set Invoke Sword · up to 6 of hers banished

## Line 5: Aleister + FIRE/WIND (going 1st; Sourced: Taffy (MDM))

Needs: Aleister, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, +1 spare card.

**Get Sorath**
1. Normal Summon Aleister → search **Invocation**
2. Link Aleister → **Artemis**
3. Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**
4. Invocation GY: add the banished Aleister
5. Discard Aleister on Sorath (+1000)
6. Sorath: revive Aleister

**Crowley into Baybarron**
7. Link Aleister + Artemis → **Endymion**, equip Artemis
8. Artemis: search **Crowley** (it summons itself)
9. Crowley: Crowley + Endymion → **Baybarron**
10. Baybarron: search **Virakam**, SKIP the banish
11. Special Summon Virakam → set **Invoke Sword**

**Finish**
12. Link Sorath + Baybarron → **Madness**
13. Sorath GY: Sorath + Aleister → **Mechaba**
14. Madness: discard spare → search **Invocation**
15. Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)

**End:** Oceanus (EMZ) · Mechaba · Virakam · set Invoke Sword

**Remember:** Going 2nd with a 2nd Invoke Sword in hand? Don't discard it at step 15: see Tip T3 for the finishers.

## Line 6: Opener + FIRE/WIND (going 1st; Sourced: Taffy (MDM) · opener: Dawnstar (MDM))

Needs: Sacred Sword, Meltdown or Aiwass, FIRE/WIND (an Aiwass in hand counts: WIND), +1 spare card.

**Get Aleister**
1. **Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister** (Aiwass gives you an extra Normal Summon). With **Meltdown** or **Aiwass in hand**, just search Aleister

**Get Sorath**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Artemis**
4. Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath (+1000)
7. Sorath: revive Aleister

**Crowley into Baybarron**
8. Link Aleister + Artemis → **Endymion**, equip Artemis
9. Artemis: search **Crowley** (it summons itself)
10. Crowley: Crowley + Endymion → **Baybarron**
11. Baybarron: search **Virakam**, SKIP the banish
12. Special Summon Virakam → set **Invoke Sword**

**Finish**
13. Link Sorath + Baybarron → **Madness**
14. Sorath GY: Sorath + Aleister → **Mechaba**
15. Madness: discard spare → search **Invocation**
16. Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)

**End:** Oceanus (EMZ) · Mechaba · Virakam · set Invoke Sword

**Remember:** Going 2nd with a 2nd Invoke Sword in hand? Don't discard it at step 15: see Tip T3 for the finishers. Sacred Sword: only Fusions can attack this turn. If Sacred Sword opened, an Aiwass in hand is your WIND monster.

## Line 7: Opener + Spenta + Crowley (going 1st; Going 1st · Line 6 with Spenta finding the FIRE · UNTESTED, built from card text)

Needs: Sacred Sword (or Meltdown / Aiwass), Spenta, Crowley, +1 spare card (Spenta #2 from Artemis covers it).

**Get Aleister and Zoroa**
1. **Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister**, Normal Summon it straight away → search **Invocation**
2. **Spenta:** discard → search **Zoroa** (FIRE)

**Get Sorath**
3. Link Aleister → **Artemis**
4. Invocation: Aleister (GY) + Zoroa (hand) → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath → Sorath revives Aleister

**Crowley into Baybarron**
7. Link Aleister + Artemis → **Endymion**, equip Artemis
8. Artemis: search **Spenta #2**
9. **Normal Summon Crowley:** Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish
10. Special Summon Virakam → set **Invoke Sword**

**Finish**
11. Link Sorath + Baybarron → **Madness**
12. Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard Spenta #2 → search **Invocation**
13. Invocation: Madness + Crowley (GY) → **Oceanus** (Extra Monster Zone)

**End:** Oceanus (EMZ) · Mechaba · Virakam · set Invoke Sword · Nibiru/Grail etc. still in hand

**Remember:** If the game won't let you Normal Summon Crowley (Aiwass's summon may use up your Normal Summon): skip Endymion, Link Aleister + Sorath → Madness, Sorath GY: Sorath + Aleister → Baybarron (search Virakam), Madness discards Crowley → Invocation, Virakam → Invoke Sword, Invocation: Madness + Virakam → Mechaba.

## Line 8: Aleister + any card (going 1st; Sourced: Taffy (MDM) · weakest line)

Needs: Aleister, +1 spare card.

**Get Sorath**
1. Normal Summon Aleister → search **Invocation**
2. Link Aleister → **Almiraj**
3. Invocation: Aleister + Almiraj → **Sorath**
4. Invocation GY: add the banished Aleister
5. Discard Aleister on Sorath
6. Sorath: revive Aleister

**Finish**
7. Link Aleister + Sorath → **Madness**
8. Sorath GY: Sorath + Aleister → **Baybarron**
9. Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**, skip banish)
10. Special Summon Virakam → set **Invoke Sword**
11. Link Virakam + Baybarron → **Little Knight**
12. Invocation: Madness + Virakam → **Mechaba**

**End:** Little Knight · Mechaba · set Invoke Sword

## Line 9: Opener + any card (going 1st; Sourced: Taffy (MDM) · weakest line · opener: Dawnstar (MDM))

Needs: Sacred Sword, Meltdown or Aiwass, +1 spare card.

**Get Aleister**
1. **Sacred Sword:** summon **Aiwass** from Deck → banish it → add **Aleister** (Aiwass gives you an extra Normal Summon). With **Meltdown** or **Aiwass in hand**, just search Aleister

**Get Sorath**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Almiraj**
4. Invocation: Aleister + Almiraj → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath
7. Sorath: revive Aleister

**Finish**
8. Link Aleister + Sorath → **Madness**
9. Sorath GY: Sorath + Aleister → **Baybarron**
10. Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**, skip banish)
11. Special Summon Virakam → set **Invoke Sword**
12. Link Virakam + Baybarron → **Little Knight**
13. Invocation: Madness + Virakam → **Mechaba**

**End:** Little Knight · Mechaba · set Invoke Sword

**Remember:** Sacred Sword: only Fusions can attack this turn.

## Line 10: Zoroa or Spenta, no Aleister (going 1st; UNTESTED · built from card text)

Needs: Zoroa, or Spenta (discard → Zoroa).

**Line**
1. Spenta (if held): discard → search **Zoroa**
2. Normal Summon Zoroa
3. Zoroa: target itself, equip **Artemis** from Extra Deck
4. Zoroa: Special Summon a Level 4 Spellcaster from hand/GY (Spenta)
5. Artemis: search **Crowley** (it summons itself)
6. Crowley + Zoroa (FIRE) → **Sorath**, or Crowley + Spenta (LIGHT) → **Mechaba**

**End:** 1 Fusion + a spare body. Turns a brick into a board.

## Line 11: Aleister got Drolled (going 1st; Sourced: Taffy (MDM) · needs Chorozo)

Needs: Aleister, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa.

**No more searches needed**
1. Normal Summon Aleister → search **Invocation** (Droll hits after this)
2. Link Aleister → **Artemis**
3. Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**
4. Invocation GY: add the banished Aleister (not from Deck, so Droll can't stop it)
5. Discard Aleister on Sorath → Sorath revives Aleister
6. Aleister + Artemis → **Chorozo**
7. Synchro: Chorozo + Sorath → **Baronne de Fleur**
8. Sorath GY: Sorath + Aleister → **Mechaba**

**End:** Baronne · Mechaba

## Line 12: Reminiscent got Drolled (going 1st; Sourced: Taffy (MDM) · needs Chorozo)

Needs: Reminiscent.

**No more searches needed**
1. Normal Summon Reminiscent: banish **Raidjin** → search **Invoke Sword** (Droll hits after this)
2. Invoke Sword: Reminiscent + Raidjin (banished) → **Sorath**
3. Sorath: revive Reminiscent
4. Link Reminiscent → **Artemis**
5. Invoke Sword GY: add Reminiscent (from GY, Droll can't stop it)
6. Reminiscent: target Sorath → Special Summon itself
7. Reminiscent + Artemis → **Chorozo**
8. Synchro: Chorozo + Sorath → **Baronne de Fleur**
9. Sorath GY: Sorath + Raidjin + Chorozo → **Aeon** (banish up to 3, pick 3 from her Extra Deck)

**End:** Baronne · Aeon · up to 6 of hers banished

## Line 13: Drolled before you got Invocation (going 1st; Going 1st · e.g. Aiwass/Meltdown search got Drolled · UNTESTED, built from card text)

Needs: Aleister (on hand or field), Virakam, or Invocation already in hand, Droll in her GY (it's WIND), Reminiscent helps (+ body).

**Droll rules**
1. Droll blocks **adding from Deck to hand** (draws too). It does NOT block **Setting** from Deck, or adding from GY/banishment
2. **TTT:** don't pick Draw 2. Pick look at her hand + shuffle 1 away

**Get Sorath**
3. Normal Summon Aleister. **SKIP** its search
4. **Virakam:** Special Summon → **Set Invocation** from Deck (Normal Spell: usable this turn). Skip if Invocation is in hand
5. Link Aleister → **Artemis**
6. **Invocation:** Aleister (your GY) + **Droll (her GY, WIND)** → **Sorath**
7. Invocation GY: add banished Aleister (from banishment: Droll can't stop it)
8. Discard Aleister on Sorath → Sorath revives Aleister

**Baronne and Mechaba**
9. **Reminiscent:** target Sorath → Special Summon itself. **SKIP** its search
10. Aleister + Artemis → **Chorozo**
11. Synchro: Chorozo + Sorath → **Baronne de Fleur**
12. Sorath GY: Sorath + Aleister → **Mechaba**

**End:** Baronne · Mechaba · Virakam · Reminiscent

**Remember:** No Virakam/Invocation/Grail/Crowley: NS Aleister (skip search), Reminiscent targets Aleister (skip search), Link Aleister → Artemis, Artemis + Reminiscent → S:P Little Knight. One interruption.

## Line 14: No starter: pass with hand traps (going 1st; Going 1st · brick hand · card text)

Needs: No Aleister, Reminiscent, Meltdown, Aiwass, Sacred Sword, Spenta, Crowley or Zoroa.

**Your turn**
1. **Don't summon or set anything.** Fuwalos and Imperm from hand only work while you control no cards
2. End your turn

**Her turn**
3. **Fuwalos:** early in her Main Phase. Draw 1 for each Deck/Extra Deck summon, to find a starter
4. **Maxx "C":** her first Special Summon. **Ash / Droll / Imperm / Ghost Belle / Ghost Ogre:** see Line S1
5. **Nibiru:** after her 5th summon this turn, tributes her whole board
6. Fuwalos and Droll don't mix: Droll blocks your Fuwalos draws

**Your next turn**
7. Play the best line your new hand fits
8. **TTT:** live if she activated a monster effect during your turn (e.g. a hand trap on you)

**End:** Nothing on board, but a full hand of interaction

**Remember:** Don't Normal Summon Fuwalos or Nibiru: they're worth far more in hand.

## Line S1: Aleister or opener + Reminiscent (going 2nd; Going 2nd · Taffy's Line 1 with going-2nd changes (marked))

Needs: Aleister, Meltdown or Aiwass, Reminiscent, +1 spare card.

**Get Aleister**
1. Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)

**1 · Two Links into Crowley**
2. Normal Summon Aleister → search **Invocation**
3. Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**
4. Link Aleister → **Artemis**
5. Link Artemis + Reminiscent → **Endymion**, equip Artemis
6. Artemis: search **Crowley** (summons itself). DON'T FUSE

**2 · Chorozo, Baybarron, Sorath**
7. Endymion + Artemis → **Chorozo** (contact fusion)
8. Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish
9. Special Summon Virakam → set **Invoke Sword**
10. Invoke Sword (hand): Aleister + Raidjin (banished) → **Sorath**

**3 · Baronne and Madness**
11. Link Baybarron + Crowley → **Madness**
12. Sorath: revive Crowley
13. Synchro: Chorozo + Sorath → **Baronne de Fleur**

**4 · Aeon finish**
14. Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**
15. Chain: Madness (discard spare → **Invocation**) + Aeon: banish her **3 best cards on the field**, then pick 3 from her Extra Deck
16. **Going-2nd change:** don't make Little Knight. Keep **Aeon** to attack
17. Invoke Sword GY: add Invocation
18. Invocation: Aleister + Endymion (GY) → **Mechaba**
19. Invocation: Madness + Crowley (both on field) → **Oceanus** (Extra Monster Zone)
20. **Baronne:** destroy 1 more of her cards (targets)
21. **Battle:** Aeon 3800 + Baronne 3000 + Oceanus 3000 + Mechaba 2500 + Virakam 1000 = **13,300**

**End:** Her field cleared, 13,300 damage if nothing stops it

**Remember:** Open with Meltdown or Aiwass from hand, not Sacred Sword. After Sacred Sword only Fusions can attack, so Baronne and Virakam couldn't. Aleister's search Ash'd or Imperm'd? With an Invocation already in hand, play the line unchanged (Imperm leaves its name, so it still targets for Reminiscent and works as material).

## Line S2: Aleister's search stopped + Reminiscent + Invocation (going 2nd; Going 2nd · S1 with Aleister Imperm'd or Ash'd · card text)

Needs: Aleister on field (search negated by Imperm/Ash), Reminiscent, Invocation already in hand, +1 spare card.

**1 · Two Links into Crowley**
1. Aleister's search was stopped: you already hold **Invocation**, so carry on
2. Reminiscent: target Aleister, summon itself; banish **Raidjin** → search **Invoke Sword**
3. Link Aleister → **Artemis**
4. Link Artemis + Reminiscent → **Endymion**, equip Artemis
5. Artemis: search **Crowley** (summons itself). DON'T FUSE

**2 · Chorozo, Baybarron, Sorath**
6. Endymion + Artemis → **Chorozo** (contact fusion)
7. Invocation: Aleister + Artemis (GY) → **Baybarron**, search **Virakam**, skip banish
8. Special Summon Virakam → set **Invoke Sword**
9. Invoke Sword (hand): Aleister + Raidjin (banished) → **Sorath**

**3 · Baronne and Madness**
10. Link Baybarron + Crowley → **Madness**
11. Sorath: revive Crowley
12. Synchro: Chorozo + Sorath → **Baronne de Fleur**

**4 · Aeon finish**
13. Sorath GY: Sorath + Baybarron + Raidjin → **Aeon**
14. Chain: Madness (discard spare → **Invocation**) + Aeon: banish her **3 best cards on the field**, then pick 3 from her Extra Deck
15. **Going-2nd change:** don't make Little Knight. Keep **Aeon** to attack
16. Invoke Sword GY: add Invocation
17. Invocation: Aleister + Endymion (GY) → **Mechaba**
18. Invocation: Madness + Crowley (both on field) → **Oceanus** (Extra Monster Zone)
19. **Baronne:** destroy 1 more of her cards (targets)
20. **Battle:** Aeon 3800 + Baronne 3000 + Oceanus 3000 + Mechaba 2500 + Virakam 1000 = **13,300**

**End:** Her field cleared, 13,300 damage if nothing stops it

**Remember:** Imperm doesn't change Aleister's name: Reminiscent can still target it and it still counts as Aleister for Fusions. If Imperm was SET, it also negates Spell/Trap effects in its column this turn: put your Spells in another column.

## Line S3: Super Poly into Chorozo: steal 2 (going 2nd; Going 2nd · found by Lewis, won with it in Solo 14 Nov · order checked against card text)

Needs: Aleister, Meltdown or Aiwass, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Super Poly, +1 spare card, She controls an Extra Deck monster (Fusion/Synchro/Xyz/Link) + a Spellcaster.

**Get Aleister**
1. **Aiwass from hand:** banish it → add **Aleister** (best: banished Aiwass is WIND material for the finish). Or Meltdown → Aleister

**Take her two monsters**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Artemis**
4. **Super Poly** (discard spare): her Extra Deck monster + her Spellcaster → **Chorozo**
5. Artemis: equip to Chorozo → search **Crowley**. It summons itself, then fuse: Crowley + FIRE/WIND (hand) → **Sorath**

**Baronne and Aeon**
6. Sorath: revive Crowley
7. Synchro: Chorozo + Sorath → **Baronne de Fleur**
8. Invocation: **Sorath + Chorozo (both in GY)** → **Aeon**: banish 2 of her cards
9. **Baronne:** destroy 1 more of her cards

**Finish**
10. **Invoke Sword in hand** (optional): Crowley (field) + Aiwass (banished, WIND) → **Raidjin**
11. **Battle:** Aeon 3800 + Baronne 3000 + Crowley 1800 = **8,600** (Raidjin instead of Crowley: 9,000)

**End:** Her 2 monsters gone + 3 more of her cards removed · Aeon · Baronne · Crowley or Raidjin

**Remember:** Aeon needs no Aleister: 2 Fusions with different Attributes from your GY are enough. Exosister and Dark Magician decks are full of Spellcasters.

## Line S4: Aleister or opener + FIRE/WIND + Grail (going 2nd; Going 2nd · Taffy's Aleister line + Grail · UNTESTED, built from card text)

Needs: Aleister, Meltdown or Aiwass, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Grail, Invocation or a spare card.

**Get Aleister**
1. Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)

**Get Sorath**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Artemis**
4. Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath → Sorath revives Aleister

**Crowley into Baybarron**
7. Link Aleister + Artemis → **Endymion**, equip Artemis
8. Artemis: search **Crowley** (it summons itself). Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish
9. Special Summon Virakam → set **Invoke Sword**

**Grail, then Aeon**
10. Link Sorath + Baybarron → **Madness**
11. Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard spare (TTT) → search **Invocation**
12. **Grail mode 2:** Madness + her best monster (tap it for its Attribute): DARK/WATER **Oceanus**, WIND **Raidjin**. LIGHT/EARTH/FIRE: use another of her monsters
13. **Invocation:** Mechaba + the Grail Fusion → **Aeon**: banish her other monster + her set card
14. **Battle:** Aeon 3800 + Virakam 1000

**End:** Her 3 cards gone · Aeon · Virakam · set Invoke Sword

**Remember:** Grail doesn't target, so it gets round Dragoon.

## Line S5: Aleister or opener + FIRE/WIND + Super Poly (going 2nd; Going 2nd · Taffy's Aleister line + Super Poly (card text))

Needs: Aleister, Meltdown or Aiwass, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Super Poly, +2 spare cards.

**Get Aleister**
1. Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)

**Get Sorath**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Artemis**
4. Invocation: Aleister (GY) + FIRE/WIND (hand) → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath → Sorath revives Aleister

**Crowley into Baybarron**
7. Link Aleister + Artemis → **Endymion**, equip Artemis
8. Artemis: search **Crowley** (it summons itself)
9. Crowley + Endymion → **Baybarron**: search **Virakam**, SKIP the banish
10. Special Summon Virakam → set **Invoke Sword**

**Break her board**
11. Link Sorath + Baybarron → **Madness**
12. Sorath GY: Sorath + Aleister → **Mechaba**. Madness: discard spare → search **Invocation**
13. **Super Poly** (discard spare): Madness + her best monster → by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**
14. Invocation: Madness (GY) + Crowley (GY) → **Oceanus** (EMZ). If Super Poly made Oceanus, keep this Invocation
15. **Invoke Sword in hand** (Omega in Extra Deck): Aleister + Sorath (banished) → **Omega** → banish another of her monsters
16. **Battle:** Oceanus 3000 + Mechaba 2500 + Super Poly Fusion (+ Omega 2800, + Virakam 1000 if no Sacred Sword)

**End:** Her best monster gone, 5,500+ damage

**Remember:** Super Poly MUST come before Invocation uses Madness. Once activated, Super Poly can't be cancelled.

## Line S6: Aleister or opener + any card + Super Poly (going 2nd; Going 2nd · Taffy's weakest line + Super Poly (card text))

Needs: Aleister, Meltdown or Aiwass, Super Poly, +2 spare cards.

**Get Aleister**
1. Aleister in hand → Normal Summon it. Otherwise **Meltdown** or **Aiwass from hand** → search Aleister. (Sacred Sword also works, but then only Fusions can attack)

**Get Sorath**
2. Normal Summon Aleister → search **Invocation**
3. Link Aleister → **Almiraj**
4. Invocation: Aleister + Almiraj → **Sorath**
5. Invocation GY: add the banished Aleister
6. Discard Aleister on Sorath → Sorath revives Aleister

**Break her board**
7. Link Aleister + Sorath → **Madness**
8. Sorath GY: Sorath + Aleister → **Baybarron**. Chain: Madness (discard spare → **Invocation**) + Baybarron (search **Virakam**, skip banish)
9. Special Summon Virakam → set **Invoke Sword**
10. **Super Poly** (discard spare): Madness + her best monster → by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**
11. Invocation: Madness (GY) + Virakam → **Mechaba**
12. **Battle:** Baybarron 2450 + Mechaba 2500 + Super Poly Fusion

**End:** Her best monster gone, about 7,000 damage

## Line S7: Spenta or Crowley + FIRE/WIND + Grail + Invocation (going 2nd; Going 2nd · no Aleister needed · UNTESTED, built from card text)

Needs: Spenta or Crowley, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Grail, Invocation, She has a face-up monster.

**Sorath into Madness**
1. **Crowley:** Normal Summon it (or Spenta: discard → search Crowley, it summons itself). Crowley + FIRE/WIND (hand) → **Sorath**
2. Sorath: revive **Crowley**
3. Link Crowley + Sorath → **Madness** (counts as Aleister, turns on Grail)

**Take her monster, then Aeon**
4. **Grail mode 2:** Madness + her face-up monster → by her Attribute: DARK/WATER **Oceanus**, LIGHT/EARTH **Baybarron**, WIND **Raidjin**. (Extra Deck monster of any Attribute → **Omega**)
5. **Invocation:** that Fusion + Sorath (GY) → **Aeon** (different Attributes)
6. **Aeon:** banish her 2 other cards
7. **Battle:** Aeon 3800

**End:** Her whole field gone (up to 3 cards) · Aeon

**Remember:** Grail doesn't target, so it gets round Dragoon. If her monster is FIRE, Sorath is already used: play S8 instead if you have Invoke Sword.

## Line S8: Spenta or Crowley + FIRE/WIND + Invocation + Invoke Sword (going 2nd; Going 2nd · no Aleister needed · UNTESTED, built from card text)

Needs: Spenta or Crowley, FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Invocation, Invoke Sword.

**Sorath into Madness**
1. **Spenta:** discard → search **Crowley** (it summons itself). Or Normal Summon Crowley from hand. Crowley + FIRE/WIND (hand) → **Sorath**
2. Sorath: revive **Crowley**
3. Link Crowley + Sorath → **Madness** (counts as Aleister on field and in GY)

**Aeon**
4. **Invocation:** Madness + Sorath (GY) → **Baybarron**: search **Virakam**, SKIP the banish
5. **Invoke Sword:** Baybarron + Sorath (banished) → **Aeon** (FIRE + LIGHT)
6. **Aeon:** banish her best monster + 1 more of her cards
7. **Battle:** Aeon 3800

**End:** Aeon · her 2 best cards banished

**Remember:** TTT goes live if she activates a monster effect on your turn. Crowley counts as Aleister only while face-up, so a Crowley revived by Sorath (negated) doesn't.

## Line S9: Aleister got Imperm'd + FIRE/WIND + Grail (going 2nd; Going 2nd · UNTESTED, built from card text)

Needs: Aleister on field (search negated), FIRE/WIND: Ash, Droll, Fuwalos, Zoroa, Invocation, Grail.

**Imperm doesn't stop its name**
1. **Invocation:** Aleister (field) + FIRE/WIND (hand) → **Sorath**
2. Invocation GY: add the banished Aleister
3. Discard Aleister on Sorath (+1000) → Sorath revives Aleister (Defence)

**Take her monster**
4. **Grail mode 2:** Aleister + her best monster (tap it for its Attribute): DARK/WATER **Oceanus**, WIND **Raidjin**, LIGHT **Mechaba**, EARTH **Baybarron**. If it's FIRE, take another of hers
5. **Battle:** the Grail Fusion + Sorath 2600

**End:** Her best monster gone · Sorath · Grail Fusion

**Remember:** Imperm negates Aleister's search, not its name, so Invocation and Grail still work.

## Tip T1: Her turn: your hand traps (tips & tricks; Going 2nd · card text)

Needs: Whatever hand traps you hold.

**Timing**
1. **Maxx "C":** on her first Special Summon. Draw 1 for every Special Summon this turn
2. **Ash:** on an effect that searches, sends from her Deck, or summons from her Deck
3. **Droll:** right after her first search, so the rest are blocked. Not in the same turn as Fuwalos
4. **Imperm** (from hand, you control no cards): her starter monster on the field
5. **Fuwalos:** early in her Main Phase, only while you control no cards
6. **Ghost Belle:** her GY effects. **Ghost Ogre:** a card effect on the field (never Shining Sarcophagus)
7. **Nibiru:** after her 5th summon this turn

**End:** Keep Super Poly for your turn

**Remember:** Her deck tells you the order: search-heavy → Droll; summon-heavy → Maxx "C".

## Tip T2: Going 2nd into Natasha's Dragoon (tips & tricks; Built from card text · practise it)

Needs: Aleister route, Super Polymerization, Imperm (ideal).

**Her turn**
1. **Imperm Imsety** (stops her send-to-GY punish)

**Your turn**
2. **Meltdown** → Aleister (bait Dragoon's negate here)
3. Normal Summon Aleister → search **Invocation**
4. **Super Poly**: Aleister + Dragoon → **Oceanus** (she can't respond)
5. Invocation: Dragoon (her GY) + Oceanus → **Aeon**
6. Aeon: banish **King's Sarcophagus** + her best Horus
7. Attack

**End:** Dragoon gone · Sarcophagus gone · Aeon 3800 on board

**Remember:** Can't hit Timaeus the turn it lands. Ghost Ogre can't touch Shining Sarcophagus. Elysium (when crafted) banishes ALL her DARK monsters.

## Tip T3: Going 2nd: finishers (tips & tricks; Built from card text · add to the end of any line)

Needs: Use whatever you have left.

**Remove her blocker**
1. **Invoke Sword in hand** (Omega in Extra Deck): Aleister + a Fusion (both banished) → **Omega** → banish her monster
2. **Super Poly:** Madness (counts as Aleister) + her monster → Fusion by her Attribute: LIGHT/EARTH **Baybarron**, WIND **Raidjin**, FIRE **Sorath**, DARK/WATER **Oceanus**
3. Do Super Poly BEFORE Invocation uses Madness. Invocation can still use Madness from the GY

**More damage**
4. **Aleister in hand:** discard during battle → a Fusion gains 1000
5. **Oceanus in GY:** banish it → one Fusion can attack directly
6. **Little Knight:** SKIP its banish or you can't attack directly

**Attack values**
7. Aeon 3800 · Oceanus 3000 · Baronne 3000 · Omega 2800 · Mechaba 2500 · Baybarron 2450
8. Raidjin 2200 · Madness 1800 · Sorath 1600 · Little Knight 1600 · Virakam 1000

**End:** Count to 8000 before you start the Battle Phase

**Remember:** Every going-2nd line already includes these where they fit.

## Tip T4: Clear her board with Aeon (no Normal Summon left) (tips & tricks; Tip · card text · UNTESTED)

Needs: A Fusion on your field, Grail, Invocation (or Reminiscent to search it), Aleister in hand (or Meltdown).

**Line**
1. **Meltdown** (if held): search **Aleister**. Your Fusions can't be negated
2. **Reminiscent** (if held): Special Summon it targeting your Fusion. Banish De Anima → search **Invocation**
3. **Grail mode 1:** Aleister (hand) + a Deck monster → a Fusion with a **different Attribute** from the one on your field (e.g. Crowley DARK → **Oceanus**, Droll/Aiwass WIND → **Raidjin**)
4. **Invocation:** both Fusions → **Aeon**: banish 2 of her cards
5. Attack

**End:** Her 2 best cards gone · Aeon 3800

**Remember:** Aeon needs different Attributes: Sorath and Mechaba are both LIGHT.

## Tip T5: Planet Run deck: what's different (tips & tricks; Side deck · secondary)

Needs: Planet Run event deck.

**Differences from the ranked deck**
1. **No Zoroa:** FIRE/WIND material is Ash, Droll, Fuwalos or a banished Aiwass
2. **No Ghost Ogre:** for Grail mode 1 LIGHT material use Spenta or Nibiru from the Deck
3. Every other line works the same

**End:** Ranked lines first; check this before naming Deck monsters in Planet Run

**Remember:** Send the Planet Run list after any change so this stays right.

## Discard priority (Madness, Mechaba, Super Poly, Spenta costs)

Discard the card that does least on **her** turn. Once you control cards, Fuwalos and Imperm-from-hand are dead.

1. Dead copies: 2nd Meltdown, a Sword when another is set, Sacred Spirit Sword after you've used one
2. Mulcharmy Fuwalos
3. Infinite Impermanence (unless you'll set it)
4. Crossout Designator
5. Ghost Belle

**Keep:** Maxx "C", Ash, Super Polymerization, Droll, Nibiru, Ghost Ogre. For Mechaba, try to hold 1 monster and 1 Spell/Trap so it can negate either type.

## Hand-card Attributes (for Invocation from hand)

Checked on YGOPRODeck, 14 Nov 2026. With Aleister, each one makes:

| Card | Attribute | Aleister + it makes |
| --- | --- | --- |
| Ash, Zoroa | FIRE | Sorath |
| Fuwalos, Droll, Aiwass | WIND | Sorath or Raidjin |
| Maxx "C", Ghost Belle | EARTH | Baybarron |
| Ghost Ogre, Nibiru, Spenta | LIGHT | Mechaba or Baybarron |
| Crowley | DARK | Caliga or Oceanus |

Spend the card lowest on the discard priority. A FIRE/WIND card makes it Line 5, which beats Line 6.

## Lessons from live games (14 Nov 2026)

- **Read both GYs and the banishment before every Invocation.** Invocation banishes from **either** GY. Her Sword returning Fusions from banishment to her GY made **Aeon** possible (and better than Caliga); missed it, then lost to the timer.
- **Her Magical Meltdown face-up = her Invocation, Sword, Grail and Super Poly can't be negated.** Don't spend Mechaba's discard on them; save the discard for Super Poly.
- **One discard, two uses:** Mechaba and Super Poly both cost a card from hand. Decide which one gets it before her turn starts.
- **Super Poly from a set position is best on her turn after she has 2+ Fusions:** fuse them into your Aeon.
- **Ghost Ogre can't destroy Shining Sarcophagus** (it can't be destroyed by monster effects).
- **Timer:** send the screenshot at the start of the turn; under 30 seconds, act on your own read.

### Game log: Planet Run vs Invoked mirror, went first (14 Nov 2026)

Hand: Ghost Ogre, Fuwalos, Crowley, Sacred Spirit Sword, Sword. Imperm'd Aleister's search.

Mistakes (Claude's calls):
1. **Didn't say "skip Baybarron's banish".** Baybarron's on-summon banish hit Madness in our GY, so Virakam had no Aleister to enable it and the planned Invocation → Mechaba was lost. **Rule: every Baybarron step says "skip the banish" unless a target is named.**
2. **Planned a Link (Little Knight) with Oceanus in the Extra Monster Zone.** Links need the Extra Monster Zone or a zone a Link points to; with Oceanus there and no Link arrows, the game demanded Oceanus as material. **Rule: before any Link, check a legal zone exists.**
3. **Line changed mid-combo** (Aiwass GY summon, then Oceanus early) without re-checking what each later step needed (Aleister in GY for Virakam).

What went right: Sword using the banished Aiwass (WIND) as material after Imperm stopped the search.

## Checklist before giving any line

1. Read both GYs, both banishment zones, and every face-up card (e.g. their Meltdown).
2. For each step, check what it needs (Aleister on field/GY? discard? free zone?) and that an earlier step doesn't remove it.
3. Every optional banish/search: say exactly what to pick, or "skip".
4. Links: confirm a legal zone. Fusions from the Extra Deck can go to Main Monster Zones; Links can't.
5. Name which card is the discard for Mechaba / Super Poly.
6. After every game: add mistakes and fixes to this page.

### Game log: Planet Run vs DoomZ (14 Nov 2026): time limit loss

- Lost on **total duel time**: 8:50 used vs her 5:32, in only 3 turns. Most of it was waiting on Claude's long replies.
- **Fix:** play the practice-sheet lines from memory without asking; ask Claude only for unusual spots; Claude replies in one or two lines during games.
- **Lewis's find:** Aleister searched Invocation, then **Invocation banished Oceanus (GY, EARTH) + Baybarron (FIRE) → Hyperinvoked Aeon**. Aeon needs **no Aleister**, just 2+ Fusions with different Attributes, and Invocation can banish them from your field and GY. Claude had wrongly said "nothing works without an Aleister". **Rule: always check GY Fusions for an Aeon.**
- **Aiwass in the GY is a free extender:** whenever a face-up Fusion you control is sent to the GY (not by battle), e.g. as Link material for Little Knight or Madness, Aiwass Special Summons itself, then you can Fusion Summon an Invoked using monsters from hand or field. Look for it every time a Fusion leaves the field.

### Game log: Planet Run vs Witchcrafter, went second (14 Nov 2026): win

- Hand: Droll, Ash, Reminiscent, Aiwass, Meltdown (+ drew Crowley). Opponent opened Witchcrafter Genni + a Spell, then Madame Verre.
- Opponent surrendered on turn 2 after Meltdown → Aleister → Aiwass. Used 1:44 of clock: short replies worked.
- **Witchcrafter Madame Verre** (UR, LIGHT Level 8 Spellcaster, 1000/2800): Quick Effect, discard a Spell to negate all your **currently** face-up monsters this turn; damage calculation: reveal Spells to gain 1000 attack each. Monsters you summon after it resolves are unaffected; Virakam stops it if she uses it on a Fusion's effect.

### Game log: Planet Run vs Hecahands (Tim), went first (14 Nov 2026)

- **Missed a free Sorath revive on our own turn.** Sorath's Quick Effect is once per turn in **each** Main Phase, so use it on your turn (e.g. revive Droll as a blocker or material) and again on theirs.
- **Grail needs an Aleister in your field, GY or banishment before you activate it.** One in hand doesn't count.
- Know which deck is in use: the Planet Run deck has no Ghost Ogre. Claude must check the deck list before naming Deck monsters for Grail.
- Sacred Spirit Sword's third mode (banish 1 of 3 random Extra Deck cards) summons nothing, so it's safe against Fuwalos. Hit Hecahands Xeno.
- **Result: loss on turn 2.** She ran 2+ Hecahands Xeno: the second Xeno summoned our Baybarron from our Extra Deck, our Mechaba was stolen, and Xeno 3400 + Mechaba 2500 + Baybarron 2450 attacked for lethal.
- **Lessons vs Hecahands:** a 2-monster board with only a Spell discard for Mechaba isn't enough. Keep a **monster** in hand for Mechaba so it can negate Xeno's Quick Effect. The Sacred Spirit Sword Extra Deck rip only hits 1 of 3 random cards, so expect a second Xeno. Her Fuwalos draws made her hand big; going first, consider making fewer summons until her Fuwalos turn is over.

### Game log: Planet Run, went first, Ash + Fuwalos (14 Nov 2026): loss

- Ash hit Aleister's search; she also used Fuwalos. Claude switched to Line 3, then changed it again mid-turn to save summons. Lewis got lost following the changing steps and ended on Aeon + Virakam + Imperm only.
- **Lesson:** when the plan breaks mid-combo, Claude gives **one** replacement line and sticks to it. Under the clock, a simple board played confidently beats a better line half-finished.
- **Practise Lines 1 and 3 against the AI** until they're automatic; then a broken line is recognisable without help.

### Game log: Planet Run vs Fiendsmith / Horus / Dark Magician, went first (14 Nov 2026): loss

- Our Aeon was removed; **Aiwass revived itself from the GY** (good), but with no Aleister it couldn't fuse.
- Claude named **Ghost Ogre**, which wasn't in hand. **Rule: read the hand from the screenshot every time.**
- **Nibiru** after her 9th summon tributed her board, but she rebuilt (Little Knight, Hapi, Imsety, Destruction, Rank 8).
- Caliga in Defence was removed by Little Knight's banish, so it didn't stop the attacks. Against a board with Little Knight, Caliga alone isn't protection.

### Game log: ranked vs Red-Eyes Dragoon, went first (14 Nov 2026): loss

- End board: Oceanus (Extra Monster Zone), Mechaba, Baybarron, Virakam, Meltdown, set Imperm; hand Ash + 2 Aleister.
- Opponent **Super Polymerization**'d Mechaba + Virakam into Mudragon of the Swamp (can't be responded to), made **Red-Eyes Dark Dragoon**, destroyed Oceanus for 3000 burn, then attacked.
- **Lessons:** Super Poly beats a negate board; nothing stops it. Save **Ash for the Dragoon route** (Red-Eyes Fusion uses Deck monsters, so Ash can negate it; Destruction's Gaze search too). Keep a **monster** in hand for Mechaba: Dragoon's destroy/burn is a monster effect.
- Lewis used **Ash on Magician's Rod's search** and **set Imperm on Rod to negate Triple Tactics Talent through Imperm's column effect** (a set Imperm also negates other Spell/Trap effects in its column that turn). Good plays; the loss came from Super Poly + Dragoon.

### Practice log: Solo, Line 5 going second (14 Nov 2026): win

- Discarded the hand Sword at step 15 (the sheet didn't say to keep it), so no Omega finish. Fixed in v1.2 (Line 5 note + Line 11).
- **Once Super Poly is activated you can't cancel it.** Madness was already banished for Oceanus, so the only legal fusion was Mechaba + Oceanus → Aeon. Order matters: Super Poly before Invocation uses Madness.
- Won anyway next turn with Aeon + Omega (2800 for the final hit) vs the Archfiend AI.

- **Spent Ash as Sorath material when Fuwalos (WIND) was already in the GY.** Invocation can banish GY monsters, so keep hand traps in hand.
