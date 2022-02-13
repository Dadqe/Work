# str = "это пример строки....wow!!! это действительно строка"
# print (str.replace("wow", "поразительно"))
# print (str.replace("это", "здесь", 1))



def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
# создаем словарь со значениями и строку, которую будет изменять
replace_values = {"кот": "кошка1", "кошка": "собака"}
my_str = "У меня есть кот и кошка"

# изменяем и печатаем строку
my_str = multiple_replace(my_str, replace_values)
print(my_str)