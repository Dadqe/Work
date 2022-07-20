import requests
from bs4 import BeautifulSoup
import re
import os
import time
import random
import datetime

# https://www.b17.ru/media/nikonov/?page=95&f=2
# Request URL: https://www.b17.ru/sound/uploaded/sound_2327_fr5kbo.mp3

# page = 94
# url = f"https://www.b17.ru/media/nikonov/?page={page}&f=2"
# url_music = "https://www.b17.ru/media_load.php?id=61210.mp3"

# Для тестов запроса с сохранённой копии на пк
# path_file = r"E:/Work/Podcasts/For mind/Data/HTML/Test95.html"
# with open(path_file, 'r') as file:
#     source = file.read()

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.119 YaBrowser/22.3.0.2430 Yowser/2.5 Safari/537.36',
}

def get_page(url):
    responce = requests.get(url, headers=headers)
    # print(responce) # узнать какой ответ от сайта получаем
    
    # сохранение страницы
    # with open(r'E:/Work/Podcasts/For mind/Data/HTML/'+ f'Test{page}.html', 'w') as file:
    #     file.write(responce.text)
    return responce.text

name_link = {}
def parse_page(page):
    soup = BeautifulSoup(page, "lxml")
    try:
        # Получим общие дивы, что б уже в них пройтись и собрать всё нужное (название и ссылку на скачивание)
        general_dives = soup.find_all("div", class_="video-list")
        
        for div in general_dives[::-1]:
        # for div in general_dives[:1]:
            name = div.find('a').text
            link = div.find('audio').get('src')
            # link = (re.search('/media_load.+?(?=")', page)).group(0) # Через Регулярки от Клима
            name_link[name] = link #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            # with open(r"E:/Work/Podcasts/For mind/Data/Tracks/"+name+".mp3", 'wb') as file:
            #     file.write(requests.get(f"https://www.b17.ru{link}").content)
            
    # Ну спарсил я вот всё, что надо, а дальше что? как мне передать эти данные дальше в другую функцию?
    except Exception as ex:
        print(f"{ex}\n[+] Smth gone wrong")
    finally:
        # print(name_link)
        print("[+] Парсинг закончился")


def save_music(num_page):
    print("Начинаю скачивать файл")
    path = f'E:/Work/Podcasts/For mind/Data/Tracks/300+'
    pre_link = 'https://www.b17.ru'
    count = 1
    for name, link in name_link.items():
        try:
            with open(f'{path}/{name}.mp3', 'wb') as file:
                file.write(requests.get(pre_link + link, headers=headers).content)
        except FileNotFoundError:
            os.makedirs(path)
            with open(f'{path}/{name}.mp3', 'wb') as file:
                file.write(requests.get(pre_link + link, headers=headers).content)
        finally:
            print(f'Запись файла #{count} "{name}" закончена')
            count += 1
    time.sleep(random.uniform(1, 3))
    
    # with open('test_music.mp3', 'wb') as file:
    #     file.write(responce.content)

# Plan: Получить страниц - перевести её в текст, запустить парсинг по этому тексту, пропарсить страничку, там словарик сам заполнится - запустить сохранение музыки - удалить словарик и всё
# Потом нашаманить с циклом для страниц
def main():
    # start = datetime.datetime.now()
    for num_page in range(83, 78, -1):
        url = f"https://www.b17.ru/media/nikonov/?page={num_page}&f=2"
        page = get_page(url=url)
        parse_page(page=page)
        print(num_page)
        print(name_link)
        save_music(num_page=num_page)
        name_link.clear()
        print('Список должен быть очищен')
        print(name_link)
        time.sleep(2)
    
    
    
    
    # page = get_page(url=url)
    # parse_page(page=page)
    # print(name_link)
    # save_music()
    # name_link.clear()
    # print('Список должен быть очищен')
    # print(name_link)
    # finish = datetime.datetime.now() - start
    # print(finish)
    # parse_page(source)
    # save_music(url=url_music)

if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    finish = datetime.datetime.now() - start
    print(finish)
# with open('test2.mp3', 'wb') as file:
#     file.write(responce.content)
