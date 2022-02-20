import requests
from bs4 import BeautifulSoup

page = 1
# url = f"https://stopgame.ru/topgames?rating=izumitelno&p={page}"

# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36"
# }
# # # Добавил второй, но вроде не всегда обязательный аргумент "Заголовки". Туда добавим Accept и UserAgent, делается это для того, чтобы показать сайту, что мы не бот, а обычный пользователь. Эти данные можно скопировать свои из браузера (Найти их можно во вкладке network в любом из get-запросов) Либо можно использовать библиотеку для генерации случайных юзер агентов, это не принципиально
# req = requests.get(url, headers=headers)
# src = req.text

path = r"E:\Work\VS Code\Python\Some about parse\StopGamePages\\" # здесь в конце второй слеш, для того, что б при использовании был там слеш и можно было к нему просто прибавить название файла и всё было б норм. Вроде называется экранирование

# # # Сохраняем сайт на всякий случай. "Т.к. многие сайты не любят, когда их парсят и велика вероятность получить бан или ограничения по времени, за большое кол-во запросов. А сохранив страницу, всегда сможем продолжить работать с ней"
# # # Вот только есть вопрос. По соседству с исполняемым файлом должна появляться html страничка...Но она появляется в корне всех папок
# with open(path + f"StopGameGames{page}.html", "w", encoding="utf-8") as file:
#     file.write(src)

# # Читаю файл (страницу), которую сохранил, для последующих действий с информацией
# with open(path + "StopGameGames{page}.html", encoding="utf-8") as file:
#     src = file.read()
    
soup = BeautifulSoup(src, "lxml")
all_games_hrefs = soup.find_all(class_="caption caption-bold")

# # Надо придумать функцию которая все дела со ссылками и именами игр проделывала, а потом просто вызывать, например, когда надо составить тот же текстовый файлик и туда всё закинуть....

# def game_and_link_catch():
#     for link in all_games_hrefs:
#         a = link.find("a")
#         game_link = a.get("href")
#         game_name = a.text.strip()
#         string = f'Game: {game_name} & link to the overview: {"https://stopgame.ru" + game_link}'
#         print(string)

# # Если нужно будет записать искомые данные в текстовик. Ну или просто собрать куда-то, я вот в текстовик для начала закину. Я не придумал, как сделать так, что б можно было просто при открытии файла вызвать функцию и всё, она бы сама записала. Только если через декоратор или генератор Yield. Что б не делать перебор в With open as
# with open(path + "list_of_games.txt", "w") as file:
#     for link in all_games_hrefs:
#         a = link.find("a")
#         game_link = a.get("href")
#         game_name = a.text.strip()
#         string = f'Game: {game_name} & link to the overview: {"https://stopgame.ru" + game_link}'
#         file.write(string + "\n")
