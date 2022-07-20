import requests
from bs4 import BeautifulSoup
import re

page = 95
url = f"https://www.b17.ru/media/nikonov/?page={page}&f=2"

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36',
}

responce = requests.get(url, headers=headers)

soup = BeautifulSoup(responce.text, "lxml")

general_dives = soup.find_all("div", class_="video-list")
# print(general_dives)

for div in general_dives[:1]:
    print(div)
    name = div.find('a').text
    print(name)
    audio = div.find('audio')
    print(audio)
    src = audio.get('src')
    print(src)
    
    link = div.find('audio').get('src')
    print(link)
    # link = (re.search('/media_load.+?(?=")', page)).group(0)