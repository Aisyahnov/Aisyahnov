#!/usr/bin/env python3
import datetime as dt, json, os
PALETTE=["#161b22","#0e4429","#006d32","#26a641","#39d353","#69f0a0"]
CELL=13; GAP=3; STEP=CELL+GAP; LEFT=34; TOP=22
def main():
 d=json.load(open(os.path.join(os.path.dirname(__file__),"..","data","contributions.json")))
 days=d["days"]; first=dt.date.fromisoformat(days[0]["date"]); start=first-dt.timedelta(days=(first.weekday()+1)%7)
 cells=[]; marks=[]; seen=set()
 for item in days:
  date=dt.date.fromisoformat(item["date"]); week=(date-start).days//7; row=(date.weekday()+1)%7
  level=0 if item["count"]==0 else min(5,1+item["count"]//5)
  cells.append((week,row,level))
  if date.day<=7 and date.strftime("%Y-%m") not in seen: seen.add(date.strftime("%Y-%m")); marks.append((week,date.strftime("%b")))
 weeks=max(x[0] for x in cells)+1; w=LEFT+weeks*STEP+8; h=TOP+7*STEP+10
 p=['<svg xmlns="http://www.w3.org/2000/svg" width="'+str(w)+'" height="'+str(h)+'" viewBox="0 0 '+str(w)+' '+str(h)+'" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"><style>.c{transform-box:fill-box;transform-origin:center;opacity:0;animation:pop .5s ease-out both,flash .7s ease-out both}@keyframes pop{0%{opacity:0;transform:scale(.2)}65%{opacity:1;transform:scale(1.12)}100%{opacity:1;transform:scale(1)}}@keyframes flash{0%,45%{filter:brightness(2.2)}100%{filter:brightness(1)}}@media(prefers-reduced-motion:reduce){.c{opacity:1;animation:none;filter:none}}</style>']
 for week,label in marks: p.append(f'<text x="{LEFT+week*STEP}" y="13" fill="#8b949e" font-size="11">{label}</text>')
 for row,label in [(1,"Mon"),(3,"Wed"),(5,"Fri")]: p.append(f'<text x="0" y="{TOP+row*STEP+10}" fill="#8b949e" font-size="10">{label}</text>')
 for week,row,level in cells:
  delay=(week*.025+row*.04); x=LEFT+week*STEP; y=TOP+row*STEP
  p.append(f'<rect class="c" style="animation-delay:{delay:.3f}s" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{PALETTE[level]}"/>')
 p.append('</svg>'); open(os.path.join(os.path.dirname(__file__),"..","contrib-heatmap.svg"),"w").write(''.join(p))
if __name__=="__main__": main()
