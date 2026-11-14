"""Builds the single-page phone cheat sheet (published as a claude.ai artifact).

Reads the same LINES / INDEX / RULES data as build.py, so the images and the page never drift.
Run from the repo root: python3 tools/invoked-cheatsheet/page.py
Writes tools/invoked-cheatsheet/out/invoked-cheat-sheet.html
"""
import os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build.py")).read()
src = src.split("from playwright.sync_api import sync_playwright", 1)[1]
src = src.split("\nimport os\nos.makedirs", 1)[0]
ns = {"re": re, "html": html}
exec("import os, re, html\n" + src.replace("__file__", repr(os.path.join(HERE, "build.py"))), ns)
LINES, INDEX1, INDEX2, INDEX3, RULES, VERSION, DATE, fmt = (ns[k] for k in ("LINES", "INDEX1", "INDEX2", "INDEX3", "RULES", "VERSION", "DATE", "fmt"))

DISCARD = [
    "Dead copies: 2nd Meltdown, an Invoke Sword when another is set, Sacred Sword after you've used one",
    "Mulcharmy Fuwalos (dead once you control cards)",
    "Infinite Impermanence, unless you'll set it",
    "Crossout Designator",
    "Ghost Belle",
]
KEEP = "Maxx \"C\", Ash, Super Poly, Droll, Nibiru, Ghost Ogre"
ATTR = [
    ("Ash, Zoroa", "FIRE", "Sorath"),
    ("Fuwalos, Droll, Aiwass", "WIND", "Sorath or Raidjin"),
    ("Maxx \"C\", Ghost Belle", "EARTH", "Baybarron"),
    ("Ghost Ogre, Nibiru, Spenta", "LIGHT", "Mechaba or Baybarron"),
    ("Crowley", "DARK", "Caliga or Oceanus"),
]

def line_section(L, ids):
    ids = [x["id"] for x in LINES if x.get("when") == L.get("when")]
    i = ids.index(L["id"])
    prev_id = ids[i - 1] if i > 0 else None
    next_id = ids[i + 1] if i < len(ids) - 1 else None
    untested = "UNTESTED" in L["tag"] or "Built from card text" in L["tag"]
    h = [f'<section class="view" id="v-line-{L["id"].lower()}" data-view="line-{L["id"].lower()}" hidden>']
    h.append(f'<header class="lh"><span class="badge">{L["id"]}</span><div><h2>{fmt(L["title"])}</h2>'
             f'<p class="tag{" warn" if untested else ""}">{fmt(L["tag"])}</p></div></header>')
    h.append('<div class="needs">' + "".join(f'<span class="chip">{fmt(n)}</span>' for n in L["needs"]) + "</div>")
    n = 1
    for name, steps in L["stages"]:
        h.append(f'<div class="stage"><h3>{fmt(name)}</h3><ol start="{n}">')
        for s in steps:
            h.append(f'<li><span>{fmt(s)}</span></li>')
            n += 1
        h.append("</ol></div>")
    h.append(f'<div class="end"><span class="k">End board</span>{fmt(L["end"])}</div>')
    if L.get("memo"):
        h.append(f'<div class="memo"><span class="k">Remember</span>{fmt(L["memo"])}</div>')
    nav = ['<nav class="pn">']
    nav.append(f'<a class="btn" href="#line-{prev_id.lower()}">← Line {prev_id}</a>' if prev_id else '<span></span>')
    nav.append('<a class="btn ghost" href="#">Which line?</a>')
    nav.append(f'<a class="btn" href="#line-{next_id.lower()}">Line {next_id} →</a>' if next_id else '<span></span>')
    nav.append("</nav>")
    h.append("".join(nav))
    h.append("</section>")
    return "\n".join(h)

def picks(idx):
    rows = []
    for hand, line, best in idx:
        rows.append(f'<a class="pick{" best" if best else ""}" href="#line-{line.lower()}"><span class="hand">{fmt(hand)}</span>'
                    f'<span class="go">{"Tip" if line.startswith("T") else "Line"} {fmt(line)}</span></a>')
    return "".join(rows)

