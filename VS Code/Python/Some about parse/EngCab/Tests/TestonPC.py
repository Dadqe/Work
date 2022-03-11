from bs4 import BeautifulSoup
import datetime
import os

# "C:\Users\Данил\Downloads\Lki_new — копия.html"
# "C:/Users/Данил/Downloads/Lki_new.html"
with open(r'C:/Users/Данил/Downloads/Lki_new — копия.html', "r", encoding='utf-8') as file:
    source = file.read()

now_time = datetime.datetime.now().replace(microsecond=0)
delta_time = now_time - datetime.timedelta(hours=3, minutes=5)

soup = BeautifulSoup(source, "lxml")

# Сначала надо спарсивать все строки из колонки "Дата создания" (должен получиться список), пройтись по списку времени и сравнивать с условием, и если оно подходит под условие, то надо спарсить всю нужную инфу

data = []

get_list_of_bid = soup.find_all("tr", class_="list-item")
for bid in get_list_of_bid:
    data_of_bid = bid.find("td", class_="col_datecreate").text.strip()
    date_time_bid_object = datetime.datetime.strptime(data_of_bid, '%d.%m.%Y %H:%M:%S')
    check = delta_time < date_time_bid_object < now_time
    
    if check:
        date_of_creation = data_of_bid
        service = bid.find_all("div", class_="hiddable2")[0].text
        description = bid.find_all("div", class_="hiddable2")[1].text
        completion_deadline = bid.find("td", class_="col_dateend").text.strip()
        sono = bid.find("td", class_="col_sono").text.strip()
        
        data.extend([f"[+]{date_of_creation}", service, description, completion_deadline, sono, "-----"])
    else:
        print(f"На момент {now_time} новых заявок не поступало")
        break
        
print(bool(data))
if data:
    with open('data3.txt', "w", encoding='utf-8') as file:
        file.writelines([f"{line}\n" for line in data])
    os.startfile(r'data3.txt')


# data = [date_of_creation, service, description, completion_deadline, sono]
# data = [date_of_creation, service]

# print(get_list_of_bid[:2])
