import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 10
P = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# здесь продолжайте программу
def is_isolate(l, i_l, lst_in, random_index): # 1-й аргумент это лист, который выбран при итерации, 2-й это индекс этого листа, 3-й это весь массив, который хранит все эти листы
    flag = True
    print(f"Номер внутреннего списка {i_l} Номер рандомного индекса {random_index}")
    if random_index == 0 and i_l != len(lst_in) - 1 and i_l != 0: # Если число первое в исследуемом списке (и список этот не последний во всём массиве и не первый)
        if l[random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index+1] == 1 or lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1: # Проверить справа, снизу, снизусправа, сверху, сверхусправа
            flag = False
    
    
    elif random_index == 0 and i_l == 0: # Если число первое в исследумом списке (и список первый)
        if l[random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index+1] == 1: # Проверить справа, снизу, снизусправа
            flag = False


    elif random_index == len(l) - 1 and i_l != len(lst_in) - 1 and i_l != 0: # Если число последнее в исследумом списке (и список не последний во всём массиве и не первый)
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l+1][random_index] == 1: # Проверить сверху, сверхуслева, слева, снизуслева, снизу
            flag = False
    
    
    elif random_index == len(l) - 1 and i_l == len(lst_in) - 1: # Если число последнее в исследумом списке (и список последний)
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1: # Проверить сверху, сверхуслева, слева
            flag = False

                    
    elif i_l != len(lst_in) - 1: # Во всех остальных случаях, проверять вокруг *начинаю сверху и по часовой стрелке
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1 or lst_in[i_l][random_index+1] == 1 or lst_in[i_l+1][random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1 or lst_in[i_l+1][random_index-1] == 1:
            flag = False

    print(f"final: {l}")
    return flag

while N != 0:
    for i_l, l in enumerate(P):
        random_index = random.randint(0, len(l)-1)
        print(f"[first] index_l = {i_l}, Должен быть список {l}, Рандомный индекс")
        if l[random_index] != 1 and is_isolate(l, i_l, P, random_index):
            l[random_index] = 1
            N -= 1
for l in P:
    print(*l)