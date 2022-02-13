# Есть список из 8ми человек, есть 8 чисел, надо сделать так, что б программа присваивала рандомному имени рандомное число, но не повторялось ни то ни другое
# Клим предложил брать рандомное число и удалять его и так же с именем, что б не было повтора
# Можно сразу создать список с цитатами и сразу присваивать их именам, делать, как с числами.

import random

names = ['Алина', 'Женя', 'Лена', 'Виолетта', 'Аня', 'Саша', 'Валя', 'Таня']

random_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

quotes = {}
print(quotes)

start = True
while start:
    for name in names:
        name = random.choice(names)
        names.remove(name)

    for number in random_numbers:
        number = random.choice(random_numbers)
        random_numbers.remove(number)

    if name not in quotes:
        quotes[name] = number
        print(quotes)
        
    else:
        print('Уже есть')
        start = False
    
print(quotes)
# Не получается =\ в итоге всего лишь 4 имени перебирает

print(names)
print(random_numbers)

# en_rus['key'] = 'ключ'