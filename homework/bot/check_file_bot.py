import telebot

bot = telebot.TeleBot('6508941706:AAGLaFiuyOBpJSpdWGZjbx-6FdJuOXhXnF8')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите ваше число')

bot.polling(non_stop=True)