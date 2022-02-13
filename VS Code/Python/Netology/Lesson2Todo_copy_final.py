
HELP = '''
help - напечатать команды
add/todo/добавить - добавить задачу
show/показать - показать все задачи
'''
# print (HELP)
Сегодня = [] # Сегдоня = list()  Варианты для создания чистого листа
Завтра = []
Другое = []

print('Доступные команды:')
print(HELP)

run = True

while run:  # run == True (run is True)
    command = input('Введите команду: ').casefold()

    if command == 'help':
        print(HELP)
        
    elif command == 'add' or command == 'todo' or command == 'добавить':
        date = input('Введите день: ').title()
        
        if date == 'Сегодня':
            task = input('Введите задачу: ')
            Сегодня.append(task)
            print(f'Задача {task} добавлена')
            question = input('Хотите добавить ещё? ').casefold()
            
            while question == 'да':
                task = input('Введите задачу: ')
                Сегодня.append(task)
                print(f'Задача {task} добавлена')
                question = input('Хотите добавить ещё? ').casefold()
                
        elif date == 'Завтра':
            task = input('Введите задачу: ')
            Завтра.append(task)
            question = input('Хотите добавить ещё? ').casefold()
            
            while question == 'да':
                task = input('Введите задачу: ')
                Завтра.append(task)
                print(f'Задача {task} добавлена')
                question = input('Хотите добавить ещё? ').casefold()
                
        else:
            task = input('Введите задачу: ')
            Другое.append(task)
            question = input('Хотите добавить ещё? ').casefold()
            while question == 'да':
                
                task = input('Введите задачу: ')
                Другое.append(task)
                print(f'Задача {task} добавлена')
                question = input('Хотите добавить ещё? ').casefold()
                
    elif command == 'show' or command == 'показать':
        if len(Сегодня) != 0:  # Или if not Сегодня!!!!!(как где-то посчитали более правильным) мб вернуть отсюда надо будет print('Сегодня день свободен')  # Можно сделать так, если в списке ничего нет, следовать к следующему списку, и так с каждым, иначе или через elif прописывать, что
            print('Сегодня надо сделать:', ', '.join(Сегодня))
            
        if len(Завтра) != 0:
            # print('Завтра делать нечего')
            print('Завтра надо сделать:', ', '.join(Завтра))
            
        if len(Другое) != 0:
            # print('Другого ничего нет')
            print('Другое:', ', '.join(Другое))
            
    elif command == 'exit' or command == 'выход' or command == 'всё':
        print('Спасибо за использование! До свидания!')
        run = False
        
    else:
        print('Неизвестная команда, запусти по-новой или уходи')
        run = False

# Бонус: сделтаь так, чтобы команды были регистронезависимы, то бишь можно было вводить как попало add/ADD/aDD/Add/... -> add

