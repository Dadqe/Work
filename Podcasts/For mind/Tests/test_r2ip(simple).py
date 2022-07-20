import requests
from bs4 import BeautifulSoup
import random # random.choice
import time

url = 'https://2ip.ru'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

try:
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    
    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    
    print(f'IP: {ip}\nLocation: {location}')
except Exception as ex:
    print(ex)