import requests
from bs4 import BeautifulSoup
import time


path = r"E:\Work\VS Code\Python\Some about parse\EngCab\\"

with open(path + f"1227d1065b1f745d.html", encoding="utf-8") as file:
    src = file.read()
    
soup = BeautifulSoup(src, "lxml")
find_time = soup.find_all(class_="col_datecreate")

founded_time_HMS = find_time[0].text.strip().split()[1]

time_minuts_last_application = founded_time_HMS.split(":")[1]
print(time_minuts_last_application)

# print(founded_time_HMS)


# Текущее время
t = time.localtime() 
current_time = time.strftime("%H:%M:%S", t) 
minuts_current_time = current_time.split(":")[1]
# delta = int(minuts_current_time)-int(time_minuts_last_application)
delta = int(minuts_current_time)-int(19)
print(type(current_time))
# print(delta<=5)
