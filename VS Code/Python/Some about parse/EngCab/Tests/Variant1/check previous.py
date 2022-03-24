

with open('data3.txt', 'r', encoding='utf-8') as file:
    previous_data = file.read()

print(type(previous_data))
print(previous_data)

data = "Ведение ЭПО"

if data in previous_data:
    print("Предыдущие данные есть уже")
    