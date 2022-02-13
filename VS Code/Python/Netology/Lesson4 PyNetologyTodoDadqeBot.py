import telebot #pip3 install --user pytelegrambotapi это установить сначала надо

TOKEN = '1682777516:AAFZnoydCAfQ1yJnVp4qz4SJlxSdbNS4xmg'
# echoBot будет отвечать на сообщение тем же самым сообщением, которое мы ему прислали
bot = telebot.TeleBot(TOKEN)

@bot.meassage_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)
    
bot.polling(none_stop=True)
