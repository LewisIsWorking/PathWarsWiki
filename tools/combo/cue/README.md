# tools/combo/cue

The CUE model of the Master Duel combo ruleset. The Pkl model in `../pkl` encodes the same rules;
`../check-combos.ps1` diffs their findings so neither can drift or silently stop checking.

## Contents

| File | What it does |
|---|---|
| `cards.cue` | **GENERATED** by `../gen-cards.ps1`. The closed `#CardName` vocabulary plus Level, Rank, Tuner, Race and Attribute for all 48 cards. Do not hand-edit. |
| `rules.cue` | **AUTHORED.** Material requirements per Extra Deck monster, transcribed by hand from each card's material line, plus both reference decklists. |
| `combo.cue` | The `#Step` and `#Route` schema and every check. Emits an `errors` list. |
| `zonefold.cue` | The recursive fold used for zone tracking, plus the findings that document why it does not work. |
| `route_inclusion.cue` | Route 1 from the wiki page, the Crystron Inclusion one-card line. Expected to be clean. |
| `route_broken.cue` | Fixture carrying seven planted illegalities, so the guards can be proved by feeding them. |

## Running it

Driven by `../check-combos.ps1`. Directly:

```powershell
cue export .\cue\*.cue -e routeInclusion.errors
```

## Why the generated and authored halves are separate

Card facts can be pulled from a database and must never be hand-typed. Material requirements
cannot: "2 or more Tuners + 1 non-Tuner monster" is prose that no parser should be trusted to read,
so it is transcribed by a human into `rules.cue`. Mixing the two would mean regenerating over
authored data.

## Learnings

Everything here was discovered building this model, and all of it is CUE-specific friction that the
Pkl model did not have:

- **CUE cannot fold state across a sequence, and it fails SILENTLY.** A struct fold over three
  updates returns the first one's result with no error. `list.Reduce` does not exist; the stdlib
  offers only fixed aggregations. Structs cannot be updated by unification, because `acc & {x: "b"}`
  *fails* when `acc` already has `x: "a"` (unification intersects, it never overwrites), so each
  update must rebuild the whole struct. Recursive definitions are the only workaround and they do
  not work; tried with both hidden (`_steps`) and regular (`inSteps`) field names.
- **`#Def & { ... }` cannot see `#Def`'s fields.** References resolve lexically, not against the
  unified result, so the zone logic could not be bolted on as a separate definition and had to move
  bodily inside `#Route`.
- **A missing map key is a hard error** that kills the entire evaluation rather than producing a
  finding. Faking a fallback needs the keys materialised, a `list.Contains` guard, and the
  `[if cond {a}, b][0]` trick.
- **No `distinct`.** Duplicate detection needs a "report only at the first occurrence" count trick.
- **No way to test an optional field for absence** inside a comprehension, so `rules.cue` uses
  sentinel defaults (`*99`) where the Pkl model uses nullable fields and `!= null`.

CUE was byte-identical to Pkl on every non-sequential check. The friction is entirely about state.
