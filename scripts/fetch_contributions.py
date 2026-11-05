#!/usr/bin/env python3
"""Fetch Aisyahnov's authenticated GitHub contribution calendar via GraphQL."""
import datetime as dt, json, os, requests
USER=os.environ.get("GITHUB_USERNAME","Aisyahnov")
TOKEN=os.environ.get("PROFILE_TOKEN")
OUT=os.path.join(os.path.dirname(__file__),"..","data","contributions.json")
def main():
 if not TOKEN: raise SystemExit("PROFILE_TOKEN is required")
 end=dt.date.today(); start=end-dt.timedelta(days=365)
 q="""query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){contributionsCollection(from:$from,to:$to){totalContributions restrictedContributionsCount contributionCalendar{weeks{contributionDays{date contributionCount contributionLevel}}}}}}"""
 res=requests.post("https://api.github.com/graphql",json={"query":q,"variables":{"login":USER,"from":start.isoformat()+"T00:00:00Z","to":end.isoformat()+"T23:59:59Z"}},headers={"Authorization":"bearer "+TOKEN,"User-Agent":"Aisyahnov-profile-art"},timeout=30)
 res.raise_for_status(); body=res.json()
 if body.get("errors"): raise SystemExit(str(body["errors"]))
 c=body["data"]["user"]["contributionsCollection"]; days=[d for w in c["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
 days=[{"date":d["date"],"count":d["contributionCount"],"level":0 if d["contributionCount"]==0 else min(5,d["contributionLevel"].count("FOUR")+d["contributionLevel"].count("THREE")+d["contributionLevel"].count("TWO")+1)} for d in days]
 total=c["totalContributions"]; active=sum(d["count"]>0 for d in days); best=max(days,key=lambda x:x["count"])
 cur=longest=run=0
 for d in days:
  run=run+1 if d["count"] else 0; longest=max(longest,run)
 for d in reversed(days):
  if d["count"]: cur+=1
  else: break
 monthly={}
 for d in days: monthly[d["date"][:7]]=monthly.get(d["date"][:7],0)+d["count"]
 out={"username":USER,"generated_at":dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),"range":{"start":str(start),"end":str(end)},"total_contributions":total,"active_days":active,"avg_per_active_day":round(total/active,1) if active else 0,"current_streak":{"length":cur},"longest_streak":{"length":longest},"best_day":{"date":best["date"],"count":best["count"]},"monthly":[{"month":k,"total":v} for k,v in sorted(monthly.items())],"days":days}
 os.makedirs(os.path.dirname(OUT),exist_ok=True); json.dump(out,open(OUT,"w"),indent=2); print(f"wrote {total} authenticated contributions")
if __name__=="__main__": main()
