# Принцип работы функции

# def print_hello():
#     print("Hello")
    
# print_hello()

# def my_function():
#     x =1
#     y = 2
#     s = x + y 
    
# my_function()

# def my_sum(a, b):
#     print(a+b)
    
# my_sum(2, 1) # Числа в скобке это параметры функции
# my_sum(123324, 5654)


# def odd_append_to_list(l, number):
#     if number % 2 == 0:
#         l.append(-1)
#     else:
#         l.append(number)
        
# my_list = []
# print(my_list)
# odd_append_to_list(my_list, 3)
# print(my_list)
# odd_append_to_list(my_list, 4)
# print(my_list)

# result = odd_append_to_list(my_list, 4)
# print(result)
# print(my_list)

# def smallify_number(number):
#     if number > 1000:
#         number = 1000
    # return number # Возвращает результат работы функции

# x =1001
# x= smallify_number(x)
# print(x)

# def mod_sum(a, b):
#     return (a + b) % 2

# x = mod_sum(1, 2)
# y = mod_sum(3, 1345)
# print(x)
# print(y)


# result = print(5)
# print(result)


def my_input(prompt_list):
    relust_list = list()
    for prompt in prompt_list:
        user_input = input(prompt)
        result_list.append()(user_input)
    return relust_list

person = my_input(['Как тебя зовут?: ', 'Сколько тебе лет?: '])
print(person)



# Конспект

#нахождение суммы элементов списка array
# sum = 0
# array = [45, 7, -934, 0, 2839]
# for i in array:
#    sum += i
# print(sum)

