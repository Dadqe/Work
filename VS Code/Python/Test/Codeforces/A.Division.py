import time
import random

first_string = int(input())
start_time = time.time()
list_of_rating = [random.randint(-5000, 5000) for n in range(1, first_string+1)]

for rating in list_of_rating:
    if rating <= 1399:
        print("Division 4")
    elif 1400 <= rating <= 1599:
        print("Division 3")
    elif 1600 <= rating <= 1899:
        print("Division 2")
    elif 1900 <= rating:
        print("Division 1")

print("--- %s seconds ---" % (time.time() - start_time))
