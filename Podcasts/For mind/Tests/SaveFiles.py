import os

page = 95
str = "краказябра"
path = f"E:/Work/Podcasts/For mind/Data/Tracks/{page}"

try:
    with open(f'{path}/smth.txt', 'w', encoding='utf-8') as file:
        file.write(str)
except FileNotFoundError:
    os.makedirs(path)
    with open(f'{path}/smth.txt', 'w', encoding='utf-8') as file:
        file.write(str)