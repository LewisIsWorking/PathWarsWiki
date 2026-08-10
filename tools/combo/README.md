# tools/combo

Machine-checked combo routes for the Master Duel deck pages, currently Crystron Trains.

## What this is for

The Crystron pages were originally written from search snippets, and roughly a dozen card facts
were wrong. Two of the errors are the reason this tool exists, because neither was catchable by
proofreading:

- The page named **"Superior Dora"**. The card is **"Super Dora"**. A plausible wrong name reads
  as correct forever, because searching it just returns nothing and the reader assumes they mistyped.
- The page described the Machine Synchro lock and then recommended a Rank 10 Xyz **after** it,
  which the game does not allow. Nothing about the sentence looked wrong.

Both are now structurally impossible rather than merely reviewable. Card names come from a
generated closed vocabulary, and a route that Xyz summons after applying the Synchro lock fails
the check by construction.

## Contents

| File | What it does |
|---|---|
| `gen-cards.ps1` | Pulls the 48 cards in the reference decklists from `db.ygoprodeck.com` and writes the card vocabulary and facts into **both** models. Re-run after a decklist change. |
| `check-combos.ps1` | Runs every route through both models, diffs their findings, and enforces the folder README rule. This is the entry point. |
| `CUE-vs-Pkl.md` | Decision record: why both languages are here, what each is good at, and the correction that changed the verdict from "on correctness" to "on ergonomics". |
| `cue/` | The CUE model. See `cue/README.md`. |
| `pkl/` | The Pkl model. See `pkl/README.md`. |

## Running it

```powershell
.\tools\combo\check-combos.ps1            # validate
.\tools\combo\check-combos.ps1 -Verbose   # list every finding
.\tools\combo\gen-cards.ps1               # refresh the card data
```

Needs `cue` and `pkl` on PATH. Pkl is a single binary; drop `pkl.exe` in `~/.local/bin`.

## Why there are two models

Deliberate redundancy. A checker that silently under-reports is worse than no checker, because it
manufactures confidence, and CUE was caught doing exactly that (see Learnings). Running both and
requiring them to **agree** means each polices the other: the day either quietly stops checking
something, the diff goes red instead of the suite going quietly green.

Whether both survive long term is an open question. The runner is what will tell us.

## The ruleset both models encode

Card name is real; card is in the declared build's decklist; one Normal Summon per turn plus
grants; Synchro Tuner counts and material Levels totalling the result's Level; Xyz material counts
and shared Rank; Link material counts and Race; the Extra Deck lock in both its forms; once per
turn and once per Duel usage; and zone tracking, meaning the acting card is really in the zone the
step claims and materials are really on the field.

## Learnings

- **A wrong answer that arrives silently costs more than an error.** CUE's first zone fold applied
  only the first step and reported nothing, and that was believed long enough to get written into
  a README as a limitation of the language. It was a self-reference bug: in
  `#Fold & {in: list.Drop(in, 1)}`, the `in` on the right resolves to the field being defined on
  the left. Both models now agree on every finding with nothing excluded. Full account in
  `cue/README.md`.
- **"The tool cannot do X" deserves the same scepticism as any other claim.** Two attempts failed
  before the third worked. Recursion is genuinely out (CUE rejects it as a `structural cycle`), but
  indexed accumulation was there the whole time.
- **A guard must be proved by feeding it.** `RouteBroken` is a fixture carrying seven planted
  illegalities, and the runner asserts an exact problem count. If that count ever drops, a check
  has stopped working. Without the fixture the suite would go green either way.
- **Generated vocabularies beat review.** The `Superior Dora` class of error survives any number of
  careful readings and dies instantly to a closed disjunction of real names.
- **A README naming every file catches what presence and length miss.** Presence is a property of
  the file; accuracy is a property of its relationship to the directory. Naming is only half:
  it catches an *undocumented* file, not a *deleted* one, so backticked filenames must also exist.
- **Matching a claim is not the claim being legal.** The zone check asserted that a step's declared
  source zone matched the tracked one, so "Normal Summon Scrap Recycler from the deck" passed
  happily, because Recycler really was in the deck. Writing Route 6 surfaced it; a Normal Summon
  must now come from the hand.

## Known limits

The model checks **material legality**, not **effect legality**. It does not read card text, so it
cannot tell that Crystron Smiger's search must fetch a *Tuner*, or that Babeldecker's rank 10
effect needs the opponent to have activated something first. Writing a route that violates one of
those will pass. Activation conditions are likewise unchecked, which is why the Diagram Token in
Route 3 is described in prose rather than modelled.

What it does check is everything structural: names, deck membership, summon limits, material
composition, locks, usage limits, and whether each card was actually where the step claimed.
