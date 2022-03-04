import requests
from bs4 import BeautifulSoup
import sys
sys.path.insert(1, 'E:/Tokens/Logins/')
from OmGAU import Login, Password

path = "E:\Work\VS Code\Python\Some about parse\Do.omgau\data\\"

url = "https://do.omgau.ru"

s = requests.Session()
source = s.get(url+'/login/index.php').text
soup = BeautifulSoup(source, "lxml")
Logintoken = soup.find("form", class_="mt-3").find_all("input")[1].get("value") # Logintoken генерируется автоматом при каждом посещении первой страницы, парсим его, что б закинуть в data для авторизации на сайте

auth = {
    'anchor': '',
    'logintoken': Logintoken,
    'username': Login,
    'password': Password
}

s.post(url+'/login/index.php', data=auth, timeout=(5)) #auth
r=s.get(url+'/my')  #page

# soup = BeautifulSoup(r.text, "lxml")
# raspisanie = soup.find(text="Расписание занятий").parent.get("href")
# print(raspisanie)

with open(path + "LogedSite.html", "w", encoding="utf-8") as file:
    file.write(r.text)


# if 'ОБЩАЯ' in r.text:
#     print("Succses")
# else:
#     print('Not login')