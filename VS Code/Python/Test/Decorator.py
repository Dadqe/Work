def func_decorator(func):
    def wrapper():
        print("---Что-то делаем перед вызовом фуркции---")
        func()
        print("---Что-то делаем после вызова функции---")
    return wrapper()

def some_func():
    print("Вызов функции some_func")

f = func_decorator(some_func)
f