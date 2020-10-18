#! /bin/bash
# by Patrick Brady
# GET random PF2E monster from from Archive of Nethys

from bs4 import BeautifulSoup
import requests
import random

address = "https://2e.aonprd.com/Monsters.aspx?ID="
n = str(random.randint(1, 1003))
url = address+n
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

main = soup.find(id='main')
id = main.find(id='ctl00_MainContent_DetailedOutput')
title = id.find('h1', class_='title').get_text()
get_spans = id.find_all('span')
statblock = [span.get_text() for span in get_spans]
print(url)
print(title)
for stat in statblock:
    print(stat)
