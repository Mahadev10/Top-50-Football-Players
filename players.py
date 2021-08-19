import requests as req
from bs4 import BeautifulSoup
import lxml,pandas as pd

base_url="https://www.footballcritic.com/top-players" # website url
page=req.get(base_url) 
# players_date is to store data from website
players_data={
    'Rank':[],
    'Name':[],
    'Team':[],
    'Nation':[],
    'Age':[]
}
if page.status_code==req.codes.ok:
    bs=BeautifulSoup(page.text,'lxml')
    l=bs.find('table',id="playerTopList").find('tbody').find_all('tr')
    for p in l:
       rank=p.find('span',class_='number')
       name=p.find('td',class_='name')
       team=p.find('span',class_='club-name')
       nation=p.find('td',class_='age')
       if rank and name and team and nation:
           rank=rank.text
           name=name.find('a').text
           team=team.find('a').text
           nation=nation.find_all('a')[-1].text
           players_data['Rank'].append(rank)
           players_data['Name'].append(name)
           players_data['Team'].append(team)
           players_data['Nation'].append(nation)   
    print(players_data)       