import time
from threading import Thread
from tkinter import *

# def sleepMe(i):
#     print("Поток %i засыпает на 5 секунд.\n" % i)
#     time.sleep(5)
#     print("Поток %i сейчас проснулся.\n" % i)

# for i in range(10):
#     th = Thread(target=sleepMe, args=(i, ))
#     th.start()


def sleepMe(i):
    print("Поток %i засыпает на 5 секунд.\n" % i)
    window = Tk()
    window.title(f"Добро пожаловать в приложение PythonRu #{i}")
    window.mainloop()
    time.sleep(5)
    print("Поток %i сейчас проснулся.\n" % i)

for i in range(4):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
