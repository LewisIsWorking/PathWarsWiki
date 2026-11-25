# Line checker (CUE)

Checks Master Duel combo lines as data before you try them in a game. It can't play the game; it checks the bookkeeping that went wrong in real games:

| Check | Real mistake it catches |
| --- | --- |
| A monster is used after it left the field | Horus game (24 Nov): Black Princess was Xyz material, then her effect was used |
| Deck counts | Rhino game 2 (25 Nov): Line B takes 2 Rikka Princess; PredaRikka runs 1 |
| Dark Law: nothing sent to your GY | Rhino game 3 (25 Nov): Predaprimitive can't be activated under Dark Law |
| Card is in the deck | Rhino game 3: Lilizard searches Polymerization; PredaRikka runs none |
| One Normal Summon, once-per-turn effects, summon locks, 5 Main Monster Zones | Cactus vs Longinephila, Predaprimitive's Plant/Dragon lock, Moonlit's Plant Xyz lock |
| Droll: no adds from the Deck once it resolves | Sloth game (25 Nov): Predaprimitive before Moonlit Waters |
| An Xyz effect that needs material still has some | Machina game (25 Nov): Rikka Queen Strenna summoned with no material, so no Hyperyton |
| Lethal: attackers on the end board, not summoned in Defence, ATK adds up | Hellebore / Primrose counted as attackers (Defence) |
| Locks already on at the start (`startLocks`) | Elfnote game (25 Nov): Cactus + their Strelitzia stop Instant Fusion and Super Poly too |
| Xyz materials match the Rank (after Primrose's Level change), Synchro has 1 Tuner and the Levels add up, Link material count | A forgotten Primrose Level change; a Synchro without a Tuner |

## Run it

Needs [CUE](https://cuelang.org) v0.11.1. `../coach/install-cue.sh` installs the release binary in about a second (`go install cuelang.org/go/cmd/cue@v0.11.1` also works but is slow).

```
./check.sh
```

Each line prints PASS or FAIL with its problems. During a match use `../coach/quick` instead (finds the line for a hand, checks one pasted line in under a second; see `../coach/README.md`). `known_bad` lines are mistakes from real games: they **pass** when the checker finds a problem, which proves the check works.

## Files

- `schema.cue`: what a line looks like and every check.
- `cards.cue`: card facts (Type, Level, effect names, which effects send to the GY). Effect names are short labels; every effect is once per turn unless listed in `notOpt`.
- `decks.cue`: deck lists (PredaRikka as saved 25 Nov 2026, RikkaM1).
- `lines_*.cue`: the lines. Same steps as the wiki pages.

## Adding a line

One step per action, in order. The fields that matter:

- `card`: the card (add `#2` for a second copy on the field at once).
- `action`: `normal_summon`, `special_summon`, `activate`, `effect`, `xyz`, `synchro`, `link`, `fusion`, `set`.
- `effect`: which of the card's effects (names in `cards.cue`).
- `zone`: where the card is (`field` by default; `hand`, `gy`, `deck`, `extra`).
- `consumes`: field monsters that leave in this step (Tributes, materials). Opponent's cards start with `opp:` (e.g. Konkon Tributing `opp:Masked HERO Dark Law`).
- `summons`: a monster this step summons when it isn't the step's own card.
- `fromDeck`: cards taken from the Deck (adds, sends, attaches, summons).
- `lock`: the summon lock the step applies (`plant`, `plant_or_dragon`, `extra_plant_xyz`, `no_special`).
- `setLevel`: Level changes, e.g. Primrose `{"Hellebore the Rikka Fairy": 6}`.
- `rankUp: true`: Xyz on top of another Xyz (Teardrop the Rikka Sacred Queen over Teardrop).
- `startField`: cards already on the field when the line starts (mid-turn positions).
- `darkLaw: true` / `drollFrom: <step>`: the opponent's Dark Law is up / Droll resolved before that step.
- `attach` / `detach`: materials attached to the step's `summons` (Sacred Queen Strenna's optional attach) / detached from the step's card. Rikka Queen Strenna's float fails with no material.
- `startLocks`: locks already on when the line starts, e.g. `["no_special"]` for Cactus Bouncer with any other Plant on either field.
- `lethal: {lp, attackers, bonus}`: optional damage check. Attackers must be on the end board and not summoned in Defence (Hellebore's revive, Primrose, Jasmine and Sacred Queen Strenna's summons are Defence; see `defEffects` in `cards.cue`). `bonus` adds ATK, e.g. `{"Teardrop: 1 Tribute": 200}`.

Hand-fitted lines from real games go in `lines_handfit.cue`. The going-first lookup table (one line per PredaRikka starter and the common 2-card pairs) is `lines_first.cue`.

Mark new lines `status: "untested"` until they've been played.
