# Coaching scenarios (regression set)

Real positions from Lewis's games, with the answer we now know is right and the mistake made at the time. Use them to test the **master-duel-match-coach** skill after changing it: for each one, would the skill (as written) lead to the right answer?

## S1. Horus, going 2nd, my Main Phase 1 (24 Nov 2026)
- **Their board:** Hapi, Imsety, Qebehsenuef, Duamutef; King's Sarcophagus; Walls of the Imperial Tomb (field); Shard of Greed. 8000 / 8000.
- **Hand:** Rikka Petal, Predaplant Longinephila, Mudan, Rikka Black Princess, Dominus Impulse.
- **Right answer:** "Horus break" (`lines_handfit.cue`). Teardrop the Rikka Sacred Queen **detaches 2** to send both Sarcophagi; Dominus Impulse for Horus the Black Flame Deity; **attack** afterwards.
- **What went wrong:** the line was corrected halfway through the message; only one Sarcophagus was sent; no attack (3100 damage missed).

## S2. Horus, their Standby Phase (24 Nov 2026)
- **My board:** Teardrop the Rikka Sacred Queen (1 material), Teardrop the Rikka Queen (2), Sacred Queen Strenna (0), Konkon, set Rikka Sheet + Dominus Impulse. **Their board:** Hapi, Qebehsenuef, Walls of the Imperial Tomb, Shard of Greed. Timer 34 s.
- **Right answer:** now, before her Main Phase: Sacred Queen's Quick Effect, detach 1 → send **Walls**, Tribute **Hapi** (so it can't add the Sarcophagi back). Fast mode: lead with that one line. (Lewis won by surrender.)

## S3. Rhino, going 1st (25 Nov 2026)
- **My board:** Rikka Princess (Special Summoned). **Hand:** Ash ×2, Mudan, Rikka Sheet.
- **Right answer:** "Rikka Princess + Mudan + Sheet". Hold Ash for his first search.
- **What went wrong:** said "Ash ×2 on his searches": Ash is once per turn.

## S4. Rhino, my turn 3, his field empty, 1 card in his hand (25 Nov 2026)
- **My board:** Konkon, Rikka Black Princess (summoned this turn). **Hand:** Longinephila, Ash.
- **Right answer:** Line B, but Strenna attaches Petal or Black Princess (PredaRikka has 1 Rikka Princess, which Glamour must add); **Xyz before Glamour** (Glamour Tributes from the field only, and should Tribute Rikka Queen Strenna). Cactus Bouncer vs Longinephila: both need the Normal Summon; Cactus locks HERO out. Then attack.
- **What went wrong:** the line attached Rikka Princess and then had Glamour add her; Mudan got Tributed before the Xyz.

## S5. Rhino, my turn 5 (25 Nov 2026)
- **Their board:** Vision HERO Increase only, no cards in hand, 6200 LP. **My board:** Konkon, Rikka Princess, set Moonlit Waters. **Hand:** Longinephila, Ash ×2.
- **Right answer:** Konkon sets Glamour; Glamour Tributes Increase through Konkon; Byblisp/Longinephila → Lilizard → Bal Teah; Jasmine; attack for 4900 (Jasmine has no ATK boost). Moonlit Waters had **no legal pair** (Hellebore and Primrose used).

## S6. Rhino, going 2nd into Dark Law + Chaos ×2 (25 Nov 2026)
- **Their board:** Contrast HERO Chaos ×2, Elemental HERO Sunrise, Masked HERO Dark Law, Xtra HERO Cross Crusader, 1 set card.
- **Hand:** Longinephila, Princess Dracaena, Mulcharmy Purulia, Predaprimitive ×2, Konkon.
- **Right answer:** no real break: Predaprimitive and Dracaena can't be activated under Dark Law, and PredaRikka runs no Polymerization. Bait a Chaos with Konkon, say plainly the hand can't break it, and for next time play Invoked against Rhino (or side Dark Ruler No More).
- **What went wrong:** the plan used Predaprimitive → Super Poly, then Lilizard → Polymerization → Starving Venom (`KNOWN BAD` in `lines_predarikka.cue`).

## S7. Jack (Cyber Dragon), going 1st, Moonlit Waters Ashed (22 Nov 2026)
- **Hand:** Ash, Instant Fusion, Super Polymerization, Forbidden Droplet (Moonlit Waters negated).
- **Right answer:** Instant Fusion needs **no materials**: Ambulomelides → add Predaprimitive → the proven Predaprimitive → Cactus line.
- **What went wrong:** said Instant Fusion needed a monster in hand. Lewis corrected it.

## S8. Sloth (Rikka mirror), going 1st (25 Nov 2026)
- **Hand:** Princess Dracaena ×2, Triple Tactics Talent, Predaprimitive, Moonlit Waters.
- **Right answer:** **Moonlit Waters first**, searches after: Droll stops every add once it resolves, and Master Duel then won't activate Moonlit Waters at all.
- **What went wrong:** Dracaena, then Predaprimitive; Droll on the add; Moonlit stuck in hand (`KNOWN BAD` in `lines_predarikka.cue`).

