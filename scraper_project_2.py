from locale import D_FMT
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"
page=requests.get(START_URL)

temp_list=[]
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find_all('table')
table_rows=star_table[7].find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

name=[]
distance=[]
mass=[]
radius=[]
for i in range(7,len(temp_list)):
    name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])

df=pd.DataFrame(list(zip(name,distance,mass,radius)),columns=['name','distance','mass','radius'])
df.to_csv('project2_output_c127.csv')

