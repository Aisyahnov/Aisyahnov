#!/usr/bin/env python3
"""Render a compact, animated activity overview from the user's real contribution data."""
import json, os
d=json.load(open(os.path.join(os.path.dirname(__file__),"..","data","contributions.json")))
total=d["total_contributions"]; active=d["active_days"]; streak=d["current_streak"]["length"]; best=d["best_day"]["count"]
w,h=880,300
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"><style>.panel{fill:#0d1117;stroke:#30363d}.t{opacity:0;animation:up .55s cubic-bezier(.22,1,.36,1) both}.bar{transform-box:fill-box;transform-origin:left;transform:scaleX(0);animation:grow .7s ease-out both}@keyframes up{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}@keyframes grow{to{transform:scaleX(1)}}@media(prefers-reduced-motion:reduce){.t,.bar{opacity:1;transform:none;animation:none}}</style><rect class="panel" x=".5" y=".5" width="{w-1}" height="{h-1}" rx="12"/><text x="24" y="34" fill="#c9d1d9" font-size="18" font-weight="700">Activity overview</text>']
items=[("Contributions",total,"#39d353"),("Active days",active,"#58a6ff"),("Current streak",streak,"#d29922"),("Best day",best,"#bc8cff")]
for i,(label,val,color) in enumerate(items):
 y=66+i*48; pct=min(100,max(4,round(val/max(total,1)*100)))
 parts.append(f'<g class="t" style="animation-delay:{i*.12:.2f}s"><text x="24" y="{y}" fill="#8b949e" font-size="14">{label}</text><text x="250" y="{y}" fill="#e6edf3" font-size="14">{val}</text><rect x="320" y="{y-12}" width="500" height="12" rx="6" fill="#161b22"/><rect class="bar" style="animation-delay:{i*.12+.18:.2f}s" x="320" y="{y-12}" width="{5*pct}" height="12" rx="6" fill="{color}"/></g>')
parts.append('</svg>')
open(os.path.join(os.path.dirname(__file__),"..","activity-overview.svg"),"w").write("".join(parts))
