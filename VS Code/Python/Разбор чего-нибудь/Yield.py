def nextCube():
    acc = 1
 
    # Бесконечный цикл
    while True:
        yield acc**3                
        acc += 1 # После повторного обращения
                # исполнение продолжится отсюда
 
# Ниже мы запрашиваем у генератора 
# и выводим ровно 15 чисел
count = 1
for num in nextCube():
    if count > 3:
        break   
    print(num)
    count += 1
