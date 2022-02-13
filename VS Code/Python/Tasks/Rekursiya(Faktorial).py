def f(num):
    if num == 0:
        return 1
    return f(num-1) * num
print(f(5)) # Выведет число 120