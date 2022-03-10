
# def square(self, value):
#     return value*value

# cls = type("MyClass", (), {"square": square})
# print(cls.square(5))

# lst = [3, 6, 2, 1]
# print(sorted(lst) == lst.sort())

# lst = [lambda x: x**2(i) for i in range(1)]
# print(lst)

# x = False
# y = True
# z = False
# if x or not y:
#     print(1)
# elif not x and not y and not z:
#     print(2)
# elif x or y and not y and x:
#     print(3)
# else:
#     print(4)

# kvps = {'user', 'oil', 'petroleum'}
# print(kvps['oil'])

# str = 'abcd'
# print(reversed(str))

# lst1 = [1, 2, 3]
# lst2 = lst1
# lst2[0] = 10

# print(lst1)

# my_str = 'Hello, World!'
# my_str[0] = 'h'
# print(my_str)

# print(all(x >= 3 and x < 10 for x in range(3,10)))

# lst = [1, 2, 3, 4, 5]
# print(lst[:4])


# class Class1:
#     def m(self):
#         print("in Class1")
        
# class Class2(Class1):
#     def m(self):
#         print("in Class2")
        
# class Class3(Class1):
#     def m(self):
#         print("In class3")
        
# class Class4(Class2, Class3):
#     pass

# obj = Class4()
# obj.m()


# import copy

# lst = [1, 2, 3, [4, 5, 6]]
# def f(x):
#     if isinstance(x, list):
#         x = copy.copy(x)
#         x.append(10)
#     else:
#         x += 10
        
#     return x

# result = f(lst)
# print(lst)


# lst = [1, 2, 3]
# def f(x):
#     if isinstance(x, list):
#         x.append(10)
#     else:
#         x += 10
        
#     return x

# result = f(lst)
# print(lst)

# lst = [3, 6, 2, "abc"]
# print(lst.sort())

