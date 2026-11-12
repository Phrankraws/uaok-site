"""Sales PDF for the 6 new BatMaine products. Reuses PAGES data from build_pages.py."""
import html, pathlib, sys
import segno

HERE = pathlib.Path(__file__).parent
src = (HERE / "build_batmaine_pages.py").read_text()
ns = {}
exec(src.split("\ndef page(p):")[0], ns)
PAGES = ns["PAGES"]
esc = lambda s: html.escape(s, quote=True)
OUT = pathlib.Path(sys.argv[1])
SITE = HERE.parent.resolve()                      # uaok-site, where the screenshots live
PDF_MAKES = {"dj.html": [0, 4, 5, 6]}             # 4 of the DJ page's 8 features fit on paper
PDF_TIER_ITEMS = {"dj.html": 2, "researcher.html": 2}                 # DJ page is the fullest
PDF_SKIP_PICS = {"kids-media/money-coins.jpg"}    # 2 game screens fit side by side

def qr_svg(url, color):
    q = segno.make(url, error="m")
    import io
    b = io.BytesIO()
    q.save(b, kind="svg", scale=4, border=1, dark=color, light="#ffffff", xmldecl=False, svgns=True)
    return b.getvalue().decode()

SHORT = {
 "researcher.html": ("BatMaineResearcher", "Big questions answered with proof", "Business owners making a big decision"),
 "avatar.html": ("BatMaineAvatar", "Social posts made and scheduled for you", "Businesses too busy to post"),
 "crm.html": ("BatMaineCRM", "Website + customer book in one", "Businesses with no real website yet"),
 "text-scheduling.html": ("BatMaine Text Scheduling", "Clients text a word and get booked", "Barbers, nail techs, salons"),
 "dj.html": ("BatMaine DJ App", "A DJ's own party app and website", "DJs who want more tips and bookings"),
 "kids-game.html": ("BatMaine Kids Learning Game", "Your child stars in their own game", "Parents of kids 3 to 8"),
}

