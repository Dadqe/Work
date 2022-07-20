yourlist = [[1, 2], [3, 4], [5, 6]]
choice = int(5)
n = [i for i in yourlist if choice in i]
# n = []
# for i in yourlist:
#     if choice in i:
#         n.append(i)

print(n)
