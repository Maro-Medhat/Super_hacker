#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = input("Enter URL : ")

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a', href=True):
    print(link['href'])