css = """
@page{size:Letter;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{font:400 10.5pt/1.45 "Figtree",Helvetica,Arial,sans-serif;color:#141A2A;-webkit-print-color-adjust:exact;print-color-adjust:exact}
h1,h2,h3{font-family:"Syne","Avenir Next",sans-serif;margin:0;line-height:1.05}
p{margin:0}
.pg{width:8.5in;height:11in;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.pg:last-child{page-break-after:auto}
.mono{font:700 7.5pt/1 "JetBrains Mono",Menlo,monospace;letter-spacing:.14em;text-transform:uppercase}
/* cover */
.cover{background:#0D111C;color:#ECEFF7;padding:.8in .75in}
.cover .kicker{color:#9AA4BD}
.cover h1{font-size:46pt;font-weight:800;letter-spacing:-.02em;margin-top:22px}
.cover h1 em{font-style:normal;color:#FF4F57}
.cover .sub{font-size:14pt;color:#C9D0E2;margin-top:18px;max-width:5.6in}
.clist{margin-top:.45in;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.citem{border:1px solid #2A3247;border-radius:14px;padding:14px 16px;background:#161C2B;border-left:6px solid var(--a)}
.citem b{font:700 12pt "Syne",sans-serif;display:block}
.citem span{color:#9AA4BD;font-size:9.5pt}
.cover .foot{position:absolute;left:.75in;right:.75in;bottom:.6in;display:flex;justify-content:space-between;align-items:flex-end;color:#9AA4BD;font-size:9pt;border-top:1px solid #2A3247;padding-top:14px}
.cover .foot b{color:#ECEFF7}
/* product */
.band{background:var(--a);color:var(--ai);padding:.42in .6in .34in}
.band .mono{opacity:.85}
.band h2{font-size:27pt;font-weight:800;letter-spacing:-.015em;margin-top:10px}
.band .name{font:800 12pt "Syne",sans-serif;margin-top:6px;opacity:.95}
.body{padding:.26in .6in 0}
.lede{font-size:11pt;color:#3B4560}
.grid2{display:grid;grid-template-columns:1.1fr .9fr;gap:20px;margin-top:14px}
.box{border:1px solid #D5DBE6;border-radius:12px;padding:12px 14px}
.box .mono{color:#566079;margin-bottom:8px;display:block}
.row{display:grid;grid-template-columns:72px 1fr;gap:8px;padding:5px 0;border-top:1px solid #EEF1F6;font-size:9.3pt}
.row:first-of-type{border-top:0}
.row .k{font:700 6.8pt/1.7 "JetBrains Mono",monospace;letter-spacing:.1em;text-transform:uppercase;color:#566079}
.row b{color:var(--a)}
.chat{display:grid;gap:4px}
.bub{padding:4px 9px;border-radius:11px;background:#EEF1F6;font-size:8.3pt;line-height:1.3;max-width:92%}
.bub.me{background:var(--a);color:var(--ai);justify-self:end}
.feat{display:grid;gap:7px}
.pics{display:grid;gap:8px;grid-template-columns:repeat(3,1fr)}
.pics-third{grid-template-columns:repeat(2,1fr)}
.pics figure{margin:0;display:grid;gap:4px}
.pics img{width:100%;display:block;border-radius:8px;border:1px solid #D5DBE6}
.pics-phone img{aspect-ratio:390/700;object-fit:cover;object-position:top}
.pics-portrait img{aspect-ratio:4/5;object-fit:cover;object-position:center 30%}
.pics-third img{aspect-ratio:1.08;object-fit:cover;object-position:center 60%}
.pics figcaption{font:700 6.3pt/1.3 "JetBrains Mono",monospace;letter-spacing:.06em;text-transform:uppercase;color:#566079}
.bottom .t b.demo{display:inline;font:700 9pt "Figtree",sans-serif;color:var(--a)}
.feat div{font-size:9.2pt;color:#3B4560}
.feat b{display:block;color:#141A2A;font-size:9.8pt}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:14px}
.step{border-top:3px solid var(--a);padding-top:7px;font-size:8.8pt;color:#3B4560}
.step b{display:block;color:#141A2A;font-size:9.6pt;margin:2px 0 3px}
.step .n{font:800 15pt "Syne",sans-serif;color:var(--a)}
.tiers{display:grid;gap:10px;margin-top:14px}
.tier{border:1px solid #D5DBE6;border-radius:12px;padding:11px 13px;position:relative}
.tier.pick{border:2px solid var(--a)}
.tier .tag{position:absolute;top:-8px;right:12px;background:var(--a);color:var(--ai);font:700 6.5pt/1 "JetBrains Mono",monospace;letter-spacing:.1em;padding:4px 7px;border-radius:99px}
.tier h3{font-size:10.5pt}
.price{font:800 18pt/1.1 "Syne",sans-serif;margin-top:3px}
.price small{font:500 9pt "Figtree",sans-serif;color:#566079}
.tier .was{font-size:7.8pt;color:#566079;font-family:"JetBrains Mono",monospace}
.tier ul{margin:6px 0 0;padding-left:14px;font-size:8.5pt;color:#3B4560}
.tier li{margin:1px 0}
.bottom{position:absolute;left:.6in;right:.6in;bottom:.42in;display:flex;gap:16px;align-items:center;border-top:1px solid #D5DBE6;padding-top:12px}
.bottom svg{width:.95in;height:.95in;display:block}
.bottom .t b{font:800 11.5pt "Syne",sans-serif;display:block}
.bottom .t{font-size:9pt;color:#3B4560}
.bottom .addon{margin-left:auto;max-width:2.7in;font-size:8.6pt;color:#3B4560;border:1px dashed #9AA4BD;border-radius:10px;padding:8px 10px}
.bottom .addon b{color:#141A2A}
/* back */
.back{padding:.7in .7in}
.back h2{font-size:28pt;font-weight:800}
table{width:100%;border-collapse:collapse;margin-top:18px;font-size:9.6pt}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid #D5DBE6;vertical-align:top}
th{white-space:nowrap;font:700 7pt "JetBrains Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:#566079;background:#EEF1F6}
td.n{font-weight:700;white-space:nowrap}
td .sw{display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--a);margin-right:7px;vertical-align:-1px}
.how{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.how div{background:#EEF1F6;border-radius:12px;padding:12px 14px;font-size:9.4pt;color:#3B4560}
.how b{display:block;font:800 11pt "Syne",sans-serif;color:#141A2A;margin-bottom:4px}
.contact{margin-top:26px;background:#0D111C;color:#ECEFF7;border-radius:16px;padding:20px 24px;display:flex;gap:22px;align-items:center}
.contact svg{width:1.05in;height:1.05in;display:block;border-radius:8px}
.contact h3{font-size:16pt}
.contact p{color:#C9D0E2;font-size:10pt;margin-top:6px}
.mission{margin-top:18px;font-size:9pt;color:#566079}
"""

parts = ['<!doctype html><html><head><meta charset="utf-8"><title>BatMaine Products</title>',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap">',
         f'<style>{css}</style></head><body>']
w = parts.append

# cover
w('<section class="pg cover"><span class="mono kicker">UAOK Intellectual Property · New for 2026</span>')
w('<h1>Tools that work <em>while you work.</em></h1>')
w('<p class="sub">Six done-for-you products for small businesses, DJs and families. Built by Ultimate Advancement of Knowledge (UAOK), a nonprofit that trains and employs young people.</p>')
w('<div class="clist">')
for p in PAGES:
    n, line, _ = SHORT[p["file"]]
    w(f'<div class="citem" style="--a:{p["accent"][2]}"><b>{esc(n)}</b><span>{esc(line)}</span></div>')
w('</div><div class="foot"><span>Every product has its own page with prices and a buy button.<br>Scan the code on each page, or visit <b>uaok.org</b> → Intellectual Property.</span><span><b>info@uaok.org</b><br>uaok.org</span></div></section>')

