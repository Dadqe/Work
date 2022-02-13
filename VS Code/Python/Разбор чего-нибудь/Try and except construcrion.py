

def division(a, b):
    try:
        c = a / b
        return int(c)
    except:
        e = print("Деление на ноль, используй другой делитель")
        return e
        
result = division(8, 2)
print(result)