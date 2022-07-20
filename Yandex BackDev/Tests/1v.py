# Саша разрабатывает игру «Отгадай слово». В этой игре, игрок должен отгадать загаданное слово из N букв за несколько попыток

# S1 = input() # Загаданное слово или строка
# Q1 = input() # Попытка игрока. Слово, которое предложил игрок
# Обе строки имеют одинаковую длину N

# S1 = "COVER"
# Q1 = "CLEAR"

# S1 = "ABBA"
# Q1 = "AAAA"

# S1 = "ABCBC"
# Q1 = "BBACA"

Q1_dict = {}
ch_dict = {}

for i in range(0, len(S1)):
    Q1_dict[i] = Q1[i]

for i in range(0, len(S1)):
    ch_dict[Q1[i]] = S1.count(Q1[i])

for i in range(0, len(S1)):
    if Q1[i] == S1[i]:
        # print(f"{i}correct")
        ch_dict[S1[i]] -= 1
        Q1_dict[i] = "correct"
        
# заполнил корректом, а потом уже сначала презентом, если не им, то абсентом

for i in range(0, len(S1)):
    if Q1[i] in S1 and ch_dict[Q1[i]] != 0 and len(Q1_dict[i]) == 1:
        # print(f'{i}present')
        Q1_dict[i] = "present"
        ch_dict[Q1[i]] -= 1
    elif Q1[i] != S1[i] and len(Q1_dict[i]) == 1:
        # print(f'{i}absent')
        Q1_dict[i] = "absent"

# for i in range(0, len(S1)):
#     if Q1[i] != S1[i] and len(Q1_dict[i]) == 1:
#         # print(f'{i}absent')
#         Q1_dict[i] = "absent"

# for i in range(0, len(S1)):
#     if Q1_dict[i] == 'absent' and Q1[i] in S1 and ch_dict[Q1[i]] != 0:
#         # print(f'{i}present')
#         Q1_dict[i] = "present"
#         ch_dict[Q1[i]] -= 1

for i in range(0, len(S1)):
    print(Q1_dict[i])

# сначала пробежаться по корректу, заполнить словарь по индексам букв, только там, где коррект -> удалить из памяти количество вхождений букв
# пробежаться по абсентам, заполнить все поля 
# пробежаться по ТОЛЬКО абсентам и проверить по порядку на пресент -> удалить из памяти количество вхождений букв






# for i in range(0, len(S1)):
#     if Q1[i] == S1[i]:
#         print("correct... Буква совпадает")
#         ch_dict[S1[i]] -= 1
#     elif Q1[i] in S1 and ch_dict[S1[i]] != 0: # если буква просто не равна, но она есть в слове
#         print("present... Вообще, такая буква есть в загаданном слове")
#         ch_dict[S1[i]] -= 1
#         # print(f"Количество таких букв в слове осталось {count_of_present}")
#     elif Q1[i] != S1[i]:
#         print("absent... Буква не совпадает")









# по примерам можно сказать, что слова перебираются побуквенно и сравниваются буквы, если они сходятся, то вывод: correct 
# надо будет сравнивать по индексам букв....

# одинаковые буквы в загаданном слове заканчиваются, надо флаг перевернуть в false и не дать заходить во второе условие


# for ch in S1:
#     bukva_S1 = ch
#     print(ch)
#     for ch in Q1:
#         bukva_Q1 = ch
#         print(ch)
#         if bukva_S1 == bukva_Q1:
#             print(f"Буква совпадает")



# for i in range(0, len(S1)):
#     ch_dict[Q1[i]] = S1.count(Q1[i])

#     if Q1[i] == S1[i]:
#         print("correct... Буква совпадает")
#     elif Q1[i] in S1 and count_of_present != 0: # если буква просто не равна, но она есть в слове
#         # print(f"Количество таких букв в слове {count_of_present}")
#         print("present... Вообще, такая буква есть в загаданном слове")
#         count_of_present -= 1
#         # print(f"Количество таких букв в слове осталось {count_of_present}")
#     elif Q1[i] != S1[i]:
#         print("absent... Буква не совпадает")
#     count_of_present = 0