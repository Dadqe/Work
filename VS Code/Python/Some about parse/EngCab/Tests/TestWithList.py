lst = ['1info']
date_time = '10.03.2022 11:38:39'
usluga = 'asd'
lst.append(date_time)
lst.append(usluga)
# lst = ["1info", date_time, usluga]
print(lst)
# write_lst = []
# for line in lst:
#     write_lst.append(line + "\n")
# Вроде что-то типа генератора списка или типа того...
# write_lst = [f"{line}\n" for line in lst]

with open('data3.txt', "w", encoding='utf-8') as file:
    file.writelines([f"{line}\n" for line in lst])