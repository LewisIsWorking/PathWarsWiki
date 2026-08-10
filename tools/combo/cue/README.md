# tools/combo/cue

The CUE model of the Master Duel combo ruleset. The Pkl model in `../pkl` encodes the same rules;
`../check-combos.ps1` diffs their findings so neither can drift or silently stop checking.

Both models currently produce **identical** findings on every route, with nothing excluded.

## Contents

| File | What it does |
|---|---|
| `cards.cue` | **GENERATED** by `../gen-cards.ps1`. The closed `#CardName` vocabulary plus Level, Rank, Tuner, Race and Attribute for all 48 cards. Do not hand-edit. |
| `rules.cue` | **AUTHORED.** Material requirements per Extra Deck monster, transcribed by hand from each card's material line, plus both reference decklists. |
| `combo.cue` | The `#Step` and `#Route` schema, every check, and the indexed zone accumulation. Emits an `errors` list. |
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

**CUE can accumulate state across a sequence, but not by recursion.** This took three attempts and
the first two failed in interestingly different ways:

1. **A recursive definition silently applied only the first element.** `#Fold & {in: list.Drop(in, 1)}`
   looks right and is not: inside that struct literal, `in` resolves to the field being defined
   **there**, not the outer one. A self-reference, so the tail was never passed. No error, just a
   wrong answer. This is the worst failure mode a checker can have.
2. **Fixing the self-reference trips `structural cycle`.** Binding the tail to a `let` first makes
   the recursion real, and CUE then rejects it outright. Recursive definitions of this shape are
   not going to work.
3. **Indexed accumulation works.** A struct keyed by index, where entry `i+1` derives from entry
   `i`. Finite keys, no recursion, nothing for the cycle detector to reject.

The route is flattened into **atomic moves** first, because one step can move several cards (the
acting card plus every material). Accumulating over moves rather than steps keeps it to a single
accumulation instead of one nested inside another.

Other CUE friction, all still true and none of it present in the Pkl model:

- **`#Def & { ... }` cannot see `#Def`'s fields.** References resolve lexically, not against the
  unified result, so the zone logic had to move bodily inside `#Route`.
- **A missing map key is a hard error** that kills the entire evaluation rather than producing a
  finding. Faking a fallback needs the keys materialised, a `list.Contains` guard, and the
  `[if cond {a}, b][0]` trick.
- **No `distinct`.** Duplicate detection needs a "report only at the first occurrence" count trick.
- **No way to test an optional field for absence** inside a comprehension, so `rules.cue` uses
  sentinel defaults (`*99`) where the Pkl model uses nullable fields and `!= null`.

The general lesson is bigger than CUE: **a wrong answer that arrives silently costs more than an
error.** Attempt 1 looked like it worked, and was believed for a while.
