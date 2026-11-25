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

## More
Games coached in other sessions (Machina Fortress, Elfnote / Power Patron) are in the Rikka page's game log and "Coaching mistakes to avoid". Add them here as scenarios when their positions are written down.
