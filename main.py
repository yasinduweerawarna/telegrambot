import os
import telebot

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Start'])
def send_welcome(message):
  bot.reply_to(message, "Hello World..!")

@bot.message_handler(commands=['help'])
def send_message(message):
  bot.send_message(message, "Sorry, Still learning..")

bot.polling()