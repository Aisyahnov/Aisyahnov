#!/usr/bin/env python3
"""Render Aisyahnov's animated personal tech arsenal."""
import os
out=os.path.join(os.path.dirname(__file__),"..","tech-arsenal.svg")
groups=[
 ("Languages",[("Python","#3776ab"),("JavaScript","#b59f00"),("TypeScript","#3178c6"),("SQL","#6b5ca5"),("HTML/CSS","#e34f26")]),
 ("Developer",[("AI Builder","#238636"),("Web Developer","#1f6feb"),("Automation","#8957e5")]),
 ("Data",[("Pandas","#150458"),("NumPy","#4d77cf"),("Jupyter","#f37626"),("scikit-learn","#f89939")]),
 ("Frameworks & Tools",[("Git","#f05032"),("GitHub","#24292f"),("VS Code","#007acc"),("Docker","#2496ed"),("FastAPI","#05998b"),("Streamlit","#ff4b4b")]),
]
w=900; h=500
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"><style>.panel{{fill:#0d1117;stroke:#30363d}}.head{{fill:#c9d1d9}}.section{{opacity:0;animation:up .5s cubic-bezier(.22,1,.36,1) both}}.chip{{transform-box:fill-box;transform-origin:center;opacity:0;animation:pop .45s ease-out both}}@keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}@keyframes pop{{0%{{opacity:0;transform:scale(.75)}}70%{{opacity:1;transform:scale(1.06)}}to{{opacity:1;transform:scale(1)}}}}@media(prefers-reduced-motion:reduce){{.section,.chip{{opacity:1;transform:none;animation:none}}}}</style><rect class="panel" x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12"/><text x="24" y="38" class="head" font-size="22" font-weight="700">&lt;/&gt; Tech Arsenal</text><line x1="24" y1="55" x2="876" y2="55" stroke="#30363d"/>']
y=92
for gi,(title,items) in enumerate(groups):
 p.append(f'<g class="section" style="animation-delay:{gi*.14:.2f}s"><text x="450" y="{y}" text-anchor="middle" fill="#e6edf3" font-size="16" font-weight="700">{title}</text></g>')
 y+=22
 x=450-(len(items)*120)/2
 for i,(name,color) in enumerate(items):
  xx=x+i*120
  p.append(f'<g class="chip" style="animation-delay:{gi*.14+i*.07+.12:.2f}s"><rect x="{xx:.0f}" y="{y}" width="108" height="30" rx="6" fill="{color}"/><text x="{xx+54:.0f}" y="{y+20}" text-anchor="middle" fill="#fff" font-size="12">{name}</text></g>')
 y+=60
p.append("</svg>")
open(out,"w").write("".join(p))
