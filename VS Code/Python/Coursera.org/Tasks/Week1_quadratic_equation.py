# import sys 

# Использование коэффициентов из командной строки при вызове программы
# a = int(sys.argv[1]) 
# b = int(sys.argv[2]) 
# c = int(sys.argv[3])

# Использование коэффициентов, которые сам задам в программе
# a = int(3)
# b = int(7)
# c = int(-6)

# def sqrt(num):
#     return int(num ** 0.5)

def equation_solution(*args):
    def sqrt(num):
        return int(num ** 0.5)

    a = int(args[0])
    b = int(args[1])
    c = int(args[2])
    D = b ** 2 - 4 * a * c
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)

    print(f"x1 = {x1} \nx2 = {x2}")
    
equation_solution(3, 7, -6)

# Пример работ
# $ python solution.py 1 -3 -4
# 4
# -1
# $ python solution.py 13 236 -396
# 1
# -19