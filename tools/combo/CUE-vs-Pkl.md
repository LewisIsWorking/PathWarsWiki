# CUE vs Pkl, and why both are still here

Decision record. Bake-off run 2026-08-10, corrected the same day.

Both models describe the **same ruleset** over the **same 48-card database** generated from one API
pull by `gen-cards.ps1`, and both emit an `errors` list checked by `check-combos.ps1`, so neither
is advantaged by how failures are surfaced.

## Verdict

**Pkl is the better tool for this, on ergonomics.** Both are fully capable.

That is a correction. The first verdict was "Pkl, on correctness", on the belief that CUE could not
accumulate state across a sequence. That belief was wrong and is the most useful thing this
exercise produced. See below.

## What each is good at

| | CUE | Pkl |
|---|---|---|
| Closed vocabulary from generated data | excellent | excellent |
| Per-item constraints (counts, levels, races) | excellent, byte-identical findings | excellent |
| State accumulated across a sequence | works, by **indexed** accumulation only | works, `fold` in three lines |
| Error messages | positional and terse | naming, custom strings |
| Lines for the same model | ~224 | ~160 |
| Already used elsewhere in the workspace | yes, `CooSource` | no |

## The correction, and why it matters more than the verdict

Three attempts at zone tracking in CUE:

1. **A recursive definition silently applied only the first step.**
   `#ZoneFold & {inSteps: list.Drop(inSteps, 1)}` looks right and is not: inside that struct
   literal, `inSteps` resolves to the field being defined **there**, not the outer one. A
   self-reference, so the tail was never passed. **No error.** Just a plausible wrong answer.
2. **Fixing the self-reference trips `structural cycle`.** Binding the tail to a `let` first makes
   the recursion real and CUE rejects the shape outright. Recursion genuinely is out.
3. **Indexed accumulation works.** A struct keyed by index where entry `i+1` derives from entry
   `i`. Finite keys, no recursion, nothing for the cycle detector to reject.

Attempt 1 was believed for long enough to be written into a README as a property of the language.
**A wrong answer that arrives quietly gets believed, and then gets documented.** "The tool cannot
do X" deserves the same burden of proof as any other claim.

## Why both are kept

Deliberate redundancy, and `check-combos.ps1` diffs their findings. Each model polices the other:
the day either silently stops checking something, the diff goes red instead of the suite going
quietly green. Given that one of them has already silently mis-computed once, that is not a
hypothetical.

The cost is that every route must be written twice and kept in sync. The diff is what makes that
cost buy something rather than just doubling the work.

## CUE friction worth knowing

None of this stopped the model being written; all of it cost time.

- `#Def & { ... }` cannot see `#Def`'s fields. References resolve **lexically**, not against the
  unified result, so helpers must live inside the definition that uses them.
- A missing map key is a **hard error** killing the whole evaluation rather than yielding a
  finding. Faking a fallback needs the keys materialised, a `list.Contains` guard, and the
  `[if cond {a}, b][0]` trick.
- No `distinct`; duplicates need a "report only at the first occurrence" count trick.
- No way to test an optional field for absence inside a comprehension, so `rules.cue` uses
  sentinel defaults where `Rules.pkl` uses nullable fields and `!= null`.
- Structs cannot be updated by unification. `acc & {x: "b"}` *fails* when `acc` has `x: "a"`, so
  every update rebuilds the struct via a comprehension copying the other keys.

## Pkl friction worth knowing

- Methods cannot be `hidden`; they are already excluded from output.
- Constraint violations **truncate the offending value** and fail fast on the first one, so a route
  with several problems would report one and hide the rest. Hence `errors` is emitted unconstrained
  and the runner asserts emptiness.
- A union type error prints the **entire** vocabulary, which is unreadable at 48 cards and worse at
  200. Use a membership constraint (`String(Cards.cards.containsKey(this))`) instead.

## What neither can do

Both check that a route you **declared** is internally consistent. Neither reads card text, so
neither knows whether an effect actually permits what a step claims. Out of reach for both: chain
resolution, priority windows, the opponent's responses, and whether a card's real effect allows the
summon written down.

Zone tracking does close part of that gap. Preconditions like "this card is in the GY by now" are
checked, which is what catches a plausible-looking line that cannot actually be executed.
