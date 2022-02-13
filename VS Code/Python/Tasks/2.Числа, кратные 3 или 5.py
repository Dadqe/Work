finish_sum = 0
n = 1000
for numbers in range (0, n):
    if numbers % 3 == 0 or numbers % 5 == 0:
        finish_sum += numbers
print(finish_sum)

a=[x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(a))
