# data = []
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# data1 = data.append(list(fibonacci(5)))
# print(data1)

# result = 0

# for i in range(10):
#     if i % 2 != 0:
#         continue
#     result += i
# print(result)

# num_steps = int(input())
num_steps = 5
for i in range(num_steps):
    print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")