# """Что-то с генераторами, переменная b - генератор, которая генерирует, похоже, список, но type = class 'generator' и потом итерируемся по этому генератору"""
import sys
# from a import a
sys.path.insert(0, 'E:/Tokens/KinoPoisk/')
from Token import token

# sys.path.insert(0, 'E:/Work/VS Code/Python/')


# # a = [1,2,3,4]
# b = (2*x for x in a)
# for i in b:
#     print(i, end=' ')

# print("finally")
# print('commit')

print(type(token))
