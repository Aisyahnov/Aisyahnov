#!/usr/bin/env python3
"""Render an icon-only animated tech stack for Aisyahnov."""
import os, html
groups=[
 ["Python","Java","JavaScript","TypeScript","Dart","PHP","SQL","HTML","CSS"],
 ["TensorFlow","PyTorch","Scikit-learn","Pandas","NumPy","Matplotlib","Seaborn","Streamlit"],
 ["MySQL","PostgreSQL","SQLite","MongoDB","SQL Server","Oracle","Pentaho"],
 ["Laravel","Flutter","Git","GitHub","VS Code","Jupyter Notebook","Google Colab","Postman","Figma","Android Studio","Burp Suite"],
]
icons={'Python':'Py','Java':'☕','JavaScript':'JS','TypeScript':'TS','Dart':'D','PHP':'PHP','SQL':'SQL','HTML':'<>','CSS':'#','TensorFlow':'TF','PyTorch':'PT','Scikit-learn':'SK','Pandas':'Pd','NumPy':'Np','Matplotlib':'Mt','Seaborn':'Sb','Streamlit':'St','MySQL':'MY','PostgreSQL':'PG','SQLite':'SQ','MongoDB':'MO','SQL Server':'MS','Oracle':'OR','Pentaho':'P','Laravel':'L','Flutter':'F','Git':'Git','GitHub':'GH','VS Code':'VS','Jupyter Notebook':'Jn','Google Colab':'Co','Postman':'Po','Figma':'Fi','Android Studio':'AS','Burp Suite':'Bu'}
colors=['#58a6ff','#bc8cff','#f0883e','#22d3ee']
cell=58; gap=12; cols=11; rows=sum((len(g)+cols-1)//cols for g in groups); w=cols*(cell+gap)+24; h=rows*(cell+gap)+24
p=['<svg xmlns="http://www.w3.org/2000/svg" width="'+str(w)+'" height="'+str(h)+'" viewBox="0 0 '+str(w)+' '+str(h)+'"><style>.i{opacity:0;animation:in .45s cubic-bezier(.22,1,.36,1) both}@keyframes in{from{opacity:0;transform:translateY(10px) scale(.8)}to{opacity:1;transform:none}}@media(prefers-reduced-motion:reduce){.i{opacity:1;animation:none}}</style><rect width="'+str(w)+'" height="'+str(h)+'" rx="12" fill="#0d1117" stroke="#30363d"/>']
n=0
for gi,g in enumerate(groups):
 for j,name in enumerate(g):
  idx=n; x=12+(idx%cols)*(cell+gap); y=12+(idx//cols)*(cell+gap); color=colors[gi]; label=html.escape(icons.get(name,name[:2]))
  p.append(f'<g class="i" style="animation-delay:{idx*.045:.2f}s"><title>{html.escape(name)}</title><rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="12" fill="#161b22" stroke="{color}" stroke-width="2"/><text x="{x+cell/2}" y="{y+36}" text-anchor="middle" fill="{color}" font-family="ui-monospace,monospace" font-size="16" font-weight="700">{label}</text></g>'); n+=1
p.append('</svg>')
open(os.path.join(os.path.dirname(__file__),'..','tech-arsenal.svg'),'w').write(''.join(p))
