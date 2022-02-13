# Что-то с декораторами https://habr.com/ru/post/141411/

# Конечно, можно вкладывать декораторы друг в друга, например так:

def bread(func):
    def wrapper():
        print("</------\>")
        func()
        print("<\______/>")
    return wrapper
 
def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper
 
# def sandwich(food="--ветчина--"):
#     print(food)
 
# sandwich()

# sandwich = bread(ingredients(sandwich))
# sandwich()

# И используя синтаксис декораторов:
    
@bread
@ingredients
def sandwich(food="--ветчина--"):
    print(food)
 
sandwich()

# # Следует помнить о том, что порядок декорирования ВАЖЕН:
# @ingredients
# @bread
# def sandwich(food="--ветчина--"):
#     print food
 
# sandwich()
# #выведет:
# # #помидоры#
# # </------\>
# # --ветчина--
# # <\______/>
# # ~салат~

# # Вызов декоратора без @
# def my_decorator(func):
#     print("Я обычная функция")
#     def wrapper():
#         print("Я - функция, возвращаемая декоратором")
#         func()
#     return wrapper
 
# # Так что, мы можем вызывать её, не используя "@"-синтаксис:
 
# def lazy_function():
#     print("zzzzzzzz")
 
# decorated_function = my_decorator(lazy_function)

# decorated_function()