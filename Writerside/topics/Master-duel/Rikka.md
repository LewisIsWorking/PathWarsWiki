# Rikka

Lewis's Rikka deck (built 21 Nov 2026). Main Deck matches **xemnas43's Master I list (6 Nov 2026)** except Droll ×2 in place of Triple Tactics Talent ×2.

## Main Deck (40)

Droll & Lock Bird 2, Rikka Petal 3, Maxx "C" 1, Ash 3, **Cactus Bouncer 1**, Primula 1, Rikka Princess 2, Mulcharmy Fuwalos 3, Mudan 2, Rikka Black Princess 3, Hellebore 1, Primrose 2, Foolish Burial 1, Rikka Glamour 3, Rikka Moonlit Waters 3, Rikka Konkon 2, **Crossout Designator 1**, Infinite Impermanence 3, Rikka Sheet 1, Dominus Impulse 2.

**21 Nov 2026 changes:** −Snowdrop, −1 Dominus Impulse (from hand it locks EARTH effects, and Hyperyton is EARTH), +Cactus Bouncer (30 of the last 100 MDM lists run 1; Normal Summon it last to stop all Special Summons, strong vs Natasha), +Crossout Designator.

**Extra Deck (21 Nov 2026):** Rikka Queen Strenna, Kanzashi, Rikka Sacred Queen Strenna ×2, Orea, a Rank 4 (N), **Teardrop the Rikka Queen ×2**, Hyperyton, Teardrop the Rikka Sacred Queen, Sunavalon Dryas ×2, Sunvine, S:P Little Knight, plus one SR Link. The 2nd Teardrop lets you upgrade one into the Sacred Queen and still have a Teardrop when you make four Level 8s (22 of the last 100 MDM lists run 2).

## How we build lines (standing approach, 25 Nov 2026)

- **Fit every line to the exact hand.** Start from the closest proven line, then change it to use the cards actually in hand (dead cards become Tribute fodder, spare searches get a job). Say what changed and why.
- **Always improve.** When a game shows a better step, add it here as a new line or an upgrade, marked **UNTESTED** until it's been played.
- **Check the line before you start:** Normal Summon used once, each once-per-turn effect used once, summon locks match the Extra Deck monsters, no more than 5 Main Monster Zones.
- **Run the line checker** (`tools/line-check`, CUE): it checks deck counts, once-per-turn effects, summon locks, zones, Dark Law, and monsters used after they left the field. It caught all three mistakes from the 24–25 Nov games.
- **Plan for their negates first.** Count them, decide what baits each one, and put the cards they can't stop first (see "Playing through negates" below).

## Playing through negates

