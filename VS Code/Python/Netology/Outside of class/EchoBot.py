import telebot # импорт библиотеки

TOKEN = '1682777516:AAFZnoydCAfQ1yJnVp4qz4SJlxSdbNS4xmg' # определение переменной TOKEN

bot = telebot.TeleBot(TOKEN) # создание специальной переменной, которая будеть управлять нашим ботом

@bot.message_handler(content_types=["text"]) # регистрация функции обработчика Строчка говорит боту, что сообщение, соответствующее следующему правилу:  content_types=["text"] (тип контента текст) нужно обработать функцией, которая идёт ниже
def echo(message):
    print(message.text) # что б он печатал на компьютер, при запуске кода, те сообщения, которые он получает
    bot.send_message(message.chat.id, message.text)
# Сказали боту - бесконечно отправлять запросы на получение сообщений
bot.polling(none_stop=True)


import telebot

TOKEN = '1682777516:AAFZnoydCAfQ1yJnVp4qz4SJlxSdbNS4xmg'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def echo(message):
    if 'Данил' in message.text:
        print(message.text)
        greeting = "Ба! Знакомые все лица"
        bot.send_message(message.chat.id, greeting)
    else:
        print(message.text)
        bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)


# Решение с сайта

import telebot

token = ''

bot = telebot.TeleBot(token)

my_name = 'Дима'


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text) # Придумали переменную для имени и ввели её в функцию(условие) Задали в условии только переменную, как назвать переменную text а потом уже за функцией дали команду напечатать текст -> укоротили код.


bot.polling(none_stop=True)