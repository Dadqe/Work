from bs4 import BeautifulSoup
import datetime
import os


with open(r'E:/Work/VS Code/Python/Some about parse/EngCab/Tests/bc724bf09f946d62.html', "r", encoding='utf-8') as file:
    source = file.read()

now_time = datetime.datetime.now().replace(microsecond=0)
delta_time = now_time - datetime.timedelta(hours=3, minutes=5)

soup = BeautifulSoup(source, "lxml")

# Сначала надо спарсивать все строки из колонки "Дата создания" (должен получиться список), пройтись по списку времени и сравнивать с условием, и если оно подходит под условие, то надо спарсить всю нужную инфу

data = []

get_list_of_bid = soup.find_all("tr", class_="list-item")
for bid in get_list_of_bid:
    data_of_bid = bid.find("td", class_="col_datecreate").text.strip() # Дата создания заявки в формате str %d.%m.%Y %H:%M:%S
    date_time_bid_object = datetime.datetime.strptime(data_of_bid, '%d.%m.%Y %H:%M:%S') # Привожу к такому формату, с которым можно работать
    check = delta_time < date_time_bid_object < now_time # Делаю проверкой неравенства
    
    # Открыть записанный раннее файл для последующей проверки
    with open('123.txt', 'w') as file:
        previous_data = file.read()
    
    # Если проверка check (время заявки попадает в последние пять минут со старта программы) выполняется (True), то надо продолжить работать
    if check: 
        service = bid.find_all("div", class_="hiddable2")[0].text # Услуга
        
        # Здесь надо сделать проверку следующего рода: Открыть файл new.txt который был до этого сохранён и проверить спарсенную услугу на присутствие в этом файле...
                
        if not "Профилактические работы" in service and not service in previous_data:
            date_of_creation = data_of_bid # Дата создания заявки
            description = bid.find_all("div", class_="hiddable2")[1].text # Описание
            completion_deadline = bid.find("td", class_="col_dateend").text.strip() # Крайний срок завершения
            sono = bid.find("td", class_="col_sono").text.strip() # СОНО
            
            data.extend([f"[+]{date_of_creation} - {completion_deadline}", service, description, sono, "-----"])
        else:
            print("Проф. работы. Надо скипнуть")
            continue
    else:
        print(f"Время последней заявки: {data_of_bid} МСК, свежих заявок нет или уже скачаны") # Сначала сделаю так, что б тут писалось, "Время последней заявки такое-то новых не было (скорее всего)"
        break
        
print(bool(data))
if data:
    with open('data3.txt', "w", encoding='utf-8') as file:
        file.writelines([f"{line}\n" for line in data])
    os.startfile(r'data3.txt')


# data = [date_of_creation, service, description, completion_deadline, sono]
# data = [date_of_creation, service]

# print(get_list_of_bid[:2])
