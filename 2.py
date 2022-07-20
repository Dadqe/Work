import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = 10
P = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# здесь продолжайте программу
def is_isolate(l, i_l, lst_in, random_index): # 1-й аргумент это лист, который выбран при итерации, 2-й это индекс этого листа, 3-й это весь массив, который хранит все эти листы
    flag = True
    
    if random_index == 0 and i_l == 0: # Если число первое в исследуемом списке (и список этот первый)
        if l[random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index+1] == 1: # Проверить справа, снизу, снизусправа, сверху, сверхусправа
            flag = False
    
    elif random_index == 0 and i_l == len(lst_in) - 1: # Если число первое и список последний
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1 or lst_in[i_l][random_index+1] == 1: # Проверить сверху, сверхусправа, справа
            flag = False
    
    elif random_index == 0 and i_l != 0 and i_l != len(lst_in) - 1: # Если число первое и список не первый и не последний
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1 or lst_in[i_l][random_index+1] == 1  or lst_in[i_l+1][random_index+1] == 1  or lst_in[i_l+1][random_index] == 1: # Проверить сверху, сверхусправа, справа, снизусправа, снизу
            flag = False
    
    elif random_index == len(l) - 1 and i_l == 0: # Если число последнее и список первый
        if lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1: # Проверить снизу, снизуслева, слева
            flag = False
    
    elif random_index == len(l) - 1 and i_l == len(lst_in) - 1: # Если число последнее и список последний
        if lst_in[i_l][random_index-1] == 1 or lst_in[i_l-1][random_index-1] == 1 or lst_in[i_l-1][random_index] == 1: # Проверить слева, сверхуслева, сверху
            flag = False
    
    elif random_index == len(l) - 1 and i_l != 0 and i_l != len(lst_in) - 1: # Если число последнее и список не первый и не последний
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1 or lst_in[i_l-1][random_index-1] == 1: # Проверить сверху, снизу, снизуслева, слева, сверхуслева
            flag = False
    
    elif i_l == 0: # Если список первый...
        if lst_in[i_l][random_index+1] or lst_in[i_l+1][random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1: # Проверить справа, снизусправа, снизу, снизуслева, слева
            flag = False
    
    elif i_l == len(l) - 1: # Если список последний...
        if lst_in[i_l][random_index-1] == 1 or lst_in[i_l-1][random_index-1] == 1 or lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1 or lst_in[i_l][random_index+1]: # Проверить слева, слевасверху, сверху, сверхусправа, справа
            flag = False
    
    else: # Во всех остальных случая проверять по кругу, начиная сверху
        if lst_in[i_l-1][random_index] == 1 or lst_in[i_l-1][random_index+1] == 1 or lst_in[i_l][random_index+1] or lst_in[i_l+1][random_index+1] == 1 or lst_in[i_l+1][random_index] == 1 or lst_in[i_l+1][random_index-1] == 1 or lst_in[i_l][random_index-1] == 1 or lst_in[i_l-1][random_index-1] == 1:
            flag = False
    
    return flag

while N > 0:
    for i_l, l in enumerate(P):
        random_index = random.randint(0, len(l)-1)
        print(f"[first] index_l = {i_l}, Должен быть список {l}, Рандомный индекс {random_index}")
        if l[random_index] != 1 and is_isolate(l, i_l, P, random_index):
            l[random_index] = 1
            N -= 1
        if N == 0:
            break
for l in P:
    print(*l)