"""One campaign's HP and Stamina log page, from the ComeOnOverUno server's hp-history.

Added 2026-10-17. Lewis: "Tongs should record all HP and stamina changes, with dates and reasons." In C06 Daichi
Kenshin's Stamina fell from 35 to 8 on 2026-09-01 with no record, Foundry's chat log was later cleared, and nobody
could say why. Tongs Browser now posts every change on a player character to the server; this renders them.

Pure: the changes are handed in, oldest first, as the server returns them.
"""

from collections import OrderedDict

EM_DASH = chr(0x2014)


def page_name(code: str) -> str:
    return f"{code}-HP-And-Stamina-Log.md"


def _cell(text) -> str:
    """Safe in a Markdown table cell and in Writerside: no pipes, tags, variables, newlines or em dashes."""
    text = str(text if text is not None else "")
    for old, new in ((EM_DASH, " - "), ("\r", " "), ("\n", " "), ("|", "/"), ("<", "&lt;"), (">", "&gt;"),
                     ("%", "&#37;")):
        text = text.replace(old, new)
    return text.strip()


def _pool(before, after, maximum) -> str:
    """"40 → 25 / 40", "? → 25 / 40" when the before is unknown, "-" without the pool."""
    if after is None:
        return "-"
    start = "?" if before is None else str(before)
    end = f"{after}" if maximum is None else f"{after} / {maximum}"
    return f"{start} → {end}"


def render_page(code: str, campaign_name: str, changes: list[dict]) -> str:
    out = [f"# {code} {campaign_name}: HP and Stamina log".replace("  ", " "), "",
           "Every change to a player character's Hit Points (HP) and Stamina Points (SP), rises and falls alike, "
           "recorded by Tongs Browser in the GM's Foundry and kept by the ComeOnOverUno server. Times are UTC. "
           "A \"?\" is a value Tongs did not know, because it first saw the character mid-change. "
           "\"manual change\" means no damage or healing card came with it, such as an edit to the sheet.", "",
           "Generated every hour from the server's record; do not edit by hand.", ""]
    by_day: "OrderedDict[str, list[dict]]" = OrderedDict()
    for change in changes:
        at = str(change.get("at") or "")
        by_day.setdefault(at[:10] or "unknown date", []).append(change)
    for day, rows in by_day.items():
        out += [f"## {day}", "", "| Time (UTC) | Character | HP | SP | Reason |", "|---|---|---|---|---|"]
        for change in rows:
            at = str(change.get("at") or "")
            out.append("| " + " | ".join([
                _cell(at[11:16] or "?"),
                _cell(change.get("character")),
                _cell(_pool(change.get("hpBefore"), change.get("hpAfter"), change.get("maxHp"))),
                _cell(_pool(change.get("spBefore"), change.get("spAfter"), change.get("maxSp"))),
                _cell(change.get("reason")),
            ]) + " |")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"
