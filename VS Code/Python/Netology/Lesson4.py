import random

TODOS = {}
# Задачи = список
# Дата (str) -> [список задач]


RANDOM_TASKS = [
    'Написать Гвидо письмо',
    'Выучить Python',
    'Записаться на курс в нетологию',
    'Посмотреть сериал "Рик и Морти"'
]

RANDOM_DATES = ['today', 'yesterday', '08-03-2021']


HELP = '''
help - напечатать команды
add/todo/добавить - добавить задачу
random - добавить случайную задачу на сегодня
random2 - добавить задачу "Почистить зубы" сейчас "Почистить зубы" на случайную дату 
show/показать - показать все задачи
'''

# Имя_функции = (Блок кода (параметры))

def add_todo(task, date):
    if date in TODOS:
        TODOS[date].append(task)
    else:
        TODOS[date] = [task] # item: date -> [task]


print(f'Доступные команды:{HELP}')

run = True

while run:  # run == True (run is True)
    command = input('Введите команду: ').lower()

    if command == 'help':
        print(HELP)
        
    elif command == 'add' or command == 'todo' or command == 'добавить':
        date = input('Введите день: ').title()
        task = input('Введите задачу: ')
        add_todo(task, date)
        print(f'Задача {task} добавлена на дату {date}')
        print(TODOS)
    elif command == 'show' or command == 'показать' or command == 'print':
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
        add_todo(task, date)
    
    elif command == 'random2':
        task = 'Позавтракать'
        date = random.choice(RANDOM_DATES)
        add_todo(task, date)
    
    else:
        print('Неизвестная команда, запусти по-новой или уходи!')

# Бонус: сделтаь так, чтобы команды были регистронезависимы, то бишь можно было вводить как попало add/ADD/aDD/Add/... -> add

