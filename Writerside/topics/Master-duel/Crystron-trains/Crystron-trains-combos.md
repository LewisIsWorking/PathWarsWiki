# Crystron Trains combos

Every route here is MACHINE CHECKED. Each one exists as a model in `tools/combo`, in both CUE and
Pkl, and `tools/combo/check-combos.ps1` validates it against the Master Duel ruleset: material
levels, tuner counts, ranks, the extra deck locks, once per turn and once per Duel limits, and
whether every card was actually in the zone the step claims.

If you change a route here, change its model too. The checker verifies that every modelled route is
named on this page, so a route that exists in one place and not the other fails the build.

The deck itself is on [Crystron Trains](Crystron-trains.md). The engine is on [Crystron](Crystron.md).

Card text checked against the card database on 2026-08-09.
## Combos.

Every step below was checked against card text. Where a line depends on a card only one of the two
reference builds plays, it is tagged AMELIA BUILD or YUKINON BUILD. Both builds are listed in the
deck variants section of [Crystron Trains](Crystron-trains.md).

> How to read these.
>> - Each route is named after the card you OPEN with.
>> - "Locks Synchro" means Machine Synchro only for the turn. No Xyz, no Link.
>> - "Locks Machine" means Machine monsters only. Xyz and Link are still legal.
>> - Decide which lock you are accepting on your FIRST activation.
>> - ^ The two locks are explained on [Crystron Trains](Crystron-trains.md). Read that first.

### Starter quality.

> Starts on its own.
>> - Crystron Inclusion. The best one. Searches any Crystron, and is itself a Crystron card on the field.
>> - Exceptional Schedule. Searches, and manufactures Urgent Schedule's activation condition.
>> - Night Train Blue Traveler. Searches Switchyard, and its GY revive is two bodies.
>> - Crystron Smiger. One body into a Tuner from deck, but locks you out of Xyz.

> Needs a partner. Do not count these as starters.
>> - Scrap Recycler. Mills brilliantly but cannot convert a mill into a board by itself. See below.
>> - Crystron Sulfador. Needs a Crystron CARD already on your field to destroy.
>> - Crystron Sulfefnir. Needs a second Crystron card in hand to discard.
>> - Heavy Armored Knight Babeldecker. Needs an EARTH machine in hand, and its Xyz effect needs
>>   your opponent to have activated something, so it is a turn 2 card.
>> - Urgent Schedule. Needs your opponent to control more monsters than you.
>> - Revolving Switchyard. On its own it is one search.

### Route 1: Crystron Inclusion.

> Machine checked as `RouteInclusion.pkl` and its CUE twin.

The flagship one-card line. Nothing here is optional until step 6.

> Steps.
>> 1. Activate Crystron Inclusion -> add Crystron Sulfador from deck.
>> 2. Sulfador, from hand: target Crystron Inclusion, the Crystron card you control -> destroy it -> summon Sulfador.
>> 3. ^ Locks Machine. Xyz is still legal. Destroying your own Inclusion is the POINT, not a cost.
>> 4. Sulfador on summon: send 2 differently named Crystron cards from deck to GY -> send Tristaros and Sulfefnir.
>> 5. Inclusion is now in your GY. Banish it -> revive Crystron Tristaros.
>> 6. Sulfador (5) + Tristaros (2) = level 7 -> Synchro summon Crystron Eleskeletus.
>> 7. Eleskeletus on summon: add 1 Crystron card from GY or banishment -> take Inclusion back for next turn.
>> 8. Tristaros is in the GY as used material. Banish it -> destroy Eleskeletus -> summon 2 Crystrons from deck.
>> 9. Eleskeletus destroyed -> its float summons another Crystron from GY or banishment.
>> 10. You now hold three Crystron bodies and have not used your normal summon.

> Why it works.
>> - Inclusion is a Continuous SPELL, so it counts as "1 Crystron card you control" for Sulfador.
>> - Every destruction in this line is your own card, and each one turns on a float or a GY effect.

### Route 2: Night Train Blue Traveler.

> Machine checked as `RouteBlueTraveler.pkl` and its CUE twin.

