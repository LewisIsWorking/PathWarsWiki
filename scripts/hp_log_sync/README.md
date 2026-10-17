# hp_log_sync

Publishes every Path Wars campaign's HP and Stamina log from the ComeOnOverUno server
(`GET api/pathwars/campaigns/<code>/hp-history`, anonymous) as one page per campaign,
`<code>-HP-And-Stamina-Log.md` in the campaign's own topics folder, with an index under
`Writerside/topics/HP-And-Stamina-Logs/` and its own Writerside instance (`hp-logs.tree`). Added 2026-10-17 after
Daichi Kenshin's Stamina fell from 35 to 8 in C06 with no record of why. Tongs Browser posts every change; the
hourly workflow `.github/workflows/sync-hp-logs.yml` runs this.

- `hp_log_render.py`: one campaign's page, grouped by UTC day, one row per change: time, character, HP before and
  after, SP before and after, reason.
- `hp_log_pages.py`: finds each campaign's folder (`Cnn-*`, the one holding a page named after itself), fetches its
  history, and writes the pages, index and tree. Only campaigns with any history get a page.
- `test_hp_log_sync.py`: run by the workflow before it publishes anything.

## Learnings

- 2026-10-17: a failed fetch must never remove a page. A campaign the server could not answer for keeps the page it
  had; only an answer of "no changes" removes one. A 404 is a server older than `hp-history`, read as none yet.
- 2026-10-17: the server's text (names, reasons) goes through `_cell`: pipes, tags, `%` (Writerside variables),
  newlines and em dashes would otherwise break the table, the build or the zero-em-dash guard.
