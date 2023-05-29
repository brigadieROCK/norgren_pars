import os
import json
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
import csv
from config import url_homepage
from googletrans import Translator
from mytoolsparser import getter, printer


site_homepage = requests.get(url_homepage)
soup_homepage = BeautifulSoup(site_homepage.text, 'html.parser')
mass_homepage = soup_homepage.find_all("a", class_="subtitle")

print(mass_homepage)

for i_home in range(0, len(mass_homepage)):
    mass_homepage[i_home] = str(mass_homepage[i_home])[
                            str(mass_homepage[i_home]).find('href="') + 6:str(mass_homepage[i_home]).find('">')]
    if (mass_homepage[i_home][0:3] == '/sg'):
        mass_homepage[i_home] = 'https://www.norgren.com' + mass_homepage[i_home]
print(mass_homepage)
mass_homepage = mass_homepage[0:3] + mass_homepage[5:]
print(len(mass_homepage))
print(mass_homepage)
for i_cat in range(0, len(mass_homepage)):
    site_page = requests.get(mass_homepage[i_cat])
    soup_page = BeautifulSoup(site_homepage.text, 'html.parser')
    mass_page = soup_page.find_all("a", class_="btn btn-sm more-info")

for i in range(0, len(mass_page)):
    mass_page[i] = str(mass_page[i])[str(mass_page[i]).find('href="') + 6:str(mass_page[i]).find('">')]
    if (mass_page[i][0:3] == '/sg'):
        mass_page[i] = 'https://www.norgren.com' + mass_page[i]

i_page = mass_page[0]
musor = i_page.split("/")[-1].split('-')
name_dir_1 = ''
for j in musor:
    if (j != musor[-1]):
        name_dir_1 += j + '-'
    else:
        name_dir_1 += j

site_podcategory_page = requests.get(i_page)
site_podcategory_page = BeautifulSoup(site_podcategory_page.text, 'html.parser')
mass_podkategory_page = site_podcategory_page.find_all("a", class_="btn btn-sm more-info")
for i_pod_cat in range(0, len(mass_podkategory_page)):
    mass_podkategory_page[i_pod_cat] = str(mass_podkategory_page[i_pod_cat])[str(mass_podkategory_page[i_pod_cat]).find('href="') + 6:str(mass_podkategory_page[i_pod_cat]).find('"',str(mass_podkategory_page[i_pod_cat]).find('href="') + 6)]
    if (mass_podkategory_page[i_pod_cat][0:3] == '/sg'):
        mass_podkategory_page[i_pod_cat] = 'https://www.norgren.com' + mass_podkategory_page[i_pod_cat]

print(mass_podkategory_page)
