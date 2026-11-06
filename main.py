import os
import telebot
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "আসসালামু আলাইকুম! আমি ইসলামিক বট")
@bot.message_handler(func=lambda m: True)
def all_msg(message):
    bot.reply_to(message, f"আপনি বলেছেন: {message.text}")
bot.infinity_polling()
