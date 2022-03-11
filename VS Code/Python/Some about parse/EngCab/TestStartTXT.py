import os
import subprocess
import time

count = 0
while count < 4:
    os.startfile(r'C:\Work\VS Code\Python\Some about parse\EngCab\Plan.txt')
    print(f'Блокнот #{count} открыт')
    count += 1
    time.sleep(3)
    
 
# if str=="Блокнот":
#     os.startfile(r'C:\Work\VS Code\Python\Some about parse\EngCab\Plan.txt')
# elif str=="Программы":
#     subprocess.Popen('explorer "c:\program Files"')