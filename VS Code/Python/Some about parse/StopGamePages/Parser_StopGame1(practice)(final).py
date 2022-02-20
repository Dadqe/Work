import requests
from bs4 import BeautifulSoup

page = 1
end_page = True
path = r"E:\Work\VS Code\Python\Some about parse\StopGamePages\\"

# while end_page:
#     url = f"https://stopgame.ru/topgames?rating=izumitelno&p={page}"

#     headers = {
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36"
#     }

#     req = requests.get(url, headers=headers)
#     src = req.text

#     with open(path + f"StopGameGames{page}.html", "w", encoding="utf-8") as file:
#         file.write(src)
    
#     soup = BeautifulSoup(src, "lxml")
#     arrow_next_page = soup.find(class_="next")
    
#     if arrow_next_page:
#         print("Arrow is")
#         page += 1
#     else:
#         print("Arrow isn't")
#         end_page = False
names_and_links = []

while end_page:
    try:
        with open(path + f"StopGameGames{page}.html", encoding="utf-8") as file:
            src = file.read()
            
        soup = BeautifulSoup(src, "lxml")
        all_games_hrefs = soup.find_all(class_="caption caption-bold")

        for link in all_games_hrefs:
            a = link.find("a")
            game_link = a.get("href")
            game_name = a.text.strip()
            string = f'Game: {game_name} & link to the overview: {"https://stopgame.ru" + game_link}'
            names_and_links.append(string)
            
        page += 1
    except FileNotFoundError:
        print("Страницы закончились")
        end_page = False

# with open(path + "list_of_games.txt", "w") as file:
#     for link in all_games_hrefs:
#         a = link.find("a")
#         game_link = a.get("href")
#         game_name = a.text.strip()
#         string = f'Game: {game_name} & link to the overview: {"https://stopgame.ru" + game_link}'
#         file.write(string + "\n")

# Создаём файл (текстовый), куда пихаем построчно полученные данные сферху (название и ссылку на обзор)
with open(path + "list_of_games.txt", "w", encoding="utf-8") as file:
    for string in names_and_links:
        file.write(string + "\n")
