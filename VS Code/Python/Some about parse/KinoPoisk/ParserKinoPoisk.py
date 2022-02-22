import requests
from bs4 import BeautifulSoup
# импортировать рандом, оттуда randint(2, 6) или ещё там как-то, можно посмотреть в видосе предпоследнем

page = 4

url = f"https://www.kinopoisk.ru/premiere/ru/2021/month/{page}/"

path = r"E:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\"

# def get_html(url):
#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36",
#     }
#     response = requests.get(url, headers=headers)
#     return response.text

# with open(path + f"KinoPoisk{page}.html", "w", encoding="utf-8") as file:
#     file.write(get_html(url))

with open(path + f"KinoPoisk{page}.html", encoding="utf-8") as file:
    source = file.read()

def get_list_of_films():
    pass

soup = BeautifulSoup(source, "lxml")
list_of_films = soup.find_all("div", class_="premier_item")
print(list_of_films[-1])

# Сайт оказался динамическим. Он подгружает фильмы по мере пролистывания страницы, сейчас на стадии поиска того, как эту задачу пройти...