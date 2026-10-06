"""Daksh profile README builder.
Put your photo in photos/ as main.png (transparent cutout looks best) or main.jpg,
then run:  python build.py   -> regenerates assets/*.svg with the photo embedded."""
import re, base64, os, glob
H = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(H, "fonts.css")).read()

def photo():
    for f in glob.glob(os.path.join(H, "photos", "main.*")):
        m = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}[f.rsplit(".", 1)[1].lower()]
        return f"data:{m};base64," + base64.b64encode(open(f, "rb").read()).decode()

CSS = FONTS + """text{font-family:Display,sans-serif;font-weight:700;fill:#f2f5ff}.m{font-family:Mono,monospace;font-weight:400}
.e{animation:en 1s cubic-bezier(.16,1,.3,1) both}.p{animation:pu 2.4s ease-in-out infinite}.f{animation:fl 6s ease-in-out infinite}
@keyframes en{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}@keyframes pu{50%{opacity:.3}}@keyframes fl{50%{transform:translateY(-7px)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}"""

def card(name, w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Daksh Vasani - {name}"><style>{CSS}</style>
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#8bc6ff"/><stop offset=".5" stop-color="#247bff"/><stop offset="1" stop-color="#1240bd"/></linearGradient>
<linearGradient id="hl"><stop stop-color="#247bff" stop-opacity=".7"/><stop offset=".5" stop-color="#567394" stop-opacity=".25"/><stop offset="1" stop-color="#ff354f" stop-opacity=".65"/></linearGradient>
<radialGradient id="h1"><stop stop-color="#1266ed" stop-opacity=".38"/><stop offset="1" stop-color="#1266ed" stop-opacity="0"/></radialGradient>
<radialGradient id="h2"><stop stop-color="#ff1c3f" stop-opacity=".22"/><stop offset="1" stop-color="#ff1c3f" stop-opacity="0"/></radialGradient>
<pattern id="d" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#99b1db" opacity=".13"/></pattern>
<clipPath id="o"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="24"/></clipPath></defs>
<g clip-path="url(#o)"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="#070b16" stroke="url(#hl)"/><rect width="{w}" height="{h}" fill="url(#d)"/>
<ellipse cx="{w-250}" cy="{h/2}" rx="400" ry="380" fill="url(#h1)"/><ellipse cx="{w}" cy="0" rx="300" ry="260" fill="url(#h2)"/>{body}</g></svg>'''

def slashes(x, y):
    return '<g fill="#ff354f" class="p">' + "".join(f'<path d="M{x+i*16} {y}h10l-8 18h-10z"/>' for i in range(3)) + '</g>'

def top(l, r, w):
    return (f'<text class="m" x="44" y="46" font-size="13" letter-spacing="2" style="fill:#7f8fae">{l}</text>'
            f'<text class="m" x="{w/2}" y="46" font-size="13" letter-spacing="2" style="fill:#7f8fae">{r}</text>'
            f'{slashes(w-114,32)}<path d="M44 76H{w-44}" stroke="#1b2740" stroke-width="2"/>')

# ---------- HERO ----------
ph = photo()
if ph:
    pic = (f'<clipPath id="pc"><rect x="690" y="90" width="510" height="550"/></clipPath>'
           f'<image href="{ph}" x="690" y="90" width="510" height="550" preserveAspectRatio="xMidYMax slice" clip-path="url(#pc)"/>')
else:
    pic = ('<circle cx="940" cy="330" r="170" fill="#0c1730" stroke="url(#hl)" stroke-width="2"/>'
           '<text x="940" y="372" font-size="120" text-anchor="middle" style="fill:#247bff">DV</text>'
           '<text class="m" x="940" y="530" font-size="13" text-anchor="middle" letter-spacing="2" style="fill:#7f8fae">PHOTO SLOT: photos/main.png</text>')
hero = top("DV / DATA SCIENCE STUDENT", "MSc · MACHINE LEARNING", 1200) + f'''
<g class="e"><rect x="44" y="104" width="170" height="30" rx="6" fill="#102441"/><text class="m" x="60" y="124" font-size="12" letter-spacing="1.5" style="fill:#a9c6f5">OPEN TO COLLABS</text><circle class="p" cx="232" cy="119" r="5" fill="#3b8cff"/>
<text class="m" x="46" y="176" font-size="22" style="fill:#9fb0cf">Hi there, I'm</text>
<text x="40" y="292" font-size="140" textLength="330" lengthAdjust="spacingAndGlyphs">DAKSH</text>
<text x="40" y="412" font-size="140" style="fill:url(#g)" textLength="440" lengthAdjust="spacingAndGlyphs">VASANI</text>
<text x="500" y="372" font-size="34">LEARN.</text><text x="500" y="404" font-size="34">BUILD. SHIP.</text>
<text x="46" y="460" font-size="30">MSc Data Science</text>
<text class="m" x="46" y="500" font-size="17" style="fill:#9fb0cf">Turning raw data into insights &amp;</text><text class="m" x="46" y="526" font-size="17" style="fill:#9fb0cf">intelligent ML / AI systems.</text>
<path d="M44 560H640" stroke="#1b2740" stroke-width="2"/>
<text class="m" x="46" y="598" font-size="14" style="fill:#9fb0cf">▸ Python</text><text class="m" x="200" y="598" font-size="14" style="fill:#9fb0cf">▸ Machine Learning</text><text class="m" x="420" y="598" font-size="14" style="fill:#9fb0cf">▸ 6 projects</text></g>
<g class="f">{pic}</g>
<g><rect x="880" y="548" width="270" height="62" rx="12" fill="#0a1226" stroke="#24447a"/>{slashes(896,566)}<text x="960" y="574" font-size="19">DATA SCIENCE / ML</text><text class="m" x="960" y="596" font-size="12" style="fill:#7f8fae">@VASANI007</text></g>'''

# ---------- STACK ----------
chips = ["Python", "R", "Django", "Streamlit", "Scikit-learn", "Pandas", "MySQL", "MongoDB",
         "Git / GitHub", "HTML · CSS · JS", "Deep Learning", "Explainable AI"]
b = top("DV / STACK", "TOOLS I BUILD WITH", 1200) + '<text x="44" y="150" font-size="54">MY <tspan style="fill:url(#g)">STACK</tspan></text>'
for i, c in enumerate(chips):
    x, y = 44 + (i % 4) * 288, 190 + (i // 4) * 108
    col = "#ff354f" if i % 5 == 4 else "#247bff"
    b += (f'<g class="e" style="animation-delay:{i*.06}s"><rect x="{x}" y="{y}" width="268" height="84" rx="14" fill="#0a1226" stroke="#1b2f55"/>'
          f'<rect x="{x}" y="{y+22}" width="5" height="40" rx="2" fill="{col}"/><text x="{x+28}" y="{y+52}" font-size="26">{c}</text></g>')
stack = b

# ---------- PROJECTS ----------
P = [("CyberMind AI", "Cybersecurity threat intelligence platform", "Python · Streamlit"),
     ("DocMindX AI", "Disease prediction &amp; health insights", "Scikit-learn · Pandas"),
     ("ISHREE AI", "AI assistant: automation, data, chat", "NLP · Streamlit"),
     ("ML Studio Pro", "AutoML, cleaning &amp; model export", "AutoML · Python"),
     ("Multi-Asset Prediction", "ML system forecasting asset prices", "Machine Learning"),
     ("Gold-Silver Prediction", "ML forecasts for gold &amp; silver", "Time-series · ML")]
b = top("DV / PROJECTS", "THINGS I'VE BUILT", 1200) + '<text x="44" y="150" font-size="54">THINGS I\'VE <tspan style="fill:url(#g)">BUILT</tspan></text>'
for i, (n, d, t) in enumerate(P):
    x, y = 44 + (i % 3) * 382, 190 + (i // 3) * 220
    b += (f'<g class="e" style="animation-delay:{i*.08}s"><rect x="{x}" y="{y}" width="362" height="200" rx="16" fill="#0a1226" stroke="#1b2f55"/>'
          f'<text class="m" x="{x+24}" y="{y+36}" font-size="13" style="fill:#ff6b80">0{i+1}</text><text x="{x+24}" y="{y+82}" font-size="30">{n}</text>'
          f'<text class="m" x="{x+24}" y="{y+118}" font-size="12" style="fill:#9fb0cf">{d}</text><text class="m" x="{x+24}" y="{y+170}" font-size="13" style="fill:#4f9bff">{t}</text></g>')
proj = b

# ---------- CONNECT ----------
L = [("LINKEDIN", "daksh-vasani"), ("INSTAGRAM", "@the_daksh.vasani_"), ("EMAIL", "Gmail"), ("GITHUB", "@VASANI007")]
b = top("DV / CONNECT", "LET'S TALK DATA", 1200) + '<text x="44" y="160" font-size="64">LET\'S BUILD <tspan style="fill:url(#g)">WHAT\'S NEXT</tspan></text>'
for i, (k, v) in enumerate(L):
    x = 44 + i * 288
    b += (f'<g class="e" style="animation-delay:{i*.08}s"><rect x="{x}" y="215" width="268" height="150" rx="16" fill="#0a1226" stroke="#1b2f55"/>'
          f'<text class="m" x="{x+22}" y="258" font-size="13" letter-spacing="2" style="fill:#7f8fae">{k}</text><text x="{x+22}" y="312" font-size="{26 if len(v)<14 else 20}">{v}</text>'
          f'<text x="{x+22}" y="346" font-size="22" style="fill:#ff354f">→</text></g>')
conn = b

for n, w, h, body in [("hero", 1200, 640, hero), ("stack", 1200, 520, stack), ("projects", 1200, 650, proj), ("connect", 1200, 400, conn)]:
    open(os.path.join(H, "assets", n + ".svg"), "w").write(card(n, w, h, body))
print("built", "with photo" if ph else "with placeholder")
