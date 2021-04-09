#! /usr/bin/python3
# by Patrick Brady
# Updated: 04-09-21 (Creature count: 1051)
# Pulls random creature from [(Archives of Nethys)](https://2e.aonprd.com)
# Works in conjunction with '20-helmet-mimic.sh' to append MOTD.

from bs4 import BeautifulSoup
import requests
import random
import textwrap

address = "https://2e.aonprd.com/Monsters.aspx?ID="
n = str(random.randint(1, 1051))
url = address+n
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

main = soup.find(id='main')
content = main.find(id='ctl00_MainContent_DetailedOutput')
title = content.find('h1', class_='title').get_text()
bio = content.find('h1', class_='title').next_sibling

get_spans = content.find_all('span')
statblock = [span.get_text() for span in get_spans]

print('\n=== MONSTER OF THE DAY ===\n' + title)
print(url)
print('\n' + textwrap.fill(bio, width=90) + '\n')

for stat in statblock:
    print(textwrap.fill(stat))
print('=== MONSTER OF THE DAY ===')
