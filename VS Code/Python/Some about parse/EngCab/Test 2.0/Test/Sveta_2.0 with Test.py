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

# cd '.\VS Code\Python\Some about parse\EngCab\Test 2.0\'
# Test\Scripts\activate
# cd .\Test\

def test():
    with open(r'E:/Work/VS Code/Python/Some about parse/EngCab/Test 2.0/Lki_new (2022-04-14 17-10-19).html', 'r', encoding='utf-8') as file:
        r = file.read()
    
    date_time_str = '2022-04-14 17:10:19'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    delta_time = date_time_obj - datetime.timedelta(hours=3, minutes=5, seconds=0)
    
    with open('E:/Work/VS Code/Python/Some about parse/EngCab/Test 2.0/new1.txt', 'r', encoding='utf-8') as file:
        previous_data = file.read()
    
    soup = BeautifulSoup(r, "lxml")
    
    data = []
    
    get_list_of_bid = soup.find_all("tr", class_="list-item")
    for bid in get_list_of_bid:
        data_of_bid = bid.find("td", class_="col_datecreate").text.strip()
        date_time_bid_object = datetime.datetime.strptime(data_of_bid, '%d.%m.%Y %H:%M:%S')
        check = delta_time < date_time_bid_object < date_time_obj
                
        service = bid.find_all("div", class_="hiddable2")[0].text # Услуга
        if check and not "Профилактические работы" in service and not service in previous_data:
            date_of_creation = data_of_bid
            service = bid.find_all("div", class_="hiddable2")[0].text
            description = bid.find_all("div", class_="hiddable2")[1].text
            completion_deadline = bid.find("td", class_="col_dateend").text.strip()
            sono = bid.find("td", class_="col_sono").text.strip()
        
            data.extend(["[+]", f"{date_of_creation} - {completion_deadline}", service, description, sono, "-----"])
    
    if data:
        print("Если в data что-то добавилось, то дальше должен открыться файл и вылезти оповещение")
        with open('E:/Work/VS Code/Python/Some about parse/EngCab/Test 2.0/new.txt', "w", encoding='utf-8') as file:
            file.writelines([f"{line}\n" for line in data])
        os.startfile(r'E:/Work/VS Code/Python/Some about parse/EngCab/Test 2.0/new.txt')
        plyer.notification.notify(
            message='НОВЫЕ ЗАЯВКИ',
            app_name='new.txt',
            # app_icon='Test.ico',
            title='ALERT!')

def gathering_new_bid(source):
    print("Посылаю get запрос")
    r = source.get(url+'/tech/new.php?sort=UF_DATECREATED&by=DESC', headers=headers)
    
    now_time = datetime.datetime.now().replace(microsecond=0)
    delta_time = now_time - datetime.timedelta(hours=3, minutes=5, seconds=0)
    with open('new.txt', 'r', encoding='utf-8') as file:
        previous_data = file.read()
    
    # For test on PC
    with open(f'Lki_new{now_time}.html', 'w', encoding='utf-8') as file: 
        file.write(r.text)
    
    print(f'Сейчас время {now_time}\n Создаю суп')
    soup = BeautifulSoup(r.text, "lxml")
    
    data = []
    
    get_list_of_bid = soup.find_all("tr", class_="list-item")
    for bid in get_list_of_bid:
        data_of_bid = bid.find("td", class_="col_datecreate").text.strip()
        date_time_bid_object = datetime.datetime.strptime(data_of_bid, '%d.%m.%Y %H:%M:%S')
        check = delta_time < date_time_bid_object < now_time
                
        service = bid.find_all("div", class_="hiddable2")[0].text # Услуга
        if check and not "Профилактические работы" in service and not service in previous_data:
            date_of_creation = data_of_bid
            service = bid.find_all("div", class_="hiddable2")[0].text
            description = bid.find_all("div", class_="hiddable2")[1].text
            completion_deadline = bid.find("td", class_="col_dateend").text.strip()
            sono = bid.find("td", class_="col_sono").text.strip()
        
            data.extend(["[+]", f"{date_of_creation} - {completion_deadline}", service, description, sono, "-----"])
    print("Должен был просканить всё страницу и если подошло по времени, собрать в data")
            
    if data:
        print("Если в data что-то добавилось, то дальше должен открыться файл и вылезти оповещение")
        with open('new.txt', "w", encoding='utf-8') as file:
            file.writelines([f"{line}\n" for line in data])
        os.startfile(r'new.txt')
        plyer.notification.notify(
            message='НОВЫЕ ЗАЯВКИ',
            app_name='new.txt',
            app_icon='Test.ico',
            title='ALERT!')
    
    

def main():
    while True:
        print("Запускаю gathering")
        start_time = time.time()
        gathering_new_bid(source=s)
        print(f"{time.time() - start_time} Столько секунд от запуска и до завершения сбора данных")
        print("gathering должен завершиться засыпаю на 2.5 мин")
        time.sleep(150)

if __name__ == "__main__":
    # Login = input('Введи логин: ')
    # Password = getpass.getpass('Введи пароль: ')
    # s = requests.Session()
        
    # auth = {
    # 'backurl': '/',
    # 'AUTH_FORM': 'Y',
    # 'TYPE': 'AUTH',
    # 'USER_LOGIN': Login,
    # 'USER_PASSWORD': Password,
    # 'Login': 'Войти'
    # }
    # headers = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    # }
    
    # s.post(url, data=auth, headers=headers, timeout=(5))
    # # Надо сделать проверку на статус после посылки s.post какой ответ по s.get в main я получаю, и если r с нужным ответом возвращается, то делаю дальше (создаю суп и т.п.), если нет, то что-то с логином и паролем... надо будет полностью перезапускать программу
    # print("Должно было произойти логирование")
    
    # while True:
    #     try:
    #         print("Запускаю основную функцию")
    #         main()
    #         print("Закончил основную функцию")
    #     except Exception as e:
    #         print("Something gone wrong...")
    #         print(e)
    #         print("The program will start in 1 minute")
    #         time.sleep(60)
    
    
    test()