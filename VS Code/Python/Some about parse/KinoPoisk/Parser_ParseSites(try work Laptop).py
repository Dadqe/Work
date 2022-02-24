from bs4 import BeautifulSoup

month = 4
page = 0

# path = r"E:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # PC
path = r"C:\Work\VS Code\Python\Some about parse\KinoPoisk\Data\\" # Laptop

with open(path + f"KinoPoisk2021_month{month}#{page}.html", encoding="utf-8") as file:
    source = file.read()

soup = BeautifulSoup(source, "lxml")

# Найти все теги с фильмами. Получится список, потом пройтись по этому списку по каждому фильму и оттуда вытащить информацию о нужном: Название, Оценка, Жанр
# find_all_films = soup.find_all('div', class_='premier_item')

# Хотел попроовать собрать данные с каждого отдельного фильма, то есть с каждого отдельного элемента в списке после нахождения всех фильмов по тегу и классу, потом просто в цикл фор засунуть, ну и пробежаться по каждому элементу списка и оттуда нужно вытащить, но что-то не получилось, может после доработать
# first_film = find_all_films[0]
# name_of_film = first_film.find('span').text.strip()
# grade_of_film = first_film.find('u').text.split(' ')[0].strip()
# genre_of_film = ''

# for item in find_all_films:
#     name_of_film = item.find('span')юtext.strip()
#     grade_of_film = ''
#     genre_of_film = ''


# Что-то пошло не так, буду брать через find_all собирать сначала все названия фильмов, т.к. по супу проще сделать поиск и собрать всё, потом просто в словарик как-нибудь собирать и добавлять или в список, но надо что б длина этих списков была одинаковой, что б информация была об одном фильме

list_of_names = []
list_of_grades = []
list_of_genres = []

# Отсюда список названий всех фильмов
find_all_names_of_films = soup.find_all('span', class_='name')
for element in find_all_names_of_films:
    name = element.find('a').text
    list_of_names.append(name)

# Отсюда список оценок (рейтинг) всех фильмов
find_all_grade_of_films = soup.find_all(class_='ajax_rating')
for element in find_all_grade_of_films:
    grade = element.find('u').text.split(' ')[0].strip()
    if not '—' in grade:
        list_of_grades.append(grade)
    else:
        list_of_grades.append(None)

# Отсюда список жанров всех фильмов
find_all_genre_of_films = soup.find_all('div', class_='textBlock')
for element in find_all_genre_of_films:
    genre = element.find_all('span')[3].text.lstrip('(').rstrip(')')
    list_of_genres.append(genre)

# len(-1)
# print(len(list_of_names))
# print(len(list_of_grades))
# print(len(list_of_genres))
# print(list_of_names)
# print(list_of_grades)
# print(list_of_genres)
# print(list_of_names[23])

data = {}

for i in range(0, len(list_of_names)):
    data[list_of_names[i]] = f"Оценка: {list_of_grades[i]}, Жанр: {list_of_genres[i]}"

print(data)