## S9. Machina (bilotahn), going 2nd into Machina Fortress (25 Nov 2026)
- **Their board:** Machina Fortress (2500) only, no backrow, 3 in hand. 8000 / 8000.
- **Hand:** Princess Dracaena, Lilizard, Rikka Glamour x2, Predaprimitive x2.
- **Right answer:** "Machina: Hand 4 lethal" (`lines_handfit.cue`, UNTESTED as a whole). Fortress punishes targeting (discard from your hand) and battle (destroys a card), so **Glamour Tributes it through Konkon**. When Sacred Queen Strenna's detach summons Rikka Queen Strenna, **attach a Rikka monster** (optional, but she needs material for her Hyperyton float). Only 1 Glamour per turn: the second is a discard. Count lethal with Attack-position monsters only: Teardrop 2800 + Hyperyton 2600 + Sacred Queen Strenna 2000 + Jasmine 1800 = 9200.
- **What went wrong:** Ash on Predaprimitive (fine: Byblisp was already sent and still searched), then Ghost Belle on Bal Teah's revive. In the improvised line **Hyperyton never came out**, most likely because Rikka Queen Strenna had no material (`KNOWN BAD: Machina, Rikka Queen Strenna Tributed with no material`). Won anyway (they surrendered on 1900).

## S10. Elfnote (trampaslocas), going 2nd, turn 2 (25 Nov 2026)
- **Their board:** Elfnote Fortuna (centre), Elfnote Power Patron, Elfnote Seraphim Strelitzia (Synchro, Defence), a face-up Elfnote Continuous Trap; 4 in hand.
- **Hand:** Cactus Bouncer, Hellebore, Moonlit Waters, Super Polymerization, Evenly Matched.
- **Right answer:** read their text first: Power Patron, Strelitzia and Fortuna all have Main Phase Quick Effects. So **do nothing in Main Phase 1, go to the Battle Phase with 0 cards, Evenly Matched from the hand at the end of your own Battle Phase**, then combo in Main Phase 2 (Moonlit Waters line, Cactus last). Super Poly has no pair (no shared Type + Attribute): set it.
- **What happened:** Evenly Matched left them on Strelitzia; then **Ash on Moonlit Waters**. Ended on Cactus + set Super Poly. Note: Strelitzia is a **Plant**, so Cactus + Strelitzia means neither player can Special Summon.

## S11. Elfnote, turn 4: Cactus + their Strelitzia (25 Nov 2026)
- **My board:** Cactus Bouncer, set Super Poly. **Their board:** Strelitzia, Medius the Pure. **Hand:** Hellebore, Predaprimitive.
- **Right answer:** **no Special Summons at all** (Cactus counts any other Plant on either field), including Instant Fusion and Super Poly. Predaprimitive → Byblisp → Longinephila; **Normal Summon Longinephila** (always Attack; a Set doesn't trigger the search). Pass. Proven (`Elfnote turn 4: Predaprimitive under Cactus + Strelitzia`); `KNOWN BAD: Elfnote turn 4, Instant Fusion under Cactus + Strelitzia` is the trap.

## S12. Elfnote, turn 6: Baronne + Lucina (25 Nov 2026)
- **Their board:** Elfnote Lucina (2500), Baronne de Fleur. **Hand:** Dracaena, Lilizard, Hellebore; field Longinephila + set Super Poly.
- **Right answer:** **Dracaena first as Baronne bait** (worked). Expect **Elfnote Tinia** from their hand: on your turn it banishes a **random card from your hand** until the End Phase. Play the key hand card (Lilizard) early instead of holding it.
- **What went wrong:** Tinia banished Lilizard and the line stopped. Hellebore later went in **Defence** (its revive always is) and died.

## S13. Elfnote, turn 8: Little Knight (25 Nov 2026)
- **LP** 5400 vs 8000. **Their board:** Elfnote Lucina, S:P Little Knight (EMZ); 2 in hand. **Hand:** Lilizard, Moonlit Waters; Hellebore in the GY; my field empty.
- **Right answer:** "Elfnote turn 8 lethal" (`lines_handfit.cue`, UNTESTED): Moonlit → Black Princess → Petal → Mudan + Primrose → Konkon sets Glamour → Sacred Queen Strenna (Attack) → Rikka Queen Strenna (attach Mudan) → Glamour Tributes Lucina via Konkon → Hellebore Tributes Rikka Queen Strenna → Hyperyton (Attack) → Primrose + Hellebore → Teardrop → Teardrop Tributes Little Knight → Normal Summon Lilizard: 3000 + 2600 + 2000 + 1200 = 8800. **Little Knight's Quick Effect answers any activation**: when Rikka Princess negates it, **Tribute a Plant the rest of the line doesn't need**, then recount the lethal.
- **What went wrong:** Rikka Princess Tributed **Primrose**, which the Teardrop Xyz needed (`KNOWN BAD: Elfnote turn 8, Rikka Princess Tributes Primrose`). Lost on turn 9.

## More
Add each new position here after every game (board, hand, right answer, what went wrong), plus a checker line where the mistake was a line.
