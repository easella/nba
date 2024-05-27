import pandas as pd
df=pd.read_csv("https://projects.fivethirtyeight.com/nba-model/nba_elo.csv")
d2urls={"2023":"https://masseyratings.com/scores.php?s=556881&sub=556881&all=1"}
curr=pd.read_csv("https://ontheroadtovote.com/ncaab/d1vsnond1/teams/nbapre.csv")
curr=curr.replace("Denver Nuggets","DEN")
curr=curr.replace("Milwaukee Bucks","MIL")
curr=curr.replace("Memphis Grizzlies","MEM")
curr=curr.replace("New Orleans Hornets","NOP")
curr=curr.replace("Charlotte Bobcats","CHA")
curr=curr.replace("Indiana Pacers","IND")
curr=curr.replace("Charlotte Hornets","CHA")
curr=curr.replace("Golden State Warriors","GSW")
curr=curr.replace("Atlanta Hawks","ATL")
curr=curr.replace("Seattle SuperSonics","OKC")
curr=curr.replace("New Jersey Nets","BRK")
curr=curr.replace("Kansas City Kings","SAC")
curr=curr.replace("Washington Bullets","WAS")
curr=curr.replace("Boston Celtics","BOS")
curr=curr.replace("New Orleans/Oklahoma City Hornets","NOP")
curr=curr.replace("Washington Wizards","WAS")
curr=curr.replace("Los Angeles Lakers","LAL")
curr=curr.replace("Philadelphia 76ers","PHI")
curr=curr.replace("Sacramento Kings","SAC")
curr=curr.replace("San Antonio Spurs","SAS")
curr=curr.replace("Minnesota Timberwolves","MIN")
curr=curr.replace("Utah Jazz","UTA")
curr=curr.replace("New York Knicks","NYK")
curr=curr.replace("Phoenix Suns","PHO")
curr=curr.replace("Brooklyn Nets","BRK")
curr=curr.replace("Oklahoma City Thunder","OKC")
curr=curr.replace("Portland Trail Blazers","POR")
curr=curr.replace("Detroit Pistons","DET")
curr=curr.replace("Chicago Bulls","CHI")
curr=curr.replace("Vancouver Grizzlies","MEM")
curr=curr.replace("Dallas Mavericks","DAL")
curr=curr.replace("Memphis Grizzlies","MEM")
curr=curr.replace("Orlando Magic","ORL")
curr=curr.replace("Miami Heat","MIA")
curr=curr.replace("Cleveland Cavaliers","CLE")
curr=curr.replace("Toronto Raptors","TOR")
curr=curr.replace("Los Angeles Clippers","LAC")
curr=curr.replace("Houston Rockets","HOU")
curr=curr.replace("New Orleans Pelicans","NOP")
pre=curr
import requests
import re
thearr=[]
didp=0
from bs4 import BeautifulSoup
for key in d2urls:
    r = requests.get(d2urls[key])
    soup = BeautifulSoup(r.text)
    
    p = re.compile(r'([^0-9-]+)\s{3,}')
    p2 = re.compile(r'\s(\d+)\s')
    aa=str(BeautifulSoup(r.text))
    aa=str(aa)
    aa=(aa.split("<hr/><pre>")[1])
    
    aa=aa.replace("               ",",")
    aa=aa.replace("  ",",")
    for i in range(0,10):
        aa=aa.replace(str(i)+" ",str(i)+",")
        
    aa=aa.replace(",,,,,,",",")
    
    q=aa
    
    
    q=q.split("\n")
    for line in q:
        if '<' not in str(line):
            fl=line
        if didp==0:
            print(line)
            didp=1
        p=False
        for num in range(0,10):
            string=str(num)+" P"
            if string in str(line):
                p=True
        
       
        
        
        
        
        line=str(line)
        
        
        
        
        if 'Games' not in str(line) and str(line)!='' and '<' not in str(line):
            j=line[1]
            n=0
            line = list(line.split(','))
            v="vs"
            
            if "@" not in str(line):
                n=1
            if "@" in str(line[1]):
                v="vs"
            else:
                v='@'
            date=str(line[0])
            
            line=str(line)
            line=line.replace("[","")
            line=line.replace("]","")
            line=line.replace("'","")
            line=line.replace('"',"")
            line=line.replace(",@",",")
            line=line.replace("@","")
            line = list(line.split(','))
            lines=[]
            for l in line:
                if l==' ' :
                    m=1
                else:
                    
                    lines.append(l)
                
            
            line=lines
            s=line[1]
            s=s.lstrip()
            s=s.rstrip()
            o=line[3]
            o=o.lstrip()
            o=o.rstrip()
            o=o.replace("amp;","")
            s=s.replace("amp;","")
            if v=='vs':
                v=1
            else:
                v=0

            if s=='LA Lakers' and o=='LA Clippers':
                n=1
                print('yes')
            if s=='LA Clippers' and o=='LA Lakers':
                n=1
                print('no')
            OPP=float(line[4])
            PTS=float(line[2])
            if PTS>OPP:
                mov=PTS-OPP
            else:
                mov=OPP-PTS
            datez=date.replace("-","")
            datez=float(datez)
            p=False
            if datez>20240414:
                p=True
            row=[s,o,line[2],line[4],2023,date,n,v,p,mov]
            
            thearr.append(row)
