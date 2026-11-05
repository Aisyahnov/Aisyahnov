#!/usr/bin/env python3
"""Render Aisyahnov's selected animated tech stack."""
import os
sections=[
 ("Languages",["Python","Java","JavaScript","Dart","PHP","SQL","HTML","CSS"],"#58a6ff"),
 ("Developer Focus",["Open-source Learner","Full-stack Web Developer","Data Engineer","IT Security","Data & AI"],"#39d353"),
 ("Data & AI",["TensorFlow","PyTorch","Scikit-learn","Pandas","NumPy","Matplotlib","Seaborn","Streamlit"],"#bc8cff"),
 ("Databases",["MySQL","PostgreSQL","SQLite","MongoDB","SQL Server","Oracle"],"#f0883e"),
 ("Data Engineering & BI",["Pentaho"],"#22d3ee"),
 ("Frameworks & Tools",["Laravel","Flutter","Git","GitHub","VS Code","Jupyter Notebook","Google Colab","Postman","Figma","Android Studio","Burp Suite"],"#d29922"),
]
w=900; row_h=58; h=62+len(sections)*row_h+24
p=['<svg xmlns="http://www.w3.org/2000/svg" width="'+str(w)+'" height="'+str(h)+'" viewBox="0 0 '+str(w)+' '+str(h)+'" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"><style>.pill{opacity:0;animation:in .45s cubic-bezier(.22,1,.36,1) both}@keyframes in{from{opacity:0;transform:translateY(10px) scale(.96)}to{opacity:1;transform:none}}@media(prefers-reduced-motion:reduce){.pill{opacity:1;animation:none}}</style><rect x=".5" y=".5" width="'+str(w-1)+'" height="'+str(h-1)+'" rx="12" fill="#0d1117" stroke="#30363d"/><text x="24" y="38" fill="#22d3ee" font-size="21" font-weight="700">▸ Tech Arsenal</text><line x1="24" y1="52" x2="'+str(w-24)+'" y2="52" stroke="#30363d"/>']
for ri,(title,badges,color) in enumerate(sections):
 y=84+ri*row_h
 p.append(f'<text x="24" y="{y}" fill="#c9d1d9" font-size="15" font-weight="700">{title}</text>')
 x=180
 for i,b in enumerate(badges):
  bw=max(72,len(b)*7+30)
  if x+bw>875: x=180; y+=32
  p.append(f'<g class="pill" style="animation-delay:{ri*.16+i*.055:.2f}s"><rect x="{x}" y="{y-19}" width="{bw}" height="28" rx="6" fill="#161b22" stroke="{color}"/><circle cx="{x+12}" cy="{y-5}" r="4" fill="{color}"/><text x="{x+22}" y="{y}" fill="#e6edf3" font-size="12">{b}</text></g>')
  x+=bw+9
p.append('</svg>')
open(os.path.join(os.path.dirname(__file__),'..','tech-arsenal.svg'),'w').write(''.join(p))
