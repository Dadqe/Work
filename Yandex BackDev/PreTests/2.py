# Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно читать из файла и выводить ответ в файл

with open('input.txt') as f:
    nums = f.read().split()

a, b = map(int, nums)
result = a + b

with open('output.txt', 'w') as f:
    f.write(str(result))