def home_section():
    rules = "".join(f"<li><span>{fmt(r)}</span></li>" for r in RULES)
    disc = "".join(f"<li><span>{fmt(d)}</span></li>" for d in DISCARD)
    attr = "".join(f"<tr><td>{fmt(c)}</td><td><span class='at at-{a.lower()}'>{a}</span></td><td>{fmt(m)}</td></tr>" for c, a, m in ATTR)
    return f'''<section class="view" id="v-home" data-view="" hidden>
<h2 class="ht">Which line? Read your hand</h2>
<div class="seg" role="tablist">
<button type="button" id="tab-1st" role="tab" data-turn="1st" aria-selected="true">Going 1st</button>
<button type="button" id="tab-2nd" role="tab" data-turn="2nd" aria-selected="false">Going 2nd</button>
<button type="button" id="tab-tips" role="tab" data-turn="tips" aria-selected="false">Tips</button>
</div>
<div class="plist" data-turn="1st"><p class="tag">Strongest first: play the top row that fits. 10–11 only if you get Drolled, 12 if you bricked</p><div class="picks">{picks(INDEX1)}</div></div>
<div class="plist" data-turn="tips" hidden><p class="tag">Use alongside any line</p><div class="picks">{picks(INDEX3)}</div></div>
<div class="plist" data-turn="2nd" hidden><p class="tag">S1 on her turn. Then S2–S8, strongest first</p><div class="picks">{picks(INDEX2)}</div></div>
<div class="stage"><h3>Golden rules</h3><ol>{rules}</ol></div>
<div class="stage"><h3>Discard order (Madness, Mechaba, Super Poly, Spenta)</h3><ol>{disc}</ol>
<p class="keep"><b>Keep:</b> {fmt(KEEP)}</p></div>
<div class="stage"><h3>Aleister + a hand card makes</h3>
<div class="tw"><table class="attr"><thead><tr><th>Card</th><th>Attribute</th><th>Fusion</th></tr></thead><tbody>{attr}</tbody></table></div></div>
</section>'''

