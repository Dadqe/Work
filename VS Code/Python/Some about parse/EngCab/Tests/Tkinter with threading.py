from tkinter import *
import time
import threading

count = 0
while True:
    while count < 3:
        def make_window():
            window = Tk()
            window.title(f"Добро пожаловать в приложение PythonRu #{count}")
            window.geometry("500x200")
            window.mainloop()
        
        t1 = threading.Thread(target=make_window) # Создание потока для открытия окна и продолжения работы
        t1.start()
        print(count)
        print(f"Window #{count} выведено на экран")
        count += 1
        time.sleep(5)
    
    
    
    # try:
    #     window = Tk()
    #     window.title(f"Добро пожаловать в приложение PythonRu #{count}")
    #     window.mainloop()
    # except:
    #     print("что-то пошло не так")
    # finally:
    #     print(count)
    #     count += 1
    #     time.sleep(5)