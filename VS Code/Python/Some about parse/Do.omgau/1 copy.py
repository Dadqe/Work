import requests
from bs4 import BeautifulSoup
import sys

sys.path.insert(0, 'E:/Tokens/Logins/') # PC
# sys.path.insert(0, 'C:/Tokens/Logins/') # Laptop
from OmGAU import Login, Password


# a = "https://do.omgau.ru/my/"
url = "https://do.omgau.ru/login/index.php"

response = requests.get(url)
source = response.text

soup = BeautifulSoup(source, "lxml")

Logintoken = soup.find("form", class_="mt-3").find_all("input")[1].get("value")
# print(Logintoken)


# path = r"C:\Work\VS Code\Python\Some about parse\Do.omgau\\" # Laptop
path = r"E:\Work\VS Code\Python\Some about parse\Do.omgau\\" # PC

data = {
    "anchor": '',
    "logintoken": Logintoken,
    "username": "da.demin1d1706014",
    "password": "Testirovanie21@"
}


session = requests.Session()
responce = session.post(url, data=data)

if "Неверный логин или пароль, попробуйте заново." in responce.text:
    print("Ne poshlo")
else:
    print("Not login")


# with open(path + "LogedSite.html", "w", encoding="utf-8") as file:
#     file.write(r.text)
