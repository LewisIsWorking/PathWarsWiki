# Coaching tools

Used by the **master-duel-match-coach** skill.

- `cardtext.py`: card text from YGOPRODeck with a local cache (`cache/`). `./cardtext.py "Card A" "Card B"`, `--fuzzy` for partial names, `--refresh` after errata. When YGOPRODeck is blocked (the cloud container), it falls back to ProjectIgnis BabelCDB (TCG names are mapped, e.g. Sacred Queen Strenna).
- `scenarios.md`: real positions with the right answer and the mistake made at the time. Re-check the skill against them after changing it.

The combo-line checker is in `../line-check`.
