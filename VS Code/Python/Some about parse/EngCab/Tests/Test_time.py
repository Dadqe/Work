import time


start_time = time.time()
for x in range(1, 1000 + 1):
    print(x)
finish_time = time.time()


print(f"start: {start_time}")
print(f"finish: {finish_time}")
print(f"delta: {finish_time - start_time}")