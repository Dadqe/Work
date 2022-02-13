import telebot
import random

TOKEN = '1682777516:AAFZnoydCAfQ1yJnVp4qz4SJlxSdbNS4xmg'

bot = telebot.TeleBot(TOKEN)

TODOS = {}

RANDOM_TASKS = [
    'Написать Гвидо писмо',
    'Выучить Python',
    'Записаться на курс в нетологию',
    'Посмотреть сериал "Рик и Морти"'
]

RANDOM_DATES = ['today', 'yesterday', '08-03-2021']

HELP = '''
* /help - напечатать команды
* /add/todo/добавить <date> <task> - добавить задачу <task> на дату <date>
* /random - добавить случайную задачу на сегодня
* /random2 - добавить задачу "Почистить зубы" сейчас "Почистить зубы" на случайную дату 
* /print/show/показать <date> - показать задачи на дату <date>
* /exit/выход/всё
'''

def add_todo(task, date):
    if date in TODOS:
        TODOS[date].append(task)
    else:
        TODOS[date] = [task]

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['random'])
def add_random(message):
    task = random.choice(RANDOM_TASKS)
    date = 'сегодня'
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=['add' , 'todo'])
def add(message):
    # команду хотим в таком формате: /todo <date> <task>
    splitted_command = message.text.split(maxsplit=2) # Параметр в скобках, что б он максимум 2 раза разбил строку по пробелам...., что б всё, что после 2го слова было в одной строчке в списке
    date = splitted_command[1]
    task = splitted_command[2]
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')

@bot.message_handler(commands=['print', 'show'])
def show(message):
    print(message.text)
    splitted_command = message.text.split() # [/print, <date>] Создаст спиосок, разделит строчку на список с несколькими строками внутри 
    date = splitted_command[1]
    if date in TODOS:
        text = date.upper() + '\n'
        for task in TODOS[date]:
            text += f'[ ] {task}\n' # += -> text = text + f'[ ] {task}'
    else:
        text = 'На эту дату задач нет'
    bot.send_message(message.chat.id, text)

@bot.message.handler(content_types=['sticker']) # Пробовали стикеры добавить, что б он в ответ их отсылал
def echo(message.text):
    bot.send_message(message.chat.id, message.text)

# @bot.message_handler(content_types=["text"])
# def echo(message):
#     print(message.text)
#     bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)