CSS = """
:root{
  /* Layout: one-screen views switched by #hash, sticky line strip on top, big tap targets for mid-duel use */
  --bg:#0d111c; --panel:#151c2e; --line:#26314f; --ink:#e9edf7; --muted:#97a3c2;
  --gold:#e0ad4a; --gold-ink:#1d1405; --name:#ffd77a; --arrow:#86b8ff;
  --end:#162a20; --end-line:#2d5a3f; --end-k:#80d69d; --memo:#231d33; --memo-line:#4a3a68; --memo-k:#c9a9ff;
  --warn:#f0a35e;
  --display:'Space Grotesk',Inter,system-ui,sans-serif; --body:Inter,system-ui,-apple-system,'Segoe UI',sans-serif;
  color-scheme:dark;
}
*{box-sizing:border-box}
html,body{background:var(--bg)}
body{color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.4;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 32px}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
.wrap{max-width:640px;margin:0 auto}
.strip{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:10px;border-bottom:1px solid var(--line);
  display:flex;flex-direction:column;gap:6px}
.strip a{min-width:38px;height:38px;padding:0 10px;border-radius:10px;display:inline-flex;align-items:center;justify-content:center;
  background:var(--panel);border:1px solid var(--line);color:var(--ink);text-decoration:none;font-weight:700;font-variant-numeric:tabular-nums}
.strip a.home{font-family:var(--display);padding:0 12px}
.strip a[aria-current="page"]{background:var(--gold);color:var(--gold-ink);border-color:var(--gold)}
.ver{margin-left:auto;font-size:12px;color:var(--muted)}
h2,h3{font-family:var(--display);text-wrap:balance;margin:0}
.ht{font-size:26px;margin-top:16px}
.lh{display:flex;gap:12px;align-items:center;margin-top:16px}
.badge{flex:none;width:52px;height:52px;border-radius:13px;background:var(--gold);color:var(--gold-ink);font:800 26px var(--display);
  display:flex;align-items:center;justify-content:center}
.lh h2{font-size:23px;line-height:1.15}
.tag{margin:4px 0 0;font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;font-weight:600}
.tag.warn{color:var(--warn)}
.needs{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0}
.chip{background:#1f2a46;border:1px solid #34446d;color:#d3e2ff;border-radius:999px;padding:5px 11px;font-size:14px;font-weight:600}
.stage{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:10px 14px 6px;margin-top:12px}
.stage h3{font-size:12px;color:var(--gold);text-transform:uppercase;letter-spacing:.08em;margin-bottom:4px}
ol{margin:0;padding:0;list-style:none;counter-reset:s}
ol[start]{counter-reset:s calc(var(--start,1) - 1)}
li{display:flex;gap:10px;padding:8px 0;border-top:1px solid #1e2843;counter-increment:s}
li:first-child{border-top:none}
li::before{content:counter(s);flex:none;width:26px;height:26px;border-radius:7px;background:#2a3961;font-weight:700;font-size:14px;
  display:flex;align-items:center;justify-content:center;margin-top:1px;font-variant-numeric:tabular-nums}
li span{min-width:0}
b{color:var(--name)} .arr{color:var(--arrow);font-weight:700}
.end{margin-top:12px;background:var(--end);border:1px solid var(--end-line);border-radius:14px;padding:10px 14px}
.memo{margin-top:10px;background:var(--memo);border:1px solid var(--memo-line);border-radius:14px;padding:10px 14px;font-size:16px}
.k{display:block;font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--end-k);margin-bottom:2px}
.memo .k{color:var(--memo-k)}
.pn{display:grid;grid-template-columns:1fr auto 1fr;gap:8px;margin-top:16px}
.pn .btn:last-child{justify-self:end}
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:44px;padding:0 14px;border-radius:12px;background:var(--panel);
  border:1px solid var(--line);color:var(--ink);text-decoration:none;font-weight:700}
.btn.ghost{color:var(--muted)}
.picks{display:flex;flex-direction:column;gap:8px;margin-top:12px}
.pick{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:12px 14px;border-radius:12px;background:var(--panel);
  border:1px solid var(--line);color:var(--ink);text-decoration:none;min-height:52px}
.pick.best{background:#2a2310;border-color:#6d5620}
.hand{min-width:0}
.go{flex:none;background:var(--gold);color:var(--gold-ink);border-radius:9px;padding:4px 10px;font-weight:800;white-space:nowrap}
.keep{margin:6px 0 8px;font-size:15px}
.tw{overflow-x:auto}
table.attr{width:100%;border-collapse:collapse;font-size:15px}
.attr th{text-align:left;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.06em;padding:4px 6px 6px 0}
.attr td{padding:7px 6px 7px 0;border-top:1px solid #1e2843;vertical-align:top}
.at{display:inline-block;border-radius:6px;padding:1px 7px;font-size:12px;font-weight:800;letter-spacing:.04em}
.at-fire{background:#5a2214;color:#ffb39a}.at-wind{background:#163f2b;color:#9ff0c0}.at-earth{background:#43361a;color:#f2d79a}
.at-light{background:#46421c;color:#fff2a6}.at-dark{background:#2e2147;color:#d6c0ff}
a:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.seg{display:grid;grid-template-columns:1fr 1fr auto;gap:6px;margin-top:12px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:4px}
.seg button{min-height:44px;padding:0 14px;border:0;border-radius:9px;background:transparent;color:var(--muted);font:700 16px var(--display);cursor:pointer}
.seg button[aria-selected="true"]{background:var(--gold);color:var(--gold-ink)}
.seg button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
.strip .lbl{font-size:11px;font-weight:800;letter-spacing:.06em;color:var(--muted);text-transform:uppercase;width:30px}
.strip .row{display:flex;flex-wrap:wrap;gap:6px;align-items:center;width:100%}
.foot{margin-top:18px;font-size:12px;color:var(--muted);text-align:right}
"""

