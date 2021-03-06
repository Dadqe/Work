import requests
from bs4 import BeautifulSoup
import datetime
import getpass
import os
import time

url = ""

Login = input('Введи логин: ')
Password = getpass.getpass('Введи пароль: ')

auth = {
    'backurl': '/',
    'AUTH_FORM': 'Y',
    'TYPE': 'AUTH',
    'USER_LOGIN': Login,
    'USER_PASSWORD': Password,
    'Login': 'Войти'
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

s = requests.Session()
s.post(url, data=auth, headers=headers, timeout=(5)) #auth Post запрос для того, что б залогиниться. таймаут, хз, это время, в течении которого он будет пробовать выполнить команду, наверное
while True:
    r=s.get(url+'/tech/new.php?sort=UF_DATECREATED&by=DESC', headers=headers)  #page получение страницы после логирования

    # For test on PC
    # with open('Lki_new.html', 'w', encoding='utf-8') as file: 
    #     file.write(r.text)

    # # Try on my PC with Lki_new.html
    # with open('E:\Work\VS Code\Python\Some about parse\EngCab\Lki_new.html', encoding='utf-8') as file: 
    #     src = file.read()

    # soup = BeautifulSoup(src, "lxml") # создание супа из файла на PC
    soup = BeautifulSoup(r.text, "lxml") # Создание супа сразу напрямую с сайта и парсинг
    find_last_bid = soup.find('tr', class_="list-item").find('td', class_="col_datecreate").text.strip() # Datetime в формате d.m.Y. H:M:S

    date_time_object = datetime.datetime.strptime(find_last_bid, '%d.%m.%Y %H:%M:%S')
    now_time = datetime.datetime.now().replace(microsecond=0)
    delta_time = now_time - datetime.timedelta(hours=3, minutes=5)
    check = delta_time < date_time_object < now_time


    print(f'{check} За последние пять минут True = Заявка появилась, False = Заявки не было')

    if check:
        # date_of_creation = date_time_object.strftime("%d.%m.%Y %H:%M:%S") # Через преобразование из datetime в строку, но у нас вроде это уже есть при парсинге в нужном формате
        date_of_creation = find_last_bid
        service = soup.find("div", class_="hiddable2").text
        description = ""
        completion_deadline = ""
        sono = ""
        # data = [date_of_creation, service, description, completion_deadline, sono]
        data = [date_of_creation, service]
        
        with open('data.txt', "w", encoding='utf-8') as file:
            file.writelines([f"{line}\n" for line in data])
        os.startfile(r'data.txt')
    else:
        print("Нет новых заявок")
    
    time.sleep(300)