- **Know what their negate can touch.** Contrast HERO Chaos only targets **face-up** cards. A monster effect activated **from the hand** (Black Princess, Mudan, Dracaena, Lilizard summoning themselves) can't be targeted until the monster is on the field.
- **Get a Rikka monster on the field first.** Rikka Princess (hand or GY) and Hellebore (hand) only negate while you control a Rikka monster. Black Princess from the hand is the safest first play: Chaos can't stop the summon.
- **Bait in order of value.** Spend their negate on your least important card (Konkon's activation, a spare search), and keep the line that wins for after their negates are gone.
- **Use cards they can't respond to:** Super Polymerization (no responses), Dark Ruler No More (no monster effects in response; negates all their monsters), Forbidden Droplet sending a monster.
- **Dark Law shuts off the Predap engine.** With Masked HERO Dark Law up, the client won't activate Predaprimitive (it sends to the GY), and Dracaena, Moonlit Waters and Droplet send to the GY too. Answer Dark Law before you search, or play Invoked against Rhino ([Tournament decks](Tournament-decks.md)).

## The game plan (Rikka Discord, 21 Nov 2026)

From fmproductions and BUTENUS REALUS in the MD Discord #rikka channel. Goal: **2-3 Xyz, set Rikka Sheet, Rikka Princess in the GY**.

1. **Mudan → Konkon.** Every line starts by getting Mudan summoned by a Plant so it searches Konkon.
2. **Rank 6 Sacred Queen Strenna** (two Level 6s). Detach 2 → **Rank 4 Rikka Queen Strenna**, attach **Rikka Princess** from the Deck (she lands in the GY later = free negate).
3. **Konkon sets Moonlit Waters.** Activate it **Tributing Rank 4 Strenna** (with her material): add **Primrose**, send **Hellebore** to the GY. That one Tribute also triggers: Strenna → an Extra Deck monster (Hyperyton/Kanzashi), Sacred Queen Strenna → set **Rikka Sheet**, **Primrose** → herself + another Rikka.
4. **Revive Hellebore** from the GY.
5. **Primrose changes the monster she summoned to Level 8**, then Xyz it with **Hellebore** → **Teardrop**. **Keep Primrose on the field.**
6. **On their turn, Primrose's Quick Effect** Xyz Summons **Teardrop the Rikka Sacred Queen** over Teardrop, so you get both Tributes.

Mistakes to avoid: using Strenna's detach-to-add (it needs material to summon on Tribute); Xyz-ing Primrose away; improvising when a proven line fits.

## Proven lines with Cactus Bouncer (Yusodus, MDM combo database)

Source: [Yusodus's Rikka guide](https://www.masterduelmeta.com/articles/guides/rikka-yusodus#pure) and the MDM combos "Pure Rikka: 1c June Moon" (Bouncer branch) and "Pure Rikka: 1.5c Black Princess (Bouncer)". "June Moon" = Rikka Moonlit Waters, "Empress Strenna" = Rikka Sacred Queen Strenna.

### A. Moonlit Waters alone → Hyperyton with a Spell material + Cactus (beats Dark Hole)

**In PredaRikka (1 Rikka Princess):** in step 8 attach Black Princess instead, so Glamour can still add Rikka Princess in step 10, and keep her in hand (her negate works from hand/GY, not the field). See Sample Hand 3.

1. **Moonlit Waters** (no Tribute): add **Mudan**, send **Black Princess** to the GY.
2. Special Summon **Black Princess** from the GY.
3. **Black Princess:** Tribute **herself** → **Rikka Petal** from the Deck.
4. **Petal:** add **Primrose**.
5. **Mudan** (hand): Tribute **Petal** → Mudan. Chain: CL1 **Mudan** adds **Konkon**; CL2 **Primrose** → Primrose + **Hellebore** from the Deck.
6. **Konkon:** set **Glamour**.
7. **Primrose:** Hellebore Level −2 (to 6).
8. Xyz **Mudan + Hellebore** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach **Rikka Princess**.
9. **Hellebore (GY):** Tribute **Rikka Queen Strenna** → Hellebore. Chain: CL1 Strenna → **Hyperyton** (attach Strenna); CL2 Sacred Queen Strenna → set **Rikka Sheet**.
10. **Glamour**, Tributing **Sacred Queen Strenna**; **chain Hyperyton: attach Moonlit Waters** (a Spell). Glamour adds **Rikka Princess + Cactus Bouncer**.
11. Special Summon **Rikka Princess** from hand. **Normal Summon Cactus Bouncer.**

End: Hyperyton (monster + Spell material: negates a monster effect **or** a Spell like Dark Hole), Hellebore, Primrose, Rikka Princess, Cactus Bouncer, Konkon, set Rikka Sheet.

### B. Black Princess + any Plant → Hyperyton + Cactus

1. Special Summon **Black Princess**. Tribute the **other Plant** (hand) → **Mudan** from the Deck. **Mudan:** add **Konkon**. **Konkon:** set **Glamour**.
2. Xyz **Mudan + Black Princess** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach **Rikka Princess**.
3. **Glamour**, Tributing **Rikka Queen Strenna**: add **Rikka Princess + Cactus Bouncer**. Chain: CL1 Strenna → **Hyperyton**; CL2 Sacred Queen Strenna → set **Rikka Sheet**.
4. Special Summon **Rikka Princess** from hand; **chain Hyperyton: attach Mudan** from the GY.
5. **Normal Summon Cactus Bouncer.**

End: Hyperyton (monster materials only: no Spell negate), Sacred Queen Strenna, Rikka Princess, Cactus Bouncer, Konkon, set Rikka Sheet.

## Line 1: Rikka Petal (or Glamour) alone

Source: **"Pure Rikka: 1c Petal/Glamour"**, Yusodus, MDM combo database, first ending (Teardrop + Hyperyton + Sacred Strenna). Played 21 Nov 2026 (solo): won turn 3.

1. Normal Summon **Rikka Petal**.
2. **Petal:** send **Black Princess** from the Deck to the **GY** (Droll can't stop a send). Plant-only lock for the turn.
3. Special Summon **Black Princess** from the GY.
4. **Black Princess:** Tribute Petal → Special Summon **Mudan** from the Deck.
5. **Mudan:** add **Rikka Konkon**. Activate it.
6. **Konkon:** set **Moonlit Waters** (or Glamour if Moonlit is already in hand).
7. Xyz **Mudan + Black Princess** (Level 6) → **Rikka Sacred Queen Strenna**.
8. **Sacred Queen Strenna:** detach 2 → **Rikka Queen Strenna** in Defence, attach **Rikka Princess** from the Deck.
9. **Moonlit Waters** (no Tribute): add **Primrose**, send **Hellebore** to the GY.
10. **Hellebore (GY):** Tribute Rikka Queen Strenna → Special Summon Hellebore. Chain order: CL1 **Rikka Queen Strenna** → **Hyperyton** (attach Strenna); CL2 **Sacred Queen Strenna** → set **Rikka Sheet**; CL3 **Primrose** → Primrose + **Black Princess #2** from the Deck.
11. **Primrose:** Black Princess Level +2 (to 8). Chain **Hyperyton**: attach **Mudan** from the GY.
12. Xyz **Black Princess + Hellebore** (Level 8) → **Teardrop the Rikka Queen**.

**End:** Teardrop, Hyperyton, Sacred Queen Strenna, Primrose, Konkon, set Rikka Sheet.

**Their turn (UNTESTED order, from card text):** Teardrop Tributes first (Quick, it has Plant material) → Primrose's Quick Xyz turns Teardrop into **Teardrop the Rikka Sacred Queen** → Sacred Queen sends Spells/Traps (as many as materials detached) and Tributes again. Hyperyton negates by detaching a material of the same card type.

## Line 2: two Teardrops + Cactus Bouncer (UNTESTED, from card text; prefer the proven lines above)

Hand: Black Princess, Rikka Princess, Mudan, Moonlit Waters (+ Droll).

1. **Moonlit Waters** (no Tribute): add **Primrose**, send **Hellebore** to the GY. Do this first so Primrose is in hand for the first Tribute.
2. Special Summon **Black Princess**, then **Rikka Princess**, from hand.
3. **Black Princess:** Tribute **Mudan from your hand** → **Mudan** from the Deck. Triggers: Mudan adds **Glamour**; **Primrose** → Primrose + **Primula** from the Deck. Five monsters on field.
4. **Primula:** Black Princess and Rikka Princess +2 (8 and 6). **Primrose:** Rikka Princess +2 (8).
5. **Hellebore (GY):** Tribute **Primula** → Hellebore (8).
6. **Glamour**, Tributing **Mudan** (the leftover Level 6): add **Rikka Princess #2** + **Cactus Bouncer**.
7. Xyz **Black Princess + Rikka Princess** → Teardrop; **Primrose + Hellebore** → Teardrop #2. Upgrade one into **Teardrop the Rikka Sacred Queen**.
8. **Normal Summon Cactus Bouncer** last.

End: Sacred Queen, Teardrop, Cactus Bouncer; Rikka Princess #2 + Droll in hand. Rikka Princess's hand summon is once per turn, so the second copy stays in hand as a negate.

## Line 3: Kanzashi + Teardrop + Cactus Bouncer, survives Dark Hole (UNTESTED, from card text)

Same hand as Line 2. Swaps the second Teardrop for **Kanzashi** (if your Plants would be destroyed by a card effect, Tribute 1 Plant from hand or field instead).

1. **Moonlit Waters** (no Tribute): add **Primrose**, send **Hellebore** to the GY.
2. Special Summon **Black Princess**, then **Rikka Princess**.
3. **Black Princess:** Tribute **Mudan from hand** → **Mudan** from the Deck (adds **Glamour**). **Primrose** triggers → Primrose + **Primula**.
4. **Hellebore (GY):** Tribute **Primula** → Hellebore.
5. **Glamour**, Tributing **Rikka Princess**: add **Rikka Princess #2** + **Cactus Bouncer**.
6. Xyz **Black Princess + Mudan** (Level 6) → **Kanzashi**. Xyz **Primrose + Hellebore** (Level 8) → **Teardrop**, then upgrade to **Teardrop the Rikka Sacred Queen** (vs Natasha: its Tribute doesn't target, so it hits Dragoon and protected Horus).
7. **Normal Summon Cactus Bouncer.**

End: Sacred Queen, Kanzashi, Cactus Bouncer; Rikka Princess #2 + Droll in hand. **Vs Dark Hole:** Kanzashi Tributes Rikka Princess from hand, nothing dies. Kanzashi's revive effect won't work while Cactus is up.

## End board options to try

| Ending | Strength | Weakness |
| --- | --- | --- |
| **Teardrop + Hyperyton + Sacred Queen Strenna** (Line 1 as written) | Most interruptions | Hyperyton's materials are all monsters, so it can't negate Spells (Dark Hole, Raigeki, Lightning Storm) |
| Line 1 + **Glamour for a Spell material** (UNTESTED) | Hyperyton negates a monster effect **or** a Spell | Konkon sets Glamour instead of Moonlit Waters; Hyperyton's attach is spent on Glamour, not Mudan |
| **Teardrop + Rikka Queen Strenna + Kanzashi** (Yusodus branch 2) | Kanzashi Tributes a Plant instead of your Plants being destroyed | One fewer negate |
| **Rikka Queen Strenna + Kanzashi + Hellebore** (Yusodus branch 3) | Most protection; Hellebore negates targeting monster effects | Fewest interruptions |

Record which ending you used in the game log below.

## Lessons

- **Pupils-style "one effect per turn" trap:** check every "activate 1 of these effects" card before planning two uses.
- **Konkon's replacement Tribute** (Tribute their monster instead of your Plant) is once per turn **per copy**: if they destroy Konkon, Mudan can search the second copy.
- **Going second with Fuwalos:** activate it on their first search while you control no cards.
- **A negated Rikka monster is still a Plant body:** after Destined Rivals / Imperm, use it as Xyz material.
- **Vs Blue-Eyes:** Tribute Jet Dragon with Konkon (no targeting, no destruction). True Light's wipe only works if it reaches the GY and Spirit Dragon isn't up.
- Upgrade Teardrop into the Sacred Queen on **their** turn (Primrose), not yours: you get both Tributes.
- **Vs Horus:** Walls of the Imperial Tomb counts as King's Sarcophagus. Teardrop the Rikka Sacred Queen sends **one Spell/Trap per material detached**, so detach 2 to clear both, or Sons keep reviving.
- **Attack after the break.** King's Sarcophagus only stops destruction by card effects, not by battle.
- **Teardrop Queen and Sacred Queen reset on their turn.** Holding both Quick Effects for her Main Phase won the Horus game.

## Game log

| Date | Opponent | Turn | Result | Notes |
| --- | --- | --- | --- | --- |
| 21 Nov 2026 | Blue-Eyes (ranked) | 2nd | **Won** (turn 6) | Destined Rivals negated Black Princess, but she was still Xyz material. Konkon + Glamour Tributed Blue-Eyes Jet Dragon; built Teardrop the Rikka Sacred Queen + Sacred Queen Strenna + Primrose. True Light set Return of the Dragon Lords. Ground them down with Hyperyton and Rikka Sheet; won turn 6. |
| 21 Nov 2026 | Charmer / Familiar-Possessed (ranked) | 2nd | **Won** (time limit) | Fuwalos on Spellbook of the Grand Circle drew a big hand. Possessed Partnerships destroyed Konkon; Mudan searched Konkon #2 and its replacement Tribute took their 4050. Ended Teardrop the Rikka Sacred Queen, Sacred Queen Strenna, Primrose, Black Princess, Primula. Foolish Burial unused (next turn: send Black Princess, revive her). They ran out the clock on turn 3. |
| 21 Nov 2026 | Rising Pyroxene (solo) | 1st | **Won** | Line 1 from Petal. Short combo, plenty of time on the clock. Won turn 3. |
| 24 Nov 2026 | Horus (MDPro4, UnknoDaemon) | 2nd | **Won** (surrender, turn 3) | Into 4 Sons + King's Sarcophagus + Walls of the Imperial Tomb. Black Princess / Mudan / Primrose → Sacred Queen Strenna, Teardrop the Rikka Queen ×2 → Teardrop the Rikka Sacred Queen, Konkon, set Sheet + Dominus Impulse. Removed Imsety and Duamutef and King's Sarcophagus, but **Walls stayed** and he **didn't attack** (3100 damage missed). On her turn, chained Teardrop Queen and Sacred Queen Quick Effects in Main 1, cleared her field; she surrendered. |
| 25 Nov 2026 | Rikka (ranked, Sloth) | 1st | **Lost** | Sample Hand 3 (Dracaena ×2, Triple Tactics Talent, Predaprimitive, Moonlit Waters). Dracaena, then Predaprimitive (Super Poly) → **Droll** on Byblisp's search. Moonlit Waters couldn't be activated under Droll. Talent took a card from their hand; Dracaena ×2 → Sylvan Dancepione got **Ashed**. Ended on Dancepione + set Super Poly. Lesson: Moonlit Waters first, searches after. See [Speed sheet: Sloth](Speed-sheet.md). |

## PredaRikka (Lewis's second Rikka deck, 21 Nov 2026)

Main Deck = **lmt's 1669-rated Rating Duel list (21 Nov 2026)**, 45 cards, card for card: Petal 1, Predaplant Byblisp 1, Longinephila 2, Princess Dracaena 3, Maxx "C" 1, Ash 3, Lilizard 1, Rikka Princess 1, Purulia 2, Fuwalos 3, Mudan 2, Black Princess 3, Hellebore 1, Primrose 1, Instant Fusion 1, Glamour 2, Triple Tactics Talent 1, Triple Tactics Thrust 1, Predaprimitive 3, Moonlit Waters 3, Predapruning 1, Konkon 1, Super Polymerization 2, Evenly Matched 1, Rikka Sheet 1, Dominus Impulse 3.

lmt's Extra Deck: Ambulomelides, Garura, Daredevil, Starving Venom, Secreterion, Bal Teah, Black Rose Dragon, Bramble Rose Dragon, Crystal Wing, Rikka Queen Strenna, Kanzashi, Sacred Queen Strenna, Teardrop, Teardrop Sacred Queen, Aromaseraphy Jasmine.

**How it works:** the Predaplant cards are extra starters that turn into a Rikka combo. **Aromaseraphy Jasmine** (Link-2, 2 Plants) is the bridge: Tribute a monster it points to → any Plant from the Deck (Petal or Black Princess). From there it's the normal Rikka game plan.

**No Polymerization (checked 25 Nov 2026):** none of the 21 PredaRikka lists on MDM (Nov 2026: Master I, Rating Duels, tournaments) runs Polymerization; 19 run Lilizard anyway. Lilizard is a **body**: it summons itself (the Polymerization add is optional), is Synchro material for Bal Teah, and draws a card when Bal Teah revives it.

**Starters (any one is a full combo):** Predaprimitive, Instant Fusion, Predaplant Longinephila, Princess Dracaena, plus the usual Petal / Black Princess / Moonlit Waters / Glamour.

**Proven line:** MDM "Predarikka: 1c Any Predap Starter" (Yusodus). Predap engine → Lilizard ×2 → Bal Teah → Jasmine → Byblisp under Jasmine's arrow → Jasmine Tributes Byblisp → Black Princess → Petal → Mudan → Konkon → Sacred Queen Strenna → Rikka Queen Strenna (+ Rikka Princess) → Instant Fusion Ambulomelides → Ambulomelides Tributes Strenna (Hyperyton + Sheet) → Bramble Rose → Black Rose → Konkon sets Moonlit → Moonlit Tributes Ambulomelides → Primrose + Hellebore → Kanzashi → Teardrop → Teardrop Sacred Queen.

End: Teardrop Sacred Queen, Hyperyton (Spell material), Kanzashi, Sacred Queen Strenna, Bramble Rose, Black Rose, Konkon, set Rikka Sheet, Rikka Princess in GY, Super Polymerization in hand.

**Going second:** Predaprimitive searches **Super Polymerization** (2 copies) for no-response removal; **Black Rose Dragon** destroys every card when Synchro Summoned; **Evenly Matched** and **Triple Tactics Thrust** are extra going-second outs; **Purulia** punishes decks that summon from the hand.

**Lewis's PredaRikka Extra Deck (21 Nov 2026):** doesn't own Black Rose Dragon or Bramble Rose Dragon (both UR; Black Rose + Bramble Rose are both in the *Exquisite Jet-Black Rose* secret pack). Without them, skip the Bramble Rose → Black Rose steps of the proven line (Black Princess from the GY + Longinephila Synchro); the rest of the end board is unchanged. You lose Black Rose's going-second board wipe; Super Poly is the main breaker instead. (Crystal Wing was missing on 21 Nov too; it is in the 25 Nov list below.)

## PredaRikka vs Natasha (21 Nov 2026, card text checked; lines below are proven unless marked)

Her deck (from [Natasha](Natasha.md)): Droll 2, Ash 2, Maxx "C", Ghost Mourner, Dark Hole, Droplet, Triple Tactics Talent, Triple Tactics Thrust, Dark Magical Curtain; everything else needs Special Summons (Sons from the GY, Dark Magician of Destruction, Gaze → Dragoon, Horus the Black Flame Deity).

### List changes (45 cards, all owned except where noted)
- **Out:** Mulcharmy Purulia ×2 (she barely summons from the hand), Predapruning, 1 Fuwalos, Triple Tactics Thrust.
- **In:** Droll ×2 (she searches with Imsety, Walls, Shining Sarcophagus, Future Silence, Dark Magician of Destruction), **Cactus Bouncer**, **Forbidden Droplet** (doesn't target, so it hits Dragoon; send a monster and Dragoon can't respond), Glamour #3 (Glamour is how you reach Cactus).

### Going first: Cactus Bouncer lock (Yusodus, "Predarikka: 1c Primitive/Instant (Bouncer)")
1. **Predaprimitive:** send **Byblisp**, add **Instant Fusion**. Byblisp (GY): add **Lilizard**. (Starting from Instant Fusion: Ambulomelides adds Predaprimitive; Predaprimitive sends Byblisp and adds **Super Poly**.)
2. **Instant Fusion** → **Ambulomelides**; it adds **Longinephila**.
3. Special Summon **Lilizard** from hand.
4. **Ambulomelides:** Tribute itself → **Longinephila** from the Deck; it adds any Predap card.
5. **Longinephila + Lilizard** → **Bal Teah**. Bal Teah: **Lilizard** from the GY (draw 1).
6. **Longinephila (GY):** banish it, Predator Counter on anything. **Byblisp** revives from the GY (in the zone Jasmine will point to).
7. **Bal Teah + Lilizard** → **Aromaseraphy Jasmine**, pointing at Byblisp. **Jasmine:** Tribute Byblisp → **Rikka Petal** from the Deck.
8. **Petal:** send **Black Princess**. Black Princess from the GY. **Black Princess:** Tribute **Jasmine** → **Mudan**; Mudan adds **Konkon**. Konkon sets **Glamour**.
9. Xyz **Mudan + Black Princess** → **Sacred Queen Strenna**. Detach 2 → **Kanzashi**, attach **Primrose**.
10. **Glamour**, Tributing a spare Plant (the guide Tributes a Black Princess; Petal also works ?): add **Rikka Princess + Cactus Bouncer**. Chain: CL1 **Kanzashi** revives **Bal Teah**; CL2 Sacred Queen Strenna sets **Rikka Sheet**.
11. Special Summon **Rikka Princess**. Xyz **Rikka Princess + Bal Teah** → **Rikka Queen Strenna**; detach Princess → add **Primrose** from the GY.
12. **Normal Summon Cactus Bouncer.**

End: Cactus Bouncer, Kanzashi, Rikka Queen Strenna, Sacred Queen Strenna, Konkon, set Rikka Sheet; Rikka Princess in the GY; **Primrose + Super Poly in hand**.

**Her turn:** she can't Special Summon (no Sons from the GY, no Dark Magician of Destruction, no Dragoon, no Horus). Dark Hole → Kanzashi Tributes **Primrose from hand** instead. **Don't activate monster effects in her Main Phase unless you must**: that's what turns on her Triple Tactics Talent / Thrust. Use **Rikka Sheet** (a Trap) first.

Backup going-first lines: Line A (Moonlit Waters → Hyperyton with a Spell material + Cactus) and Line B (Black Princess + Plant → Hyperyton + Cactus) above.

### Going second (UNTESTED plan, from card text)
1. **Her turn:** Droll after her first search (Imsety's search or Walls). Ash on Imsety's / Shining Sarcophagus's search. Maxx "C" on her first Special Summon. Stopping the board beats breaking it.
2. **Your turn, first card: Forbidden Droplet**, sending a **monster** (a dead Fuwalos is ideal): she can't respond with Dragoon. Choose **Dragoon** and as many **Sons** as you can pay for; negated Sons can't use their float effects this turn.
3. **Then remove with Tributes, not destruction:** Konkon's cost-Tribute, Teardrop the Rikka Sacred Queen (sends King's Sarcophagus and Walls, then Tributes). Tributing beats King's Sarcophagus and Dragoon's protection.
4. **Horus the Black Flame Deity** (from her hand) triggers when a Horus card leaves by your effect: answer it with **Rikka Princess** (hand or GY, needs a Rikka monster on your field) or **Dominus Impulse**.
5. **Shining Sarcophagus** sends back a monster you summon from the GY if she discards a Spell: bait it with Black Princess before reviving anything important.
6. **Super Poly**: Dragoon + a **DARK Predaplant of yours** → **Starving Venom** removes Dragoon without touching a Horus card (no Black Flame Deity trigger).
7. **Evenly Matched** at the end of your Battle Phase banishes her extra cards face-down: no destruction, no targeting, and banished Sons can't come back.

## Hand-fitted lines (UNTESTED, pass the line checker)

Fitted to exact hands from real games. Full steps in `tools/line-check/lines_handfit.cue`.

### Line C: Predaprimitive + Konkon + Longinephila (going first)
The proven Predaprimitive line above, with two upgrades:
1. **Black Princess Tributes Longinephila from the hand**, not Jasmine. Longinephila is dead in hand (the Normal Summon is for Cactus), and Jasmine stays on the field.
2. **Mudan adds Glamour** (Konkon is already in hand); **Konkon sets Moonlit Waters**.
3. **Before Cactus: Moonlit Waters, Tributing Rikka Queen Strenna** → add Black Princess, send Mudan. Strenna → **Hyperyton**. Decline Primrose's trigger (keep her for their turn).

End: Cactus, Kanzashi, Sacred Queen Strenna, **Hyperyton**, **Jasmine**, Konkon, set Sheet; Rikka Princess in the GY; Primrose + Black Princess in hand.

### Horus break: Petal + Mudan + Black Princess (going second)
Petal (add Primrose) → Black Princess → Mudan Tributes Petal (Konkon; Primrose + Hellebore) → Konkon sets Sheet → Mudan + Black Princess → Sacred Queen Strenna → Kanzashi → Primrose + Hellebore → Teardrop → Teardrop the Rikka Sacred Queen → **detach 2: send King's Sarcophagus + Walls**, Tribute Imsety. Then attack.

### Rikka Princess on field + Mudan + Sheet (going first)
Mudan Tributes Rikka Princess (Konkon) → Konkon sets Moonlit → Moonlit: Primrose, send Hellebore → Hellebore Tributes Mudan (Primrose + Black Princess) → Black Princess to Level 8 → Teardrop with Hellebore → set Sheet. Keep Primrose and both Ash.

## How to learn PredaRikka (practice plan)

1. **Learn the two halves separately.** Predap half: *starter → Lilizard → Bal Teah → Jasmine → Jasmine Tributes Byblisp → Petal or Black Princess*. Rikka half: *Mudan → Konkon → Sacred Queen Strenna → Rikka Queen Strenna (+Rikka Princess) → Tribute her → Hyperyton/Kanzashi + Sheet → Teardrop*. Jasmine is the bridge.
2. **EDOPro drills in order:** Line B (shortest) → Line A → Glamour → Instant Fusion → Predaprimitive (longest). Do each until you can finish it without reading the puzzle message.
3. **Say each step's purpose out loud** ("this Tribute triggers Primrose", "this detach puts Rikka Princess in the GY"). If you can't, that's the step to re-learn.
4. **Self-check after every board:** 2-3 Xyz? Sheet set? Rikka Princess in the GY? Cactus last? A Plant in hand for Kanzashi?
5. **Then going second:** the 10 random-hand puzzles. Before playing, write your order: Droplet → Tributes → Horus answer → Super Poly → Evenly Matched.

**Final vs-Natasha PredaRikka (45, 22 Nov 2026):** Droll 2, Petal 1, Byblisp 1, Longinephila 2, Dracaena 3, Maxx "C" 1, Ash 3, Lilizard 1, Cactus Bouncer 1, Rikka Princess 1, Fuwalos 1, Meowls 2, Mudan 2, Black Princess 3, Hellebore 1, Primrose 1, Instant Fusion 1, Glamour 2, Triple Tactics Talent 1 (was Thrust), Predaprimitive 3, Moonlit Waters 3, Konkon 1, Super Poly 2, Forbidden Droplet 1, Evenly Matched 1, Rikka Sheet 1, Dominus Impulse 3.
Monte Carlo (200k hands): brick going 1st 5.1%; going 2nd 2.5%; going 2nd with a Super Poly / Droplet route 86.6%; at least one hand trap for her turn 80.7%.

## Lewis's current PredaRikka list (deck "PredaRikka | 2026-11-21", screenshot 25 Nov 2026)

**Main Deck (45):**
- **Monsters (26):** Droll & Lock Bird 2, Rikka Petal 1, Predaplant Byblisp 1, Predaplant Longinephila 2, Princess Dracaena 3, Maxx "C" 1, Ash Blossom 3, Predaplant Lilizard 1, Cactus Bouncer 1, Rikka Princess 1, Mulcharmy Purulia 2, Mulcharmy Fuwalos 1, Mudan 2, Rikka Black Princess 3, Hellebore 1, Primrose 1.
- **Spells (14):** Instant Fusion 1, Rikka Glamour 2, Triple Tactics Talent 1, Predaprimitive 3, Rikka Moonlit Waters 3, Rikka Konkon 1, Super Polymerization 2, Forbidden Droplet 1.
- **Traps (5):** Evenly Matched 1, Rikka Sheet 1, Dominus Impulse 3.

**Extra Deck (15):** Predaplant Ambulomelides, Garura, Predaplant Daredevil, Starving Venom, Predaplant Bal Teah, **Crystal Wing Synchro Dragon**, Rikka Queen Strenna, Kanzashi, Rikka Sacred Queen Strenna, Orea the Sylvan High Arbiter, Teardrop the Rikka Queen ×2, Sacred Tree Beast Hyperyton, Teardrop the Rikka Sacred Queen, Aromaseraphy Jasmine.

Differences from the 22 Nov vs-Natasha list: Purulia ×2 back in for Mulcharmy Meowls ×2. Extra Deck now has Crystal Wing (still no Black Rose / Bramble Rose).

## PredaRikka sample hands

Card text checked against the Project Ignis card database (25 Nov 2026). The database uses the TCG names: **Rikka Sacred Queen Strenna = Rikka Empress Strenna**, **Moonlit Waters = Rikka June Moon**, **Teardrop the Rikka Sacred Queen = Teardrop the Rikka Empress**, **Primrose = Primrose the Twin Rikka Fairy**.

### Hand 1: Longinephila, Dracaena, Predaprimitive ×2, Konkon (going 2nd into Vision HERO Faris, no hand traps)

**Their board:** Vision HERO Faris (Level 5 DARK Warrior, 1600 ATK) only. Faris has no interruption: it only Special Summons itself and places a Vision HERO as a Continuous Trap. They were still in Main Phase 1 in the screenshot, so check what else they add.

**Key ideas:**
- **Konkon removes Faris for free.** Black Princess's cost Tributes a Plant you control; with Konkon up you Tribute Faris instead. No targeting, no destruction.
- **Longinephila's Predator Counter on Faris** is what lets **Byblisp** come back from the GY to be Jasmine's Tribute.
- **Only one Predaprimitive per turn.** The second copy is dead this turn (Super Poly discard later).
- **Dracaena sends Rikka Princess** so she's already in the GY as your negate on their turn.
- Do every Extra Deck summon that isn't a Plant Xyz **before** Moonlit Waters resolves (it locks you to Plant Xyz).

**Line (UNTESTED, from card text):**
1. **Predaprimitive:** send **Byblisp** from the Deck, add **Super Polymerization** (to set for later; you don't need it this turn). Plant/Dragon lock. **Byblisp (GY):** add **Lilizard**.
2. **Dracaena:** send **Rikka Princess** from the Deck, Special Summon Dracaena (now Level 4).
3. **Normal Summon Longinephila:** add a Predap card (Predaprimitive #3 is the only one left: Super Poly discard).
4. Special Summon **Lilizard** from hand (you control a Predaplant).
5. Synchro **Longinephila (Tuner, 1) + Lilizard (3)** → **Bal Teah** in a **Main Monster Zone** (keep the Extra Monster Zone free). **Bal Teah:** Lilizard from the GY, **draw 1**.
6. **Longinephila (GY):** banish it, put a **Predator Counter on Faris**.
7. Link **Bal Teah + Lilizard** → **Aromaseraphy Jasmine** in the **Extra Monster Zone** (its arrows point down-left and down-right).
8. **Byblisp (GY):** Special Summon it into a zone Jasmine points at.
9. **Jasmine:** Tribute Byblisp → **Rikka Black Princess** from the Deck.
10. **Konkon:** set **Moonlit Waters**.
11. **Black Princess:** Tribute **Faris** (Konkon's replacement) → **Mudan** from the Deck. **Mudan:** add **Glamour**. Their field is now empty.
12. Xyz **Mudan + Black Princess** → **Rikka Sacred Queen Strenna** (attack position). Detach 2 → **Rikka Queen Strenna** in Defence, attach **Petal** from the Deck.
13. **Moonlit Waters**, Tributing **Rikka Queen Strenna**: **Primrose** to hand, **Hellebore** to the GY. Chain: CL1 Rikka Queen Strenna → **Hyperyton** in attack position (attach Strenna); CL2 Sacred Queen Strenna → set **Rikka Sheet**.
14. **Hellebore (GY):** Tribute **Dracaena** → Hellebore. **Primrose** triggers → Primrose + **Black Princess #2** from the Deck.
15. **Primrose:** Black Princess #2 +2 (to 8). Chain **Hyperyton**: attach **Mudan** from the GY (monster material = negate a hand trap/monster effect).
16. Xyz **Black Princess #2 + Hellebore** → **Teardrop the Rikka Queen**.
17. **Battle:** Teardrop 2800 + Hyperyton 2600 + Sacred Queen Strenna 2000 + Jasmine 1800 = **9200 into an empty board: lethal.** If they keep a blocker, Teardrop detaches 1 to Tribute it (Quick, she has Plant material).

Monster Zones check: after step 14 you have Sacred Queen Strenna, Hyperyton, Hellebore, Primrose, Black Princess #2 (all 5) + Jasmine in the Extra Monster Zone. That's why Instant Fusion isn't in this line: Ambulomelides would take the 5th zone.

**If the game goes on:** Primrose (Def) stays for her Quick Effect on their turn (Teardrop → Teardrop the Rikka Sacred Queen), Rikka Princess negates from the GY, Hyperyton negates a monster effect, Rikka Sheet is set, Glamour + Super Poly + Predaprimitive in hand. Petal revives in their End Phase.

**If they extended past Faris:** same line to step 11 (Konkon takes their best face-up monster instead of Faris), then use Teardrop's Tribute and keep the attack for whatever is left.

### Hand 2: Droll, Dracaena, Cactus Bouncer, Moonlit Waters, Dominus Impulse (going 1st)

**Key ideas:**
- **Moonlit Waters alone is a full combo** (Line A above, proven). Cactus is already in hand, so you don't need Glamour to find it, and **Dracaena** is a spare Plant to Tribute.
- **Cactus Bouncer stops your own Special Summons too** (while any other Plant is on the field). So on their turn Primrose's Quick Xyz, Rikka Queen Strenna's float and Hellebore's revive are all off. Spend Primrose now: **Primrose + Hellebore → Teardrop**. Teardrop's Tribute doesn't summon, so it still works under Cactus.
- **Set Dominus Impulse** rather than holding it: from the hand it locks your LIGHT/EARTH/WIND effects for the rest of the Duel (Cactus is EARTH).

**Line (Line A steps are proven; the Dracaena / Teardrop changes are UNTESTED, from card text):**
1. **Dracaena:** send **Rikka Princess** from the Deck, Special Summon Dracaena (Level 4). Rikka Princess is now your GY negate.
2. **Moonlit Waters** (no Tribute): add **Mudan**, send **Black Princess** to the GY.
3. Special Summon **Black Princess** from the GY. **Black Princess:** Tribute herself → **Rikka Petal** from the Deck.
4. **Petal:** add **Primrose**.
5. **Mudan** (hand): Tribute **Petal** → Mudan. Chain: CL1 Mudan adds **Konkon**; CL2 **Primrose** → Primrose + **Hellebore** from the Deck.
6. **Konkon:** set **Glamour**.
7. **Primrose:** Hellebore Level -2 (to 6).
8. Xyz **Mudan + Hellebore** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach **Black Princess** from the Deck (Rikka Princess is already in the GY).
9. **Hellebore (GY):** Tribute **Rikka Queen Strenna** → Hellebore. Chain: CL1 Strenna → **Hyperyton** (attach Strenna); CL2 Sacred Queen Strenna → set **Rikka Sheet**.
10. **Glamour**, Tributing **Dracaena** (keep Sacred Queen Strenna on the field); **chain Hyperyton: attach Moonlit Waters** (a Spell). Glamour adds **Black Princess + Mudan #2** (both Level 6) for next turn.
11. Xyz **Primrose + Hellebore** (both Level 8) → **Teardrop the Rikka Queen**.
12. **Normal Summon Cactus Bouncer.** Set **Dominus Impulse**. Keep **Droll** in hand.

**End board:** Teardrop (Quick Tribute, Plant material), Hyperyton (monster + Spell material: negates a monster effect or a Spell), Sacred Queen Strenna, Cactus Bouncer, Konkon, set Rikka Sheet, set Dominus Impulse. Hand: Droll, Black Princess, Mudan. GY: Rikka Princess.

**Their turn, in order of what to use:**
- **Cactus means they can't Special Summon at all.** Their outs are: removing Cactus or all your other Plants, Normal Summons, and Spell/Trap effects.
- **Droll** after their first search.
- **Rikka Princess (GY)** negates a monster effect. Her Tribute can be **their** monster via Konkon.
- **Hyperyton** negates a monster effect or a Spell (e.g. Dark Hole, Raigeki, a field spell).
- **Teardrop** Tributes something (Quick). Each Tribute triggers **Sacred Queen Strenna** to set Rikka Sheet again from the GY.
- **Rikka Sheet** (Tribute a Plant): their monster can't use effects and you take it.
- **Dominus Impulse** for anything that Special Summons (backup if Cactus leaves).

If they **Ash Moonlit Waters**, you still have Dracaena: Normal Summon Cactus next to it for the lock, set Dominus Impulse, and hold Droll.

### Hand 3: Dracaena ×2, Triple Tactics Talent, Predaprimitive, Moonlit Waters (going 1st, vs "Sloth")

**Status: KNOWN-BAD order vs Droll (lost 25 Nov).** Leading with Predaprimitive gave Droll a target before Moonlit Waters had started. Corrected order: **Moonlit Waters first** (steps 2-7 below), then Predaprimitive. The rest of the line is still UNTESTED.

**Key ideas:**
- **Moonlit Waters is the engine** (Line A, proven). Dracaena is a spare Plant for Glamour's Tribute; Predaprimitive just banks Super Poly for later.
- **PredaRikka runs 1 Rikka Princess and 1 Lilizard** (the pure Rikka list ran 2 Princess). So when Sacred Queen Strenna attaches a Rikka monster, attach **Black Princess**, and leave Rikka Princess in the Deck for Glamour. Dracaena can't send Lilizard after Byblisp has searched it: send **Longinephila**.
- **Don't Special Summon Rikka Princess.** Her negate only works from the hand or GY; keep her in hand.
- **Triple Tactics Talent is dead on turn 1** (it needs them to activate a monster effect in *your* Main Phase). Keep it for turn 3.

**Line (UNTESTED as a whole; Line A steps are proven):**
1. **Predaprimitive:** send **Byblisp**, add **Super Polymerization**. Byblisp adds **Lilizard**.
2. **Moonlit Waters** (no Tribute): add **Mudan**, send **Black Princess** to the GY.
3. **Black Princess** from the GY; Tribute herself → **Petal**. **Petal:** add **Primrose**.
4. **Mudan:** Tribute Petal → Mudan. Chain: CL1 Mudan adds **Konkon**; CL2 **Primrose** → Primrose + **Hellebore**.
5. **Konkon:** set **Glamour**. **Primrose:** Hellebore -2 (to 6).
6. Xyz **Mudan + Hellebore** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach **Black Princess** from the Deck.
7. **Hellebore (GY):** Tribute Rikka Queen Strenna → Hellebore. Chain: Strenna → **Hyperyton**; Sacred Queen Strenna → set **Rikka Sheet**.
8. **Dracaena:** send **Longinephila**, Special Summon Dracaena.
9. **Glamour**, Tributing **Dracaena**; chain **Hyperyton: attach Moonlit Waters**. Add **Rikka Princess + Cactus Bouncer**.
10. Xyz **Primrose + Hellebore** → **Teardrop the Rikka Queen** (Cactus would stop Primrose's Quick Xyz on their turn anyway).
11. **Normal Summon Cactus Bouncer.** Set Triple Tactics Talent.

**End board:** Teardrop, Hyperyton (monster + Spell material), Sacred Queen Strenna, Cactus Bouncer, Konkon, set Rikka Sheet, set Triple Tactics Talent. Hand: **Rikka Princess** (negate), Dracaena #2, Lilizard, Super Poly. They can't Special Summon while Cactus and another Plant are up.

**Mistake I made live (25 Nov):** first version attached Rikka Princess in step 6 (then Glamour can't find her: 1 copy) and had Dracaena send Lilizard (already searched). Corrected within a minute; check copy counts before planning a search.

**What actually happened (25 Nov, vs Sloth):** Dracaena first, then Predaprimitive (Super Poly added) → **Droll** on Byblisp's search. Post-Droll line (UNTESTED, from card text):
1. **Triple Tactics Talent** is live (Droll is a monster effect in your Main Phase). Draw 2 is blocked by Droll, so **look at their hand and shuffle away the best card** (hand trap or starter).
2. ~~Moonlit Waters~~ **Master Duel won't let you activate Moonlit Waters under Droll** (it has to add a card). Tested 25 Nov.
3. **Black Princess** from the GY. Tribute **Dracaena** → **Mudan** from the Deck (Special Summons from the Deck still work under Droll; Mudan's search fails).
4. Xyz **Black Princess + Mudan** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach Rikka Princess (or Petal if she's already in the GY).
5. **Set Super Poly** (discard Dracaena #2 on their turn).

**What Lewis did instead:** Normal Summoned Dracaena #2 and linked both into **Sylvan Dancepione** (its excavate Special Summons, so Droll doesn't stop it), but they **Ash Blossom'd** it. Ended on Dancepione + set Super Poly, Moonlit Waters in hand as the discard. Right call: nothing else was live.

**Super Poly vs a Rikka opponent:** their Rikka monsters are all **WATER Plants**, so any two with different names → **Garura, Wings of Resonant Life** (2 monsters, same Type and Attribute, different names). Two of their monsters gone, no response, and you draw 1 when Garura hits the GY.

**Lesson:** vs a Droll player, do the **Moonlit Waters** combo first (Black Princess / Mudan are Special Summons from the GY/Deck) and save Predaprimitive's search for after Droll is gone. Every add in this deck (Byblisp, Petal, Mudan, Glamour) is a Droll target; Black Princess, Primrose, Hellebore, Strenna and Konkon's Set are not.

### Hand 4: Dracaena, Lilizard, Glamour ×2, Predaprimitive ×2 (going 2nd into Machina Fortress, vs bilotahn)

**Their board:** Machina Fortress (2500) only, no backrow, 3 cards in hand. Fortress punishes monster effects that **target** it (they discard a card from your hand) and **battle** (destroys one of your cards), so Tribute it without a target: **Glamour's Tribute through Konkon**. Longinephila's Predator Counter doesn't target either.

**Line (UNTESTED, from card text; same skeleton as Hand 1):**
1. **Predaprimitive:** send **Byblisp**, add **Super Poly**. Byblisp adds **Longinephila** (Lilizard is already in hand).
2. **Dracaena:** send **Rikka Princess**, Special Summon Dracaena.
3. **Normal Summon Longinephila** (search anything). Special Summon **Lilizard**.
4. Synchro **Longinephila + Lilizard** → **Bal Teah** (Main Monster Zone). Bal Teah: Lilizard from the GY, draw 1.
5. **Longinephila (GY):** Predator Counter on Fortress.
6. Link **Bal Teah + Lilizard** → **Jasmine** (Extra Monster Zone). **Byblisp** from the GY under Jasmine's arrow.
7. **Jasmine:** Tribute Byblisp → **Black Princess**. **Black Princess:** Tribute **Dracaena** → **Mudan**; Mudan adds **Konkon**.
8. **Konkon:** set **Moonlit Waters**.
9. **Glamour**, Tributing **Machina Fortress** via Konkon: add **Black Princess + Mudan** (both Level 6).
10. Xyz **Mudan + Black Princess** → **Sacred Queen Strenna**. Detach 2 → **Rikka Queen Strenna**, attach **Petal**.
11. **Moonlit Waters**, Tributing Rikka Queen Strenna: **Primrose** to hand, **Hellebore** to the GY. Strenna → **Hyperyton**; Sacred Queen → set **Rikka Sheet**.
12. Special Summon **Black Princess** from hand. **Hellebore (GY):** Tribute her → Hellebore. **Primrose** → Primrose + **Black Princess #3**.
13. **Primrose:** Black Princess #3 +2 (to 8). Xyz **Black Princess #3 + Hellebore** → **Teardrop**.
14. **Attack:** Teardrop 2800 + Hyperyton 2600 + Sacred Queen Strenna 2000 + Jasmine 1800 = **9200, lethal.**

Copy counts used: Black Princess 3/3, Mudan 2/2, Petal, Rikka Princess, Hellebore, Primrose, Byblisp, Lilizard (all 1/1), Longinephila 1/2.

**Predaprimitive's choice:** it adds **any "Polymerization" or "Fusion" Spell**: Super Poly or **Instant Fusion** (Lewis, 25 Nov). This line doesn't need either; pick Instant Fusion when you want Ambulomelides as an extra body/search, Super Poly for a no-response removal next turn.

**Live (25 Nov):** they **Ashed Predaprimitive**. The cost already sent Byblisp, so Byblisp's search (Longinephila) still happens and the rest of the line is unchanged: you only lose the Spell it would have added.

**Live, part 2:** **Ghost Belle** negated Bal Teah's Lilizard revive (no Lilizard, no draw). Fix (UNTESTED): **Byblisp** from the GY (Fortress has the counter) → Link **Bal Teah + Dracaena** → Jasmine; Jasmine Tributes Byblisp → Black Princess → Tribute herself → Mudan → Konkon → set Moonlit → **Glamour Tributes Fortress via Konkon** (Black Princess + Mudan) → Sacred Queen Strenna → Rikka Queen Strenna → Moonlit Tributes her (Hyperyton + Sheet, Primrose + Hellebore) → Hellebore Tributes Jasmine → Primrose + Black Princess → Teardrop. Attack for 7400 (not lethal).

**Rule we nearly broke:** **only 1 Rikka Glamour per turn** (and only 1 Moonlit Waters, 1 Predaprimitive). With 2 in hand, the second is a discard, not a second search.

**Fallback if you have no Longinephila (UNTESTED):** Dracaena (send Rikka Princess) → **Glamour** (no Tribute) adds Black Princess → Black Princess from hand, Tribute Dracaena → Mudan → Konkon → set Moonlit → Xyz Sacred Queen Strenna → Rikka Queen Strenna → **Moonlit Waters Tributing Fortress via Konkon** (Primrose + Hellebore; Sacred Queen sets Sheet) → **Normal Summon Lilizard**, Hellebore Tributes it → Primrose + Black Princess → Teardrop. Not lethal (Teardrop 2800 + Strenna 2000), but Fortress is gone.
