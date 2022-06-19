import requests as r

import pandas as pd

from bs4 import BeautifulSoup

response = r.get("https://en.wikipedia.org/wiki/2021-22_PGA_Tour")
table_id = "Sony Open in Hawaii\n"
wiki_text = response.text

soup = BeautifulSoup(wiki_text, 'html.parser')

event_table = soup.find_all('table')[1:2]

print(event_table)


df = pd.read_html(str(event_table))


df = df[0]

print(df)

df.to_excel('c:/Users/bucke/Desktop/Data_3400/Final Project _TigerWoods/2022Season.xlsx')

