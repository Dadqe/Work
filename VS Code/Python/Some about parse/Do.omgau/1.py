import requests
from bs4 import BeautifulSoup
import sys

# sys.path.insert(0, 'E:/Tokens/KinoPoisk/') # PC
sys.path.insert(0, 'C:/Tokens/Logins/') # Laptop
from OmGAU import Login, Password

url = "https://do.omgau.ru/login/index.php"

path = r"C:\Work\VS Code\Python\Some about parse\Do.omgau\\" # Laptop

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.4.840 Yowser/2.5 Safari/537.36",
}

data = {
    "username": Login,
    "password": Password,
}

source = requests.Session()
responce = source.post(url, headers=headers, data=data)

with open(path + "LogedSite.html", "w", encoding="utf-8") as file:
    file.write(responce.text)
