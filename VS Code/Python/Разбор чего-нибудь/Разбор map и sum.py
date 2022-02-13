# input() --> для ввода
# list(input()) --> разбить введенное на цифры
# map(int, list(input())) --> каждую цифру привести к целому (у нас ведь изначально текст)
# sum(map(int, list(input()))) --> посчитать сумму цифр
# print(sum(map(int, list(input())))) --> вывести сумму

# print(sum(map(int, list(input()))))

# a = map(int, list(input()))
# print(a)

# b = list(a)
# print(b)
# print(type(b))

# c = sum(b)
# print(c)
# print(type(c))

# сумма списка целых чисел
# x = [1, 2, 3, 4]
# print(type(x))
# print(sum(x, 10))


# a = input()
# print(type(a))
# print(a)

# b = list(a)
# print(type(b))
# print(b)

# с = map(int, b)
# print(type(с))
# print(с)

# d = sum(map(int, b))
# print(type(d))
# print(d)

# d = sum(c)   # Почему это не работает??? нельзя назначить переменную с map??
# print(type(d))
# print(d)

# От Клима на сумму через цикл for in

# string1 = input()
# sum = 0
# for i in string1:
#     sum += int(i)
# print(sum)

# Вопрос. Типа я ввожу цифры, они образуют string1, потом ввожу переменную(или что?) sum = 0 после чего запускаю цикл, который проходится по каждому моему элементу(строки)(каждой отдельной цифре)i, которые я ввёл в string1 и прибавляет к сумме?



# old_list = ['1', '2', '3', '4', '5', '6', '7']
 
# new_list = []
# for item in old_list:
#     new_list.append(int(item))
 
# print (new_list)
 
# [1, 2, 3, 4, 5, 6, 7]


# Как видите такой способ занимает меньше строк, более читабелен и выполняется быстрее. map также работает и с функциями созданными пользователем: Применяет функцию "ко всем объектам в объекте"?? ну ко всем итерируемым объектам
def miles_to_kilometers(num_miles):
    """ Converts miles to the kilometers """
    return num_miles * 1.6
 
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
print(type(mile_distances))
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print (kilometer_distances)
 
# [1.6, 10.4, 27.84, 3.84, 14.4]