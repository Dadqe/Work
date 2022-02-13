# import sys

# digit_string = sys.argv[1]

def print_stairs():
    # Для вывода через консоль
    # numbers = digit_string
    
    # Для вывода через VSCode
    numbers = 3
    number = numbers
    while numbers != 0:
        space = numbers - 1
        print(" " * space, end="")
        step = number - space
        print("#" * step)
        numbers -= 1    

# Вызов func ничего не возвращает поэтому print(func(int(sys.argv[1]))) это самое ничего и выводит в консоль. Замените на func(int(sys.argv[1])) для получения ожидаемого результата )
print_stairs()
# print("" * (numbers - 1))
# print("#" * numbers)
    
# Напишу цифру 3, должно получиться:
#     __#
#     _##
#     ###