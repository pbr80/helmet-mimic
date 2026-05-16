#! /usr/bin/python3

from bs4 import BeautifulSoup
import requests
import random
import sys
import textwrap


def main():
    address = "https://2e.aonprd.com/Monsters.aspx?ID="

    while True:
        n = str(random.randint(1, 4775))
        url = address + n
        try:
            page = requests.get(url, timeout=5)
        except Exception:
            continue
        if page.status_code != 200:
            continue

        soup = BeautifulSoup(page.content, 'html.parser')
        main_div = soup.find(id='main')
        if main_div is None:
            continue
        mp = main_div.find('span', class_='monster-page')
        if mp is None:
            continue
        hop = mp.find('span', class_='hide-on-print')
        if hop is None:
            continue
        title_el = hop.find('h1', class_='title')
        if title_el is None:
            continue

        title = title_el.get_text()
        bio = title_el.next_sibling

        get_spans = mp.find_all('span', recursive=True)
        statblock = [span.get_text() for span in get_spans]
        break

    print('\n= = = = = =\n' + title)
    print(url)
    print('\n' + textwrap.fill(str(bio), width=90) + '\n')

    for stat in statblock:
        print(textwrap.fill(stat))
    print('= = = = = =')


if __name__ == '__main__':
    main()