def build():
    ids = [L["id"] for L in LINES]
    first = [L["id"] for L in LINES if L.get("when") == "1st"]
    second = [L["id"] for L in LINES if L.get("when") == "2nd"]
    tips = [L["id"] for L in LINES if L.get("when") == "tips"]
    strip = ('<div class="row"><span class="lbl">1st</span><a class="home" href="#">?</a>' +
             "".join(f'<a href="#line-{i.lower()}" data-v="line-{i.lower()}">{i}</a>' for i in first) + '</div>' +
             '<div class="row"><span class="lbl">2nd</span>' +
             "".join(f'<a href="#line-{i.lower()}" data-v="line-{i.lower()}">{i}</a>' for i in second) +
             '</div><div class="row"><span class="lbl">Tips</span>' +
             "".join(f'<a href="#line-{i.lower()}" data-v="line-{i.lower()}">{i}</a>' for i in tips) +
             f'<span class="ver">v{VERSION} · {DATE}</span></div>')
    body = "\n".join([home_section()] + [line_section(L, ids) for L in LINES])
    js = """
(function(){
  var views=[].slice.call(document.querySelectorAll('.view'));
  var links=[].slice.call(document.querySelectorAll('.strip a'));
  function show(){
    var h=(location.hash||'').replace('#','');
    var found=views.some(function(v){return v.dataset.view===h});
    if(!found) h='';
    views.forEach(function(v){v.hidden=v.dataset.view!==h});
    links.forEach(function(a){ if((a.dataset.v||'')===h) a.setAttribute('aria-current','page'); else a.removeAttribute('aria-current'); });
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',show); show();
  var tabs=[].slice.call(document.querySelectorAll('.seg button'));
  var lists=[].slice.call(document.querySelectorAll('.plist'));
  function setTurn(t){
    tabs.forEach(function(b){b.setAttribute('aria-selected', b.dataset.turn===t ? 'true':'false')});
    lists.forEach(function(l){l.hidden = l.dataset.turn!==t});
    try{localStorage.setItem('turn',t)}catch(e){}
  }
  tabs.forEach(function(b){b.addEventListener('click',function(){setTurn(b.dataset.turn)})});
  var saved='1st'; try{saved=localStorage.getItem('turn')||'1st'}catch(e){}
  setTurn(saved);
  document.querySelectorAll('ol[start]').forEach(function(o){o.style.setProperty('--start',o.getAttribute('start'))});
})();
"""
    page = f"""<title>Invoked Cheat Sheet</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Space+Grotesk:wght@600;700;800&display=swap">
<style>{CSS}</style>
<div class="wrap">
<nav class="strip" aria-label="Lines">{strip}</nav>
{body}
<p class="foot">Invoked cheat sheet · v{VERSION} · {DATE} · source: PathWarsWiki</p>
</div>
<script>{js}</script>
"""
    out = os.path.join(HERE, "out")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "invoked-cheat-sheet.html")
    open(path, "w").write(page)
    print(path)

def sync_wiki():
    p = os.path.join(HERE, "..", "..", "Writerside", "topics", "Master-duel", "Invoked-practice.md")
    s = open(p).read()
    gen = []
    for L in LINES:
        kind = "Tip" if L.get("when") == "tips" else "Line"
        when = "tips & tricks" if L.get("when") == "tips" else f"going {L.get('when')}"
        gen.append(f"## {kind} {L['id']}: {L['title']} ({when}; {L['tag']})\n\nNeeds: {', '.join(L['needs'])}.\n")
        n = 1
        for name, steps in L["stages"]:
            gen.append(f"\n**{name}**\n")
            for st in steps:
                gen.append(f"{n}. {st}\n"); n += 1
        gen.append(f"\n**End:** {L['end']}\n")
        if L.get("memo"):
            gen.append(f"\n**Remember:** {L['memo']}\n")
        gen.append("\n")
    a = s.index("## Line 1:"); b = s.index("## Discard priority")
    s = s[:a] + "".join(gen) + s[b:]
    a = s.index("| Your hand has | Play |"); b = s.index("\n\n", a)
    table = "| Going | Your hand has | Play |\n| --- | --- | --- |\n" + "\n".join(
        f"| {w} | {h} | Line {l}{' (best)' if best else ''} |" for w, idx in (("1st", INDEX1), ("2nd", INDEX2), ("tips", INDEX3)) for h, l, best in idx)
    s = s[:a] + table + s[b:]
    s = re.sub(r"!\[invoked-line-[^\]]+\]\([^)]*\)\n?", "", s)
    base = f"https://raw.githubusercontent.com/LewisIsWorking/PathWarsWiki/main/Writerside/images/invoked-cheatsheet/v{VERSION}/"
    s = re.sub(r"!\[invoked-0-which-line\]\([^)]*\)", f"![invoked-0-which-line]({base}invoked-0-which-line.png)\n" +
               "\n".join(f"![invoked-line-{L['id']}]({base}invoked-line-{L['id']}.png)" for L in LINES), s)
    s = re.sub(r"\*\*Current version: v[\d.]+ \([^)]*\)\.\*\*", f"**Current version: v{VERSION} ({DATE}).**", s)
    open(p, "w").write(s)
    print("wiki synced")

build()
sync_wiki()
