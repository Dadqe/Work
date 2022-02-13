import random

number = random.randint(0, 101)

while True:
    
    answer = input('Введите число: ')
    if not answer or answer == 'exit':
        break 
    
    if not answer.isdigit():
        print('Введите правильное число!')
        continue
    user_answer = int(answer)
    
    if user_answer > number:
        print('Загаданное число меньше')
    elif user_answer < number:
        print('Загаданное число больше')
    else:
        print('Совершенно верно!')
        break 
    
# (Или так можно) ok == True: вместо while True:
# а потом будет вместо break ok = False
# и в третью строчку можно написать конкретное число, а так вот рандомное ставит