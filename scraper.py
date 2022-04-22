import requests
import json
import MySQLdb
from bs4 import BeautifulSoup

HOST = "localhost"
USERNAME = "scr_u"
PASSWORD = ""
DATABASE = "octanegg"

url = 'https://octane.gg/stats/players?mode=3&minGames=50&group=rlcs2122fall'
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")



