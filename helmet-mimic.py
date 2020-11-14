#! /usr/bin/python3
# by Patrick Brady
# GET random PF2E monster from from Archive of Nethys

from bs4 import BeautifulSoup
import requests
import random
import textwrap

address = "https://2e.aonprd.com/Monsters.aspx?ID="
n = str(random.randint(1, 1003))
url = address+n
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

main = soup.find(id='main')
content = main.find(id='ctl00_MainContent_DetailedOutput')
title = content.find('h1', class_='title').get_text()
bio = content.find('h1', class_='title').next_sibling

get_spans = content.find_all('span')
statblock = [span.get_text() for span in get_spans]

print(title)
print(url)
print('\n' + textwrap.fill(bio) + '\n')

for stat in statblock:
    print(textwrap.fill(stat))
