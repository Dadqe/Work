# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

# def positive_sum(arr):
#     result = 0
#     if len(arr) != 0:
#         for num in arr:
#             if not '-' in num:
#                 result += int(num)
#         return result
#     else:
#         return 0

# def positive_sum(arr):
#     result = 0
#     if len(arr) != 0:
#         for num in arr:
#             if num > 0:
#                 print(num, type(num))
#         return result
#     else:
#         return 0


def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# positive_sum([1,2,3,4,5])
positive_sum([])