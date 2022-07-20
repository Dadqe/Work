import requests
from bs4 import BeautifulSoup
import datetime
import getpass
import os
import time
from plyer import *
import plyer.platforms.win
import plyer.platforms.win.notification

url = "Https://Lki.tax.nalog.ru"

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
    #with open('Lki_new.html', 'w', encoding='utf-8') as file: 
    #     file.write(r.text)

    # # Try on my PC with Lki_new.html
    # with open('E:\Work\VS Code\Python\Some about parse\EngCab\Lki_new.html', encoding='utf-8') as file: 
    #     src = file.read()

    now_time = datetime.datetime.now().replace(microsecond=0)
    delta_time = now_time - datetime.timedelta(hours=3, minutes=5, seconds=3)

    # soup = BeautifulSoup(src, "lxml") # создание супа из файла на PC
    soup = BeautifulSoup(r.text, "lxml") # Создание супа сразу напрямую с сайта и парсинг

    # Сначала надо спарсивать все строки из колонки "Дата создания" (должен получиться список), пройтись по списку времени и сравнивать с условием, и если оно подходит под условие, то надо спарсить всю нужную инфу

    data = []

    get_list_of_bid = soup.find_all("tr", class_="list-item")
    for bid in get_list_of_bid:
        data_of_bid = bid.find("td", class_="col_datecreate").text.strip()
        date_time_bid_object = datetime.datetime.strptime(data_of_bid, '%d.%m.%Y %H:%M:%S')
        check = delta_time < date_time_bid_object < now_time
        
        if check:
            service = bid.find_all("div", class_="hiddable2")[0].text # Услуга
            if not "Профилактические работы" in service: # !!!Тут ведь придумывал двойное условие, мы ещё исключали услуги, которые уже были собраны, не помню зачем.
                date_of_creation = data_of_bid
                service = bid.find_all("div", class_="hiddable2")[0].text
                description = bid.find_all("div", class_="hiddable2")[1].text
                completion_deadline = bid.find("td", class_="col_dateend").text.strip()
                sono = bid.find("td", class_="col_sono").text.strip()
            
                data.extend(["[+]", f"{date_of_creation} - {completion_deadline}", service, description, sono, "-----"])
            else:
                print("Профилактические работы исключены")
                continue
        else:
            print(f"{now_time} OK")
            break
            
    if data:
        with open('new.txt', "w", encoding='utf-8') as file:
            file.writelines([f"{line}\n" for line in data])
        os.startfile(r'new.txt')
        plyer.notification.notify(
            message='НОВЫЕ ЗАЯВКИ',
            app_name='new.txt',
            app_icon='Test.ico',
            title='ALERT!')
    time.sleep(300)

def login_and_take_page(url, Login, Password):
    pass

def gathering(source):
    pass


if __name__ == "__main__":
    pass