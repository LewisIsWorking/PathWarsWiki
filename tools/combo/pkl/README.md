# tools/combo/pkl

The Pkl model of the Master Duel combo ruleset. The CUE model in `../cue` encodes the same rules;
`../check-combos.ps1` diffs their findings so neither can drift or silently stop checking.

## Contents

| File | What it does |
|---|---|
| `Cards.pkl` | **GENERATED** by `../gen-cards.ps1`. The closed `CardName` vocabulary plus Level, Rank, Tuner, Race and Attribute for all 48 cards. Do not hand-edit. |
| `Rules.pkl` | **AUTHORED.** Material requirements per Extra Deck monster, transcribed by hand from each card's material line, plus both reference decklists. |
| `Combo.pkl` | The `Step` and `Route` classes and every check, including the zone fold. Emits an `errors` list. |
| `RouteInclusion.pkl` | Route 1 from the wiki page, the Crystron Inclusion one-card line. Expected to be clean. |
| `RouteBroken.pkl` | Fixture carrying seven planted illegalities, so the guards can be proved by feeding them. |

## Running it

Driven by `../check-combos.ps1`. Directly:

```powershell
pkl eval -f json .\pkl\RouteInclusion.pkl
```

Pkl is a single native binary. Put `pkl.exe` in `~/.local/bin`, which is already on PATH.

## What this model does that the CUE one cannot

**Zone tracking.** Each step declares the zone it acts from and the zone it moves to, and
`Combo.pkl` folds that across the route to check the claim. This is what catches a line that looks
legal and cannot actually be executed, for example reviving a card that is still in the deck, or
Xyz summoning with a material that is still in hand. CUE cannot express this fold at all, so its
sequential findings are reported but excluded from the diff.

That fold is the single most valuable check here, because every other check validates a step in
isolation while this one validates the route as a *sequence*.

## Why `errors` is unconstrained

`errors` is a plain `List<String>` rather than `List<String>(isEmpty)` on purpose. A constraint
violation is the natural Pkl idiom, but Pkl truncates the offending value in the error message and
fails fast on the first violated constraint, so a route with several problems would report one and
hide the rest. Emitting the list and letting the runner assert emptiness prints every problem in
full, which is the whole point.

## Learnings

- **Methods cannot be `hidden`.** `hidden function f()` is a parse error; methods are already
  excluded from output.
- **`getOrNull(x) ?? fallback` is the difference** between a checker that reports "card is in
  nowhere tracked" and one that dies. CUE has no equivalent and errors out instead.
- **Error strings are the deliverable.** Naming the card and the step ("step 4: xyz summon of
  Gustav Max is illegal, because Crystron Smiger applied the Machine Synchro lock at step 1") is
  worth more than any amount of type-level cleverness, because the person reading it is trying to
  fix a combo, not debug a schema.
