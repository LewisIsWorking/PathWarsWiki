# Coaching tools

Used by the **master-duel-match-coach** skill.

## Live mode (during a match)

Every second counts: Master Duel's turn timer **and** the whole-duel clock. One tool does the checking: `./quick`.

**Once per container (5 seconds):**

```
git clone -q --depth 1 https://github.com/lewisisworking/pathwarswiki /tmp/pww && /tmp/pww/tools/coach/quick setup
```

`setup` installs CUE v0.11.1 as a release binary (about 1 s; `go install` is only the fallback), runs the full checker and warms the cache. Card text for the whole PredaRikka Main + Extra Deck and every opponent card in `opponents.txt` is already committed in `cache/`, so nothing needs the network during a game.

**On every screenshot (well under a second):**

| Need | Command |
| --- | --- |
| Best pre-checked line for this hand | `quick find mudan moonlit predap if ttt` |
| ...with cards already on your field | `quick find mudan sheet "2x ash" --field rp` |
| ...under Droll / Dark Law / Cactus lock | add `--droll`, `--darklaw`, `--cactus` |
| Card text (offline) | `quick card bp "dark law" zero` |
| A saved line's steps | `quick show "Line C"` |
| Check a line you just wrote | `quick check my.cue` or `quick check - <<'EOF' ... EOF` |
| Short names you can type | `quick names` (any unique part of a name works too) |

What `find` prints:

- **DON'T**: known mistakes from real games that this hand could repeat (the `known_bad` lines).
- The fitting checked lines, best first: the one using the most hand cards, proven before untested. The best one is printed in full as numbered steps, ready to send. A **CHECK SITUATION** line means the line assumed something different (Droll, Dark Law, Cactus lock).
- Lines written for the other deck (pure Rikka) are **re-checked for PredaRikka on the spot**: they show up only if they still pass, otherwise under "break here" with the reason (usually PredaRikka's single Rikka Princess).
- **NO CHECKED LINE FITS THIS HAND**: then there is no checked line. Say so. Write one as CUE (format in `../line-check/README.md`) and `quick check` it before sending, or give the shortest safe play marked UNCHECKED.

`check` accepts a whole `lines: "name": {...}` block or just the fields (`status`, `source`, `deck`, `hand`, `steps`, `end`). It names unknown cards with the closest real one, turns CUE's errors into "step 3.action: X isn't allowed. Allowed: ...", and prints the steps ready to send only when the line passes. Exit code 0 = pass.

Typical loop (timer over 60 s):

1. `quick find <hand> [--field ...]` → a line fits: send its numbered steps (one message, whole turn), plus the DON'Ts.
2. Nothing fits: adapt the closest line in a file, `quick check` it, fix until PASS, send.
3. Under 60 s or "FAST": no tools, one line (Speed sheet rules).
4. After the game: save the line in `../line-check/lines_handfit.cue`, mark proven / known_bad.

## Files

- `quick`, `quick.py`: the live-mode tool above. `install-cue.sh`: CUE installer (used by `quick`).
- `cardtext.py`: card text from YGOPRODeck with a local cache (`cache/`). `./cardtext.py "Card A" "Card B"`, `--fuzzy` for partial names, `--refresh` after errata. When YGOPRODeck is blocked (the cloud container), it falls back to ProjectIgnis BabelCDB (TCG names are mapped, e.g. Sacred Queen Strenna).
- `opponents.txt`: opponent cards kept in the cache. Add new ones after a game, then `quick precache` and commit `cache/`.
- `scenarios.md`: real positions with the right answer and the mistake made at the time. Re-check the skill against them after changing it.

The combo-line checker is in `../line-check`.
