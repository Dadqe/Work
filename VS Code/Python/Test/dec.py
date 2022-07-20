def timer(func):
    print("Засечь время до исполнения функции")
    func()
    print("Получу время выполнения функции")

@timer
def a():
    print("какая-то функция")


a
