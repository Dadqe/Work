# Типы данных

# Пошли прикольчики свои
# a = "Hi, "
# b = "World"
# print (a + b)
# c = a + b
# print (c)
# e = len(c)
# print (e)

# a = 2
# b = 2
# c = 2 * 2
# print (2 + 2)
# print (c)
# print (a + b)

# тест со складыванием чисел после ввода

# chislo1 = input ('Введите первое число: ')
# chislo2 = input ('Введите второе число: ')
# c = int(chislo1) + int(chislo2)
# print (c)
# print (int(chislo1) + int(chislo2))

# Числа
# print (2 + 2)
# print (2 - 2)
# print (2 / 2)
# print (2 * 2)

# pi = 3.14
# r = 5

# print(pi * (r ** 2))

# print (5 % 2) # Остаток от деления
# print (5 // 2) # Деление нацело, остаток отбрасывается

# Строки (Без разницы какие кавычки ставить, можно одинарные, двойные и даже тройные)
# greeting = 'Hello, World'
# hello = 'hello'
# world = 'world'

# print (hello + world)
# print (len(greeting)) # Длина строки !!!не работает, почему-то пишет всегда 12 и всё

# Логический тип
# True / False

# Специальный тип None

# Составные типы данных

# Списки

# int_list = [1, 2, 3, 4]

# different = ['Hello', 1, 1.434, None, True, 1]
# print(int_list)
# print(different)

# print(different + int_list)
# print(len(different))

# different.append('Privet, Mir')
# print(different)

# print(different [0])

# x = 42
# different.append(x)
# print(different)
# different.append(int_list)
# print(different)

# l = len(different)
# print(different[l - 1])
# print(different[-2])
# print(different[-1][2])

# different[0] = 'world'
# print(different)
# print(different [-1]) # Отсюда что-то пошло не так, не захотел печатать (две точки может в конце поставить? после -1) !!!Тут надо просто вытащить из комментов добавление списка в список different,append(int_list)
# print(different [-1][2])

# int_list1 = [1, -1, 30, 4]
# int_list1.sort()
# print(int_list1)
# print(sum(int_list1))

# Словари
# Понятие -> Определение
# Отображение

en_rus = {
    # Ключ -> значение
    # Key -> value
    'hello': 'Привет',  # Запись (item)
    'world': 'мир',
}
print(en_rus)
print(en_rus['hello'])
en_rus['key'] = ''
print(en_rus)
en_rus['key'] = 'allo'
print(en_rus)
# print(en_rus['key'])

# countries = {
#     'Africa': ['Египет', 'Судан', 'Алжир'],
#     'Europe': ['Austria', 'Spain', 'Russia']
# }

# print(countries)
# print(countries['Europe'][0])
# a = countries['Europe']
# print(type(a))
# print(a[0], a[1])
# # print(a[0].replace)
# print(a.replace(a[0], a[1]))
# b = ', '.join(a)
# print(type(b))
# print(b)
# c = list([b])
# print(type(c))
# print(c[0])

# d = 'hello'
# print(type(d))
# print(d)

# wrong_dict = {
#   [1, 2]: 'Wrong Key'
# }

# countries['Asia'] = ['China', 'Thainland', 'Vietnam']
# print (countries)

# countries['Europe'].append('Germany')
# print(countries['Europe'])

# Пользовательский ввод-вывод
# name = input('Введите ваше имя: ')
# print ('Hello, ' + name)

# Задача 1: Форматирование строк
# Можно прочитать про "форматирование строк"

# date = input('Введите дату: ')
# task = ....

# Задача 2: Несколько раз

# Задача 3:

# date = 'Сегодня'
# task = 'Дело 1'

# todos = {
#   'Сегодня' : 'Дело 1'
# }
