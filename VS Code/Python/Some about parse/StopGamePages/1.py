import requests
from bs4 import BeautifulSoup

page = 1
end_page = True
path = r"C:\Work\VS Code\Python\Some about parse\StopGamePages\\"

names_and_links = []

with open(path + f"StopGameGames{page}.html", encoding="utf-8") as file:
    src = file.read()
            
soup = BeautifulSoup(src, "lxml")
all_games_hrefs = soup.find_all(class_="caption caption-bold")

# for link in all_games_hrefs:
#     a = link.find("a")
#     game_link = a.get("href")
#     game_name = a.text.strip()
#     string = f'Game: {game_name} & link to the overview: {"https://stopgame.ru" + game_link}'
#     names_and_links.append(string)
    
print(all_games_hrefs)

