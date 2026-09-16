# campaign_timeline: where each campaign went, and for how long

Lewis, 2026-09-16: a timeline of every campaign built from the bot's
transcripts. Each node is a location, measured on two scales, IRL time and
in-game time, with the events that happened there. It scrolls **down**.

Pilot: **C04 Magni Guard**, published at
`Writerside/topics/C04-The-Magni-Guard/C04-Magni-Guard-Timeline.md`.

## How it works

| Step | Script | Model? |
|---|---|---|
| 1. Read the archive into numbered messages, per month | `messages.py` | no |
| 2. Split each month into scenes by location | `extract.py` | **yes**, a free model via the `delegate` skill |
| 3. Check the split, then save it | `scenes.py` | no |
| 4. Merge scenes into visits and write the page | `page.py`, `page_render.py` | no |

**The model's output is never trusted on its word.** A month is rejected,
retried once, and otherwise left out if its scenes do not cover every
message exactly once and in order. Time cues are kept only if they are real
quotes from that month's posts. Nothing is estimated.

## Running it

Extraction needs the local `delegate` skill, so it runs on Lewis's machine,
not in CI. It only sends months that are new or have grown.

```bash
python scripts/campaign_timeline/extract.py \
  --source ../telegram-pbp-reminder/data/pbp_logs/Magni_Guard \
  --code C04 --name "Magni Guard" --data timelines/C04-Magni-Guard.json

python scripts/campaign_timeline/page.py \
  --source ../telegram-pbp-reminder/data/pbp_logs/Magni_Guard \
  --data timelines/C04-Magni-Guard.json \
  --page Writerside/topics/C04-The-Magni-Guard/C04-Magni-Guard-Timeline.md
```

## Editing by hand

The data file `timelines/<code>-<campaign>.json` has two sections for the GM:

```json
"in_game": { "2026-06#14": "2 days", "2026-07#1": "3h" },
"renames": { "The Big Atrium": "The Atrium" }
```

- **`in_game`**: keyed by the visit id the page prints under each visit.
  Write `3 days`, `2d 4h`, `1 week and 2 hours`, `90 mins`. Text it can't
  read (`about a week`) is shown as written, with no bar.
- **`renames`**: fixes a place the model named two ways. Renaming one name
  to another also merges back-to-back visits to it.

Then run `page.py` again. Neither section is touched by `extract.py`.

## The scales

- **IRL** runs from a visit's first post to the next visit's first post, so
  the wait between posts counts. That is what a scene really costs.
- **Bars** are relative to the longest visit on the same page, 10 cells each.

## Tests

```bash
python -m pytest scripts/pbp_sync scripts/campaign_timeline -q
```

⚠️ Run both suites together, as above. The renderer is `page_render.py`, not
`render.py`: pbp_sync already has a `render` module, and in one pytest run
the two collided and this suite failed to import.