wl={}

for  i in range(1947,2024):
    wl[i]={}
prez=pd.read_csv("https://ontheroadtovote.com/ncaaf/prefbs/wl.csv")
for row in prez.itertuples():
    odds=str(row.WL)
    wl[float(row.season)][row.Team]=odds
for row in df.itertuples():
    date=str(row.date)
    date=date.replace("-","")
    date=date.replace("-","")
    date=date.strip()
    y=float(row.season)
    y=y-1
    n=row.neutral
    if row.season>1999:
        if row.team1=='LAC' and row.team2=='LAL':
            n=True
        if row.team1=='LAL' and row.team2=='LAC':
            n=True
    OPP=float(row.score2)
    PTS=float(row.score1)
    if PTS>OPP:
        mov=PTS-OPP
    else:
        mov=OPP-PTS
    thearr.append([row.team1,row.team2,row.score1,row.score2,y,date,n,1,row.playoff,mov])
curr=pd.DataFrame(thearr,columns=['team1','team2','score1','score2','season','date','neutral','is_home','playoff','mov'])

curr=curr.replace("Denver","DEN")
curr=curr.replace("Milwaukee","MIL")
curr=curr.replace("Indiana","IND")
curr=curr.replace("Charlotte","CHA")
curr=curr.replace("Memphis Girzzlies","MEM")
curr=curr.replace("Golden State","GSW")
curr=curr.replace("Atlanta","ATL")
curr=curr.replace("Boston","BOS")
curr=curr.replace("Washington","WAS")
curr=curr.replace("LA Lakers","LAL")
curr=curr.replace("Philadelphia","PHI")
curr=curr.replace("Sacramento","SAC")
curr=curr.replace("San Antonio","SAS")
curr=curr.replace("Minnesota","MIN")
curr=curr.replace("Utah","UTA")
curr=curr.replace("New York","NYK")
curr=curr.replace("Phoenix","PHO")
curr=curr.replace("Brooklyn","BRK")
curr=curr.replace("Oklahoma City","OKC")
curr=curr.replace("Portland","POR")
curr=curr.replace("Detroit","DET")
curr=curr.replace("Chicago","CHI")
curr=curr.replace("Dallas","DAL")
curr=curr.replace("Memphis","MEM")
curr=curr.replace("Orlando","ORL")
curr=curr.replace("Miami","MIA")
curr=curr.replace("Cleveland","CLE")
curr=curr.replace("Toronto","TOR")
curr=curr.replace("LA Clippers","LAC")
curr=curr.replace("Houston","HOU")
curr=curr.replace("New Orleans","NOP")
df=curr
from decimal import Decimal
class Elo:
    
    
    

    def __init__(self,k,g=1,homefield = 110): 
        self.ratingDict={}
        self.k = k
        self.g = g
        self.homefield= homefield

    def addPlayer(self,name,rating = 1500):
        self.ratingDict[name] = rating
    def gameOver(self, winner, loser, winnerHome,neutral,wp,lp,wr,lr):
        
        
        homef=hfazz
        if('True' in str(neutral)):
            
        
            homef=0
        
        
        if(winnerHome==True):
            
            elod=(eloLeague.ratingDict[winner]+homef+wr)-(eloLeague.ratingDict[loser]+lr)
        if(winnerHome!=True):
            
            elod=(eloLeague.ratingDict[winner]+wr)-(homef+eloLeague.ratingDict[loser]+lr)
        
        elo=float(elod)
        wp=float(wp)
        lp=float(lp)
        
        o=abs(wp-lp)
        y=float(((o)+3))
        
        mov=((o+3)**0.8)/(7.5+0.006*elod)
        k=25
        if winnerHome==True:
            
            result = self.expectResult(self.ratingDict[winner] + homef+wr, self.ratingDict[loser]+lr)
        else:
            result = self.expectResult(self.ratingDict[winner]+wr, self.ratingDict[loser]+homef+lr)
        shift=(k*mov)*(1 - result) 
        self.ratingDict[winner] +=shift
        self.ratingDict[loser] -=shift
        
        

    def expectResult(self, p1, p2):
        global exp
        exp = (Decimal(p2)-Decimal(p1))/Decimal(400.0)
        n2=Decimal(10.0)
        j=Decimal(exp)
        o=Decimal(1)/((n2**(j))+Decimal(1))
        return float(o)

