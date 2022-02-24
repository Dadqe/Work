from bs4 import BeautifulSoup

month = 4
page = 0

# path = r"E:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # PC
path = r"C:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # Laptop

with open(path + f"KinoPoisk2021_month{month}#{page}.html", encoding="utf-8") as file:
    source = file.read()

soup = BeautifulSoup(source, "lxml")

list_of_names = []
list_of_grades = []
list_of_genres = []

# Отсюда список названий всех фильмов
find_all_names_of_films = soup.find_all('span', class_='name')
for element in find_all_names_of_films:
    name = element.find('a').text
    name = name.replace(",", "")
    name = name.replace(" ", "_")
    list_of_names.append(name)

# Отсюда список оценок (рейтинг) всех фильмов
find_all_grade_of_films = soup.find_all(class_='ajax_rating')
for element in find_all_grade_of_films:
    grade = element.find('u').text.split(' ')[0].strip()
    if not '—' in grade:
        list_of_grades.append(grade)
    else:
        list_of_grades.append(0)

# Отсюда список жанров всех фильмов
find_all_genre_of_films = soup.find_all('div', class_='textBlock')
for element in find_all_genre_of_films:
    genre = element.find_all('span')[3].text.lstrip('(').rstrip(')')
    list_of_genres.append(genre)

# # В словарик это собрать
# data = {}

# for i in range(0, len(list_of_names)):
#     data[list_of_names[i]] = f"Оценка: {list_of_grades[i]}, Жанр: {list_of_genres[i]}"

# print(data)

# Или как с играми делал в текстовичок загрузить сразу
films = []
films_6more = []

for i in range(0, len(list_of_names)):
    string = f'{list_of_names[i]}, {list_of_grades[i]}, {list_of_genres[i]}'
    films.append(string)
    if float(string.split(',')[1].strip()) >= float(6):
        films_6more.append(string)
    else:
        continue

print(films)
print(films_6more)

# Создаём файл (текстовый), куда пихаем построчно полученные данные сферху (название и ссылку на обзор)
with open(path + "Films_6more.txt", "a", encoding="utf-8") as file:
    for string in films_6more:
        file.write(string + "\n")


# Осталось понять, как это всё в цикл обернуть, что б я проходился по всем моим сайтам скачанный и делал это
