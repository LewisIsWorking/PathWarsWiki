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

## Zone tracking

Each step declares the zone it acts from and the zone it moves to, and `Combo.pkl` folds that
across the route to check the claim. This catches a line that looks legal and cannot actually be
executed: reviving a card still in the deck, or Xyz summoning with a material still in hand.

It is the single most valuable check here, because every other check validates a step in isolation
while this one validates the route as a *sequence*.

The CUE model now does this too, by indexed accumulation, and produces identical findings. An
earlier version of this README claimed CUE could not express the fold at all. That was wrong, and
the mistake is worth keeping visible: the first CUE attempt returned a wrong answer **silently**,
which is easy to mistake for a limitation of the tool rather than a bug in the code. See
`../cue/README.md` for what actually went wrong.

Pkl still writes it in three lines against CUE's twenty-odd, and Pkl's `fold` needs no explanation
to a reader. That is an ergonomics argument, not a capability one.

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