for p in PAGES:
    a, ai = p["accent"][0], p["accent"][1]
    url = f'https://uaok.org/{p["file"][:-5]}'
    n, line, who = SHORT[p["file"]]
    w(f'<section class="pg" style="--a:{a};--ai:{ai}">')
    w(f'<div class="band"><span class="mono">{esc(p["label"])}</span><h2>{p["h1"].replace("<em>","").replace("</em>","")}</h2><div class="name">{esc(n)}</div></div>')
    w(f'<div class="body"><p class="lede">{esc(p["lede"])}</p><div class="grid2">')
    # left: real screenshots when the page has them, else the example
    if p.get("gallery"):
        pics = [g for g in p["gallery"] if g[0] not in PDF_SKIP_PICS][:3]
        w(f'<div class="box"><span class="mono">Real screens</span><div class="pics pics-{pics[0][3]}">')
        for src, alt, cap, kind in pics:
            w(f'<figure><img src="{(SITE / src).as_uri()}" alt="{esc(alt)}"><figcaption>{esc(cap)}</figcaption></figure>')
        w('</div></div>')
    elif p.get("chat"):
        w('<div class="box"><span class="mono">Example text</span><div class="chat">')
        for who_, msg in p["chat"]:
            w(f'<span class="bub{" me" if who_=="me" else ""}">{esc(msg).replace(chr(10),"<br>")}</span>')
        w('</div></div>')
    else:
        w('<div class="box"><span class="mono">Example</span>')
        for k, v in p["demo"]:
            w(f'<div class="row"><span class="k">{esc(k)}</span><span>{v}</span></div>')
        w('</div>')
    # right: features
    w(f'<div class="box"><span class="mono">{esc(p["makes_label"])}</span><div class="feat">')
    for h, d in [p["makes"][i] for i in PDF_MAKES.get(p["file"], range(4))]:
        w(f'<div><b>{esc(h)}</b>{esc(d)}</div>')
    w('</div></div></div>')
    # steps
    w('<div class="steps">')
    for i, (h, d) in enumerate(p["steps"], 1):
        w(f'<div class="step"><span class="n">{i}</span><b>{esc(h)}</b>{esc(d)}</div>')
    w('</div>')
    # tiers
    w(f'<div class="tiers" style="grid-template-columns:repeat({len(p["tiers"])},1fr)">')
    for t in p["tiers"]:
        w(f'<div class="tier{" pick" if t.get("pick") else ""}">' + ('<span class="tag">MOST PICKED</span>' if t.get("pick") else ""))
        w(f'<h3>{esc(t["name"])}</h3><div class="price">{t["price"]}</div><div class="was">{esc(t["was"])}</div><ul>')
        for it in t["items"][:PDF_TIER_ITEMS.get(p["file"], 4)]:
            w(f'<li>{esc(it)}</li>')
        w('</ul></div>')
    w('</div></div>')
    # bottom
    demo = p.get("live_demo")
    demo_line = (f'<br><b class="demo">Try the live demo:</b> {esc(demo["url"].replace("https://", ""))} · login {esc(demo["user"])} / {esc(demo["password"])}'
                 if demo else "")
    w(f'<div class="bottom">{qr_svg(url, a)}<div class="t"><b>Scan to see it and buy</b>{esc(url.replace("https://",""))}<br>Pay online by card. We reach out within 1 business day.{demo_line}</div>')
    if p.get("addon"):
        s, d = p["addon"][:2]
        w(f'<div class="addon"><b>{esc(s)}</b> {esc(d)}</div>')
    w('</div></section>')

# back page
w('<section class="pg back"><span class="mono" style="color:#566079">Which one fits?</span><h2 style="margin-top:10px">Pick the one that solves your problem.</h2>')
w('<table><thead><tr><th>Product</th><th>Best for</th><th>What it does</th><th>Starts at</th></tr></thead><tbody>')
for p in PAGES:
    n, line, who = SHORT[p["file"]]
    prices = [t["price"] for t in p["tiers"] if t["price"] != "$0"]
    start = prices[0].replace("<small>", "").replace("</small>", "")
    w(f'<tr style="--a:{p["accent"][0]}"><td class="n"><span class="sw"></span>{esc(n)}</td><td>{esc(who)}</td><td>{esc(line)}</td><td class="n">{start}</td></tr>')
w('</tbody></table>')
w('<div class="how"><div><b>1. Pick</b>Scan a product\'s code or go to uaok.org → Intellectual Property.</div><div><b>2. Pay</b>Choose your plan and pay online by card. Monthly plans cancel any time.</div><div><b>3. We start</b>We reach out within 1 business day and set it all up with you.</div></div>')
w(f'<div class="contact">{qr_svg("https://uaok.org/#contact", "#0D111C")}<div><h3>Questions first?</h3><p>Email <b>info@uaok.org</b> or send a message at <b>uaok.org</b>. Try the live CRM demo at uaok.org/crm, or ask about a free DJ App demo with your name on it.</p></div></div>')
w('<p class="mission">BatMaine products are made by Ultimate Advancement of Knowledge (UAOK), a nonprofit that trains and employs young people. Every sale supports that work. Prices are starting prices and can change. Not affiliated with Anthropic or any of the services the products connect to.</p>')
w('</section></body></html>')

OUT.write_text("".join(parts))
print("wrote", OUT)
