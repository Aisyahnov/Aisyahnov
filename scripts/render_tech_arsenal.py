#!/usr/bin/env python3
"""Render Aisyahnov's animated tech arsenal from her project stack."""
import os
items=[
 ("Languages",["Python","JavaScript","TypeScript","Dart","PHP","SQL"],"#58a6ff"),
 ("Developer",["Full-stack web","Flutter mobile","AI builder"],"#39d353"),
 ("Data & AI",["NLP","SMS spam detection","Forecasting","Computer vision"],"#bc8cff"),
 ("Frameworks & Tools",["Flutter","Laravel","React","Node.js","FastAPI","SQLite","Firebase","Git","Docker","Jupyter"],"#22d3ee"),
]
w=900; row_h=62; h=62+len(items)*row_h+20
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"><style>.pill{opacity:0;animation:in .45s cubic-bezier(.22,1,.36,1) both}.dot{animation:blink 1.2s steps(2,start) infinite}@keyframes in{from{opacity:0;transform:translateY(10px) scale(.96)}to{opacity:1;transform:none}}@keyframes blink{50%{opacity:.35}}@media(prefers-reduced-motion:reduce){.pill{opacity:1;animation:none}.dot{animation:none}}</style><rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12" fill="#0d1117" stroke="#30363d"/><text x="24" y="38" fill="#22d3ee" font-size="21" font-weight="700"><tspan class="dot">▸</tspan> Tech Arsenal</text><line x1="24" y1="52" x2="{w-24}" y2="52" stroke="#30363d"/>']
for ri,(title,badges,color) in enumerate(items):
 y=84+ri*row_h
 p.append(f'<text x="24" y="{y}" fill="#c9d1d9" font-size="15" font-weight="700">{title}</text>')
 x=180
 for i,b in enumerate(badges):
  bw=max(72, len(b)*8+28); delay=(ri*0.18+i*0.07)
  p.append(f'<g class="pill" style="animation-delay:{delay:.2f}s"><rect x="{x}" y="{y-19}" width="{bw}" height="28" rx="6" fill="#161b22" stroke="{color}"/><circle cx="{x+12}" cy="{y-5}" r="4" fill="{color}"/><text x="{x+22}" y="{y}" fill="#e6edf3" font-size="12">{b}</text></g>')
  x+=bw+10
  if x>860: x=180; y+=34
p.append('</svg>')
open(os.path.join(os.path.dirname(__file__),"..","tech-arsenal.svg"),"w").write("".join(p))
