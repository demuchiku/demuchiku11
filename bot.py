import telebot

TOKEN = "8873405167:AAF7BU2f-QdAjhBDU9I3pijM5jNiEM_HVRc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я работаю 🤖")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Доступные команды:\n/start - запуск\n/help - помощь")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, f"Ты написал: {message.text}")

bot.polling()