kval=25
currSeason=1946

eloLeague = Elo(k = kval)
df=df.astype({"team1":"string","team2":"string","is_home":float,"score1":float,"score2":float})
df=df.replace("NJA","BRK")
df=df.replace("NJN","BRK")
df=df.replace("KCK","SAC")
df=df.replace("NOJ","UTA")
df=df.replace("TEX","SAS")
df=df.replace("DLC","SAS")
df=df.replace("SEA","OKC")
df=df.replace("CHO","CHA")
df=df.replace("CHP","WAS")
df=df.replace("CHZ","WAS")
df=df.replace("BAL","WAS")
df=df.replace("CAP","WAS")
df=df.replace("PHW","GSW")
df=df.replace("FTW","DET")
df=df.replace("MNL","LAL")
df=df.replace("ROC","SAC")
df=df.replace("MLH","ATL")
df=df.replace("KCO","SAC")
df=df.replace("CIN","SAC")
df=df.replace("SYR","PHI")
df=df.replace("VAN","MEM")
df=df.replace("SFW","GSW")
teams=set(df.team1.tolist()+df.team2.tolist())
currSeason=1946
df2=pd.read_csv("https://github.com/fivethirtyeight/data/raw/master/nba-elo/nbaallelo.csv")
aba=df2[df2.lg_id=='ABA']
abateams=set(aba.fran_id.tolist())
for team in teams:
    eloLeague.addPlayer(team,rating=1300)
        
df=df.sort_values(by='date')
eloLeague.addPlayer("AND",rating=1562)
eloLeague.addPlayer("BAL",rating=1419)

eloLeague.addPlayer("DEN",rating=1295)
eloLeague.addPlayer("DET",rating=1495)
eloLeague.addPlayer("INJ",rating=1366)
eloLeague.addPlayer("LAL",rating=1527)
eloLeague.addPlayer("SAC",rating=1535)
eloLeague.addPlayer("SHE",rating=1405)
eloLeague.addPlayer("PHI",rating=1458)
eloLeague.addPlayer("ATL",rating=1430)
eloLeague.addPlayer("WAT",rating=1382)
listz=[]
w=0
ll=0
nn=df[df.neutral==0]
ys={}
restz=[]
for row in nn.itertuples():
    ys[row.season]=[]
