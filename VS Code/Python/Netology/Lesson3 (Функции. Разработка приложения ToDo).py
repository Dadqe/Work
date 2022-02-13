# import random

TODOS = {}
# Задачи = список
# Дата (str) -> [список задач]


RANDOM_TASKS = [
    'Написать Гвидо писмо',
    'Выучить Python',
    'Записаться на курс в нетологию',
    'Посмотреть сериал "Рик и Морти"'
]


HELP = '''
help - напечатать команды
add/todo/добавить - добавить задачу
random - добавить случайную задачу на сегодня
show/показать - показать все задачи
exit/всё/выход
'''

print(f'Доступные команды:{HELP}')

run = True

while run:  # run == True (run is True)
    command = input('Введите команду: ').lower()

    if command == 'help':
        print(HELP)
        
    elif command == 'add' or command == 'todo' or command == 'добавить':
        date = input('Введите день: ').title()
        task = input('Введите задачу: ')
        print(date)
        print(task)
        print(TODOS) # Пока что будет пустой, потому что не выполнялось добавление ключа и значения в словарь. Поэтому переходит дальше
        
        # Такая дата есть в словаре
        if date in TODOS:
            # print('Дата есть в словае')
            TODOS[date].append(task)
            print(TODOS)
        # Такой даты нет
        else:
            # print('Даты нет в словаре')
            TODOS[date] = [task] # item: date -> [task] # Как я понял, тут добавляем такую дату и значение для этой даты. (т.е. Key -> Value) Если уже есть, тогда эту ситуацию игнорит код, выполнит предыдущий шаг до else
        print(f'Задача {task} добавлена на дату {date}')
        print(TODOS)
        # print(TODOS)
    elif command == 'show' or command == 'показать' or command == 'print': # А можно ли тут сравнить с переменной, а для этой переменой уже задать какие-то несколько значений, т.е. сделать переменную с кучей кавычек и наименованиями внутри, ну, список, и если введённый текст встретится в списке, то выполнить?!!!!!!
        date = input('Введите дату: ')
        if date.title() in TODOS:
            print(f'{date.upper()} надо сделать:')
            for task in TODOS[date.title()]:
                print(task)
        else:
            print('Такой даты нет')
    elif command == 'exit' or command == 'выход' or command == 'всё':
        print('Спасибо за использование! До свидания!')
        break
    
    elif command == 'random':
        task = random.choice(RANDOM_TASKS)
        date = 'today'
        if date in TODOS:
            # print('Дата есть в словае')
            TODOS[date].append(task)
        # Такой даты нет
        else:
            # print('Даты нет в словаре')
            TODOS[date] = [task] # item: date -> [task] # Как я понял, тут добавляем такую дату, если уже есть, тогда эту ситуацию игнорит код
        print(f'Задача {task} добавлена на дату {date}')
    else:
        print('Неизвестная команда, запусти по-новой или уходи')

# Бонус: сделтаь так, чтобы команды были регистронезависимы, то бишь можно было вводить как попало add/ADD/aDD/Add/... -> add

