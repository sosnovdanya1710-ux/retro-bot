import os
import subprocess
import sys

# Автоматическая установка библиотек, чтобы не создавать лишний файл
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI", "flask"])

import telebot
from flask import Flask
from threading import Thread
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

bot = telebot.TeleBot('8780460653:AAHIT2p0MUzZHSi6aF_424zntgN3KSnzo3A')

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is alive"

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Открыть профиль', web_app=WebAppInfo(url='[https://sosnovdanya1710-ux.github.io/банан/](https://sosnovdanya1710-ux.github.io/банан/)'))
    markup.add(btn)
    bot.send_message(message.chat.id, "Привет! Кнопка ниже:", reply_markup=markup)

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.infinity_polling()
            