for row in nn.itertuples():
    if row.is_home==1:
        hp=row.score1
        ap=row.score2
    else:
        hp=row.score2
        ap=row.score1
    diff=hp-ap
    ys[row.season].append(diff)
yz=[]
import numpy as np
didp=0
for key in ys:
    yz.append(np.mean(ys[key]))
hfazz=round(np.mean(yz))*kval
rest={}
didp=0
wins={}

wins={}
winss={}
for  i in range(1947,2024):
    wins[i]={}
    winss[i]=[]
    
for row in pre.itertuples():
    odds=str(row.Odds)
    odds=odds.replace("+","")
    odds=float(odds)
    wins[float(row.Year)][row.Team]=odds
    winss[float(row.Year)].append(odds)

df=df.astype({"date":"string"})
from datetime import date
df=df[df.date<str(date.today())]
df['date']=df['date'].str.replace("-","")
df=df.astype({"date":float})

from datetime import datetime
df=df.sort_values(by='date')
msqe={}

for i in range(9,50):
    msqe[str(i)]=set()
df=df.fillna("False")
df=df.astype({"playoff":"string"})
df=df.replace("SDC","LAC")
df=df.replace("SDR","HOU")
df=df.replace("BUF","LAC")
df=df.replace("NYN","BRK")
df=df.replace("CHH","CHA")
df=df.replace("DNR","DEN")
df=df.replace("TRI","ATL")
df=df.replace("CAR","SSL")
df=df.replace("OAK","VIR")
df=df.replace("LAS","UTS")
df=df.replace("ANA","UTS")
df=df.replace("WSA","VIR")
df=df.replace("MMP","MMS")
df=df.replace("MMT","MMS")
df=df.replace("PTP","PTC")
df=df.replace("MNP","PTC")
df=df.replace("DNA","DEN")
df=df.replace("WSB","WAS")
df=df.replace("HSM","SSL")
df=df.replace("MNM","FLO")
df=df.replace("MMF","FLO")
df=df.replace("NYA","BRK")
df=df.replace("SAA","SAS")
df=df.replace("SDA","SDS")
df=df.replace("NOB","MMS")
df=df.replace("NOK","NOP")
df=df.replace("INA","IND")
for game in df.itertuples():
    o=game.team2
    s=game.team1
    if game.season>currSeason:
        rest={}
        lsdf=df[df.season<game.season]
        ls=set(lsdf.team1.tolist()+lsdf.team2.tolist())
        for key in eloLeague.ratingDict.keys():
            er=eloLeague.ratingDict[key]
            
            if key in ls:
                if game.season<1984 or key not in wins[game.season]:
                    
                    eloLeague.ratingDict[key]=(0.75 * eloLeague.ratingDict[key]) + (0.25 * 1505)
                if key in wins[game.season] and game.season>1983:
                    mean=np.mean(winss[game.season])
                    ew=wins[game.season][key]
                    winsz=((mean-ew)/4000)*20
                    winsz=winsz*0.75
                    eloLeague.ratingDict[key]+=winsz
                    
                    if key in wl[game.season]:
                        wlz=wl[game.season][key]
                        wlz=round(float(wlz))
                        wlz=((41-wlz)/5)*-20
                        wlz=wlz*0.75
                        eloLeague.ratingDict[key]+=wlz
                        
                        
                        
                        
                        
                    eloLeague.ratingDict[key]=(0.75 * eloLeague.ratingDict[key]) + (0.25 * 1505)
                    
        currSeason=game.season
    t1r=0
    t2r=0
    date_format = "%Y%m%d"

    if s in rest and o in rest:
        
        
        d1=str(rest[s])
        d1=d1.replace(".0","")
        d2=str(rest[o])
        d2=d2.replace(".0","")
        date=str(game.date)
        date=date.replace(".0","")
        a = datetime.strptime(d1, date_format)
        b = datetime.strptime(d2, date_format)
        c = datetime.strptime(date, date_format)
        delta = c-b

            
        t2r=delta.days
        delta = c-a

        
        t1r=delta.days
        
        t1r=float(t1r)
        t2r=float(t2r)
        
       
            
            
            
        t1r=(t1r)*20
        
        t2r=(t2r)*20
        restz.append(t1r)
        restz.append(t2r)
        
    if game.score1>game.score2 or game.score1==game.score2:
        if game.is_home==1:
            wh=True
        else:
            wh=False
        n=False
        h=hfazz
        if game.neutral==1:
            n=True
            h=0
        if wh==True:
            hr=eloLeague.ratingDict[game.team1]+h
            ar=eloLeague.ratingDict[game.team2]
        else:
            hr=eloLeague.ratingDict[game.team1]
            ar=eloLeague.ratingDict[game.team2]+h
        if hr>ar:
            w+=1
        if ar>hr:
            ll+=1
        eloLeague.gameOver(game.team1,game.team2,wh,n,game.score1,game.score2,t1r,t2r)
    if game.score2>game.score1:
        if game.is_home==1:
            wh=False
        else:
            wh=True
        h=hfazz
    
        n=False
        if game.neutral==1:
            n=True
            h=0
        if wh==True:
            hr=eloLeague.ratingDict[game.team1]
            ar=eloLeague.ratingDict[game.team2]+h
        else:
            ar=eloLeague.ratingDict[game.team2]
            hr=eloLeague.ratingDict[game.team1]+h
        if hr<ar:
            w+=1
        if ar<hr:
            ll+=1
        eloLeague.gameOver(game.team2,game.team1,wh,n,game.score2,game.score1,t2r,t1r)
    rest[s]=game.date
    rest[o]=game.date

    listz.append(wh)
    for i in range(9,50):
        spread=abs((hr-ar)/float(i))
        spread=round(spread)
        if spread==0:
            spread=1
        ms=(float(game.score1)-float(game.score2))-spread
        
        msz = np.square(ms)
        msqe[str(i)].add(msz)
arr=[]
d2urls={"2023":"https://masseyratings.com/scores.php?s=556881&sub=556881&all=1&mode=3&sch=on&format=0"}
for key in d2urls:
    r = requests.get(d2urls[key])
    soup = BeautifulSoup(r.text)
    
    p = re.compile(r'([^0-9-]+)\s{3,}')
    p2 = re.compile(r'\s(\d+)\s')
    aa=str(BeautifulSoup(r.text))
    aa=str(aa)
    aa=(aa.split("<hr/><pre>")[1])
    
    aa=aa.replace("               ",",")
    aa=aa.replace("  ",",")
    for i in range(0,10):
        aa=aa.replace(str(i)+" ",str(i)+",")
        
    aa=aa.replace(",,,,,,",",")
    
    q=aa
    
    
    q=q.split("\n")
    for line in q:
        
        
        
        
        
        line=str(line)
        
        
        
        
        if 'Games' not in str(line) and str(line)!='' and '<' not in str(line) and 'Sch' in str(line):
            j=line[1]
            n=0
            line = list(line.split(','))
            v="vs"
            if "@" not in str(line):
                n=1
            if "@" in str(line[1]):
                v="vs"
            else:
                v='@'
            date=str(line[0])
            
            line=str(line)
            line=line.replace("[","")
            line=line.replace("]","")
            line=line.replace("'","")
            line=line.replace('"',"")
            line=line.replace(",@",",")
            line=line.replace("@","")
            line = list(line.split(','))
            lines=[]
            for l in line:
                if l==' ' :
                    m=1
                else:
                    
                    lines.append(l)
                
            
            line=lines
            s=line[1]
            s=s.lstrip()
            s=s.rstrip()
            o=line[3]
            o=o.lstrip()
            o=o.rstrip()
            o=o.replace("amp;","")
            s=s.replace("amp;","")
            date=date.replace("-","")
            if v=='vs':
                v=1
            else:
                v=0
                
            row=[s,o,line[2],line[4],2023,date,n,v]
            arr.append(row)

curr=pd.DataFrame(arr,columns=['team1','team2','score1','score2','season','date','neutral','is_home'])

curr=curr.replace("Denver","DEN")
curr=curr.replace("Milwaukee","MIL")
curr=curr.replace("Indiana","IND")
curr=curr.replace("Charlotte","CHA")
curr=curr.replace("Golden State","GSW")
curr=curr.replace("Atlanta","ATL")
curr=curr.replace("Boston","BOS")
curr=curr.replace("Washington","WAS")
curr=curr.replace("LA Lakers","LAL")
curr=curr.replace("Philadelphia","PHI")
curr=curr.replace("Sacramento","SAC")
curr=curr.replace("San Antonio","SAS")
curr=curr.replace("Minnesota","MIN")
curr=curr.replace("Utah","UTA")
curr=curr.replace("New York","NYK")
curr=curr.replace("Phoenix","PHO")
curr=curr.replace("Brooklyn","BRK")
curr=curr.replace("Oklahoma City","OKC")
curr=curr.replace("Portland","POR")
curr=curr.replace("Detroit","DET")
curr=curr.replace("Chicago","CHI")
curr=curr.replace("Dallas","DAL")
curr=curr.replace("Memphis","MEM")
curr=curr.replace("Orlando","ORL")
curr=curr.replace("Miami","MIA")
curr=curr.replace("Cleveland","CLE")
curr=curr.replace("Toronto","TOR")
curr=curr.replace("LA Clippers","LAC")
curr=curr.replace("Houston","HOU")
curr=curr.replace("New Orleans","NOP")
import datetime
tom=str(datetime.date.today() + datetime.timedelta(days=1))
from datetime import date
today=str(date.today())
from datetime import datetime
c=curr
curr=curr.astype({"date":"string"})
curr['date']=curr['date'].str.replace("-","-")
print(today)

today=str(today)
today=today.replace("-","")
today=today.replace(" 00:00:00","")

today=float(today)
curr=curr.astype({"date":float})
curr=curr[curr.date==float("20240527")]
msqez={}
for i in range(9,50):
    msqez[str(i)]=0
for i in range(9,50):
    msqez[str(i)]=sum(msqe[str(i)])/len(msqe[str(i)])
mas=min(msqez, key=msqez.get)
mas=float(mas)
for row in curr.itertuples():
    t2r=0
    t1r=0
    o=row.team2
    s=row.team1
    t1r=0
    t2=row.team2
    t1=row.team1
    t2r=0
    date_format = "%Y%m%d"

    if s in rest and o in rest:
        
        
        d1=str(rest[s])
        d1=d1.replace(".0","")
        d2=str(rest[o])
        d2=d2.replace(".0","")
        date=str(row.date)
        date=date.replace(".0","")
        a = datetime.strptime(d1, date_format)
        b = datetime.strptime(d2, date_format)
        c = datetime.strptime(date, date_format)
        delta = c-b

            
        t2r=delta.days
        delta = c-a

        
        t1r=delta.days
        
        t1r=float(t1r)
        t2r=float(t2r)
            
            
            
        t1r=(t1r)*20
        
        t2r=(t2r)*20
        restz.append(t1r)
        restz.append(t2r)
    hr=eloLeague.ratingDict[t1]+t1r
    ar=eloLeague.ratingDict[t2]+t2r
    
    if row.is_home==1:
        hr=hr+hfazz
    else:
        ar=ar+hfazz
    if hr>ar:
        diff=hr-ar
        s=diff/28
        s=str(s)
        print(t1+" beats "+t2+" by "+s)
    else:
    
        diff=ar-hr
        s=diff/28
        s=str(s)
        print(t2+" beats "+t1+" by "+s)
