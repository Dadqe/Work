# N = 2 # число открытых вакансий в новом офисе
# vac_and_cand = ceo,1 # название вакансий и максимальное число кандидатов на эту вакансию
# humans = 3 # число участвоваших в отборочном соревновании кандидатов
# name_vac_tasks_mistakes = arcady_volozh,ceo,6,100 # индентификатор кандидата, название интересующей его вакансии, количество решенных кандидатом задач и начисленный ему штраф соответственно

# N = int(input())
# vacs = [input() for i in range(N)]
# H = int(input())
# names = [input() for i in range(H)]

N = 2            
vacs = ['ceo,1', 'co_founder,1']
H = 3
names = ['arcady_volozh,ceo,6,100', 'elon_musk,ceo,5,0', 'ilya_segalovich,co_founder,6,10']

vacs_dict = {}

for i in range(len(names)):
    if names[i].split(",")[1] in vacs_dict:
        vacs_dict[names[i].split(",")[1]].append((names[i].split(",")[0], names[i].split(",")[2], names[i].split(",")[3]))
    else:
        vacs_dict[names[i].split(",")[1]] = [tuple([names[i].split(",")[0], names[i].split(",")[2], names[i].split(",")[3]])]

# vac = names[0].split(",")[1]
# print(type(vac))

print(vacs_dict)
confirmed = []

# Создать словарь, а не кортежи с наименованием вакансии и желающими туда попасть. Потом забрать этих желающих и отфильтровать по задачам, если количество задач не одинаково, иначе по индексу штрафов







# for i in range(int(N)):
#     vacs.append(tuple(input().split(",")))
# print(vacs)

# lst = list()
# for i in range(int(input()): 
#     lst.append(input())