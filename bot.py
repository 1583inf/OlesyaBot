import telebot
bot = telebot.TeleBot('1512568206:AAHySA7FLNJV8pLVfo8sW6YoLqoiRS4Du58')
@bot.message_handler(commands=['start', 'help'])
def sens_welcome(message):
    bot.reply_to(message, 'Я бот, Приятно познакомиться,  {message.from_user.first_name)')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower()=='привет':
        bot.send_message(message.from_user.id, 'привет')
    else:
        bot.send_message(message.from_user.id, 'не понимаю')
bot.polling(none_stop = True)
