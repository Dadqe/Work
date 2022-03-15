def sum(a, b):
    result = a + b
    
    with open("result.txt", "w", encoding="utf-8") as file:
        file.write(str(result))
        
def main():
    a = int(input("Введи первое число "))
    b = int(input("Введи второе число "))
    
    sum(a, b)

if __name__ == "__main__":
    main()