> Steps.
>> 1. Discard Night Train Blue Traveler -> add Revolving Switchyard from deck.
>> 2. Activate Switchyard. Do NOT use a Switchyard effect yet, you only get one.
>> 3. Get a second EARTH machine into the GY. Normal summon Scrap Recycler -> send Derricrane to GY.
>> 4. Blue Traveler from GY: target Derricrane -> summon BOTH. Locks Machine, Xyz still legal.
>> 5. ^ ONCE PER DUEL. Not per turn. You never get this back.
>> 6. Two level 10 EARTH machines on the field.
>> 7. Now spend Switchyard. See the branch below.

> The Switchyard branch, and it is a real decision.
>> - Going FIRST: use effect B. Summon Flying Pegasus Railroad Stampede from deck, it becomes level 10.
>> - ^ Three level 10s, which is Gustav Rocket directly. The no-battle-damage clause costs nothing on turn 1.
>> - ^ AMELIA BUILD ONLY. Yukinon plays no level 4 EARTH machine with 1800+ ATK, so effect B has no target.
>> - Going SECOND and killing: use effect A instead. Send a card from hand -> add Babeldecker or Derricrane.
>> - ^ Effect B would switch off your own battle damage for the turn, even after Switchyard leaves the field.

### Route 3: Exceptional Schedule.

> Machine checked as `RouteSchedule.pkl` and its CUE twin.

The Diagram Token looks like a misplay. It is the activation condition.

> Steps.
>> 1. Activate Exceptional Schedule -> add Urgent Schedule from deck.
>> 2. Give your OPPONENT the Diagram Token. Level 10 EARTH machine, 3000/3000.
>> 3. They now control more monsters than you, which is exactly what Urgent Schedule requires.
>> 4. Urgent Schedule -> summon 1 level 4 or lower AND 1 level 5 or higher EARTH machine from deck, in defence.
>> 5. ^ Their effects are NEGATED. A Scrap Recycler summoned this way does NOT mill. Take Blue Traveler and Recycler for bodies, not effects.
>> 6. You may not attack with non-machines this turn. This deck has none, so it costs nothing.

> Dealing with the token you just gave away.
>> - You have handed your opponent a 3000 ATK body. Do not leave it there.
>> - Level 10 + Tristaros (2) = level 12 -> Synchro summon Centur-Ion Legatia.
>> - Legatia on summon: draw 1, then destroy the monster your opponent controls with the HIGHEST ATK.
>> - ^ At 3000 the Diagram Token is almost always the highest. You draw a card and take it straight back.
>> - Legatia is a Machine Synchro, so this line survives even the Synchro lock.

### Route 4: Crystron Smiger. The disruption plan.

> Machine checked as `RouteSmiger.pkl` and its CUE twin.

Take this line when you want an opponent's-turn board rather than damage.

> Steps.
>> 1. Normal summon Crystron Smiger.
>> 2. Target a face-up card you control -> destroy it -> summon 1 Crystron TUNER from deck.
>> 3. ^ Locks SYNCHRO. Xyz and Link are gone for the turn. This is the trade you are making.
>> 4. Build Machine Synchros and keep Tristaros in hand for your opponent's turn.
>> 5. Smiger from GY: banish it -> add 1 Crystron Spell/Trap from deck -> take Crystron Cluster.
>> 6. Set Cluster. Pass.

> What you are holding for their turn.
>> - Tristaros in hand: any activation they make turns into a summon from deck plus a Synchro.
>> - Cluster set: shuffle a Crystron from GY or banishment -> destroy 1 card, or 2 with a Crystron Synchro out.
>> - Therion "King" Regulus in hand, if you have it, is a free negate. See below.

### Route 5: Heavy Armored Knight Babeldecker. Turn 2 only.

> Machine checked as `RouteBabeldecker.pkl` and its CUE twin.

> Steps.
>> 1. Your opponent activated something on their turn, so Babeldecker's Xyz condition is live.
>> 2. Normal summon Babeldecker WITHOUT tributing.
>> 3. On summon -> special summon 1 EARTH machine from your HAND.
>> 4. Babeldecker alone -> Xyz summon a rank 10 EARTH machine using only itself as material.
>> 5. Rank 10 -> Juggernaut Liebe, using the rank 10 as material and transferring its materials.
>> 6. Detach for +2000 ATK. It attacks up to materials +1 times.

### Scrap Recycler is not a starter. Play it as an extender.

> What it actually does.
>> - Normal or special summoned -> send 1 MACHINE from deck to GY. This has NO once per turn clause.
>> - ^ So every time you re-summon it, you mill again. That is the engine.
>> - At 900 ATK it is Clockwork Knight material, and Clockwork Knight can revive it from the GY.

> Why it cannot start alone.
>> - Milling Sulfador does nothing, because Sulfador needs a Crystron card already on your field.
>> - Milling Blue Traveler does nothing until a second EARTH machine is in the GY.
>> - Linking Recycler away fixes that, but then you have no second machine to tribute for Clockwork Knight.
>> - Recycler plus any of Inclusion, Blue Traveler or Exceptional Schedule is excellent. Recycler alone is a body and a mill.

### Two-card upgrades.

> Inclusion plus Scrap Recycler.
>> - Run Route 1, but normal summon Recycler first and mill a second Crystron to deepen the GY.
>> - Recycler is also a spare Link body once its mill is spent.

> Blue Traveler plus Qliphort Genius on the field.
>> - Blue Traveler's revive summons TWO monsters at the same time.
>> - Genius: when 2 monsters are special summoned at once to its zones -> add 1 level 5 or higher machine from deck.
>> - ^ So make Genius BEFORE you use Blue Traveler's GY effect, never after. Ordering is the whole trick.

> Any line plus Therion "King" Regulus.
>> - Regulus is an EARTH MACHINE, so it fits every lock this deck applies.
>> - Target any machine in your GY -> summon Regulus from hand and equip that monster to it.
>> - Then, when your opponent activates anything: send 1 Therion monster card from hand or face-up field -> NEGATE.
>> - ^ Regulus is itself a Therion monster on your face-up field, so it can send ITSELF. That is a free negate on any board.

### Traps to avoid.

> Derricrane does NOT trigger off Barrage Blast. [YUKINON BUILD]
>> - Derricrane destroys only when detached "to activate that monster's effect", meaning the Xyz's own effect.
>> - Detaching it for Gustav Max's burn -> Derricrane destroys a card. Correct.
>> - Detaching it for Barrage Blast -> nothing. Barrage Blast is not the Xyz monster's effect.

> Do not use Switchyard effect B on a turn you want to attack for game.
>> - The no-battle-damage clause persists even after Switchyard leaves the field.

> Urgent Schedule negates what it summons.
>> - Do not plan on the summoned Recycler milling or the summoned Blue Traveler doing anything on summon.

> Blue Traveler's revive is once per DUEL.
>> - Spending it turn 1 for a rank 10 means it is gone for the rest of the game.

### Route 6: Flying Launcher into Barrage Blast. [YUKINON BUILD]

> Machine checked as `RouteFlyingLauncher.pkl` and its CUE twin.

> Steps.
>> 1. Any two level 10 monsters -> Xyz summon Superdreadnought Rail Cannon Flying Launcher.
>> 2. On Xyz summon: add 1 EARTH machine OR Barrage Blast from deck. Take Barrage Blast.
>> 3. Set Barrage Blast. It is a trap, so it is live from your opponent's turn onward.
>> 4. Flying Launcher also grants an EXTRA normal summon of a machine this Main Phase.
>> 5. ^ Use it on Babeldecker or a second Scrap Recycler. Free body, most people forget this line exists.
>> 6. Flying Launcher can also detach any number of materials -> destroy that many spells and traps.

> Why one copy of Barrage Blast is worth a slot.
>> - It is searchable off Flying Launcher, so the single copy behaves like more.
>> - Once per turn: detach any number from your Machine Xyz -> destroy that many cards on the field.
>> - From the GY, if your Machine Xyz is destroyed: banish it and a Machine Xyz from GY -> damage equal to Rank x 200.
>> - ^ Rank 10 is 2000. Rank 11 Liebe is 2200. Rank 12 AA-ZEUS is 2400.

