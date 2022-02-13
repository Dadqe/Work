import telebot
import translators


token = "5164752718:AAGKBu37WzAKG9mP4c3EbahA1ynPvllFn2c"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
    answer = 'Hello, ' + message.chat.first_name
    bot.send_message(message.chat.id, answer)

# Новая функция
@bot.message_handler(content_types=["text"])
def translate(message):
    txt = message.text
    answer = translators.google(txt, from_language='auto', to_language='en')
    bot.send_message(message.chat.id, answer)

# Запускаем бота.
# Если все хорошо, ячейка будет стоять запущенной, пока ее вручную не остановить.
bot.polling(none_stop=True)