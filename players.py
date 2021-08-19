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