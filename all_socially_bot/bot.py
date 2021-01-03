# ..........TELEGRAM BOT.............
# IT is used to find the Instagram Handle with just your UserName and try to give you the
# result directly onto your telegram channel.
#
# Developed by Abhishek Jaiswal 
# Github ID : github@abhishek-iiit

import time
import telebot

TOKEN = "xxxxxxxx.......xxxxxxxxxxxx"
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message
def send_welcome(message):
    bot.reply_to(message, 'Welcome,to All_Socially,get Social Media Handle link directly,for more info type /help')

@bot.message_handler(commands=['help']) # help message
def send_welcome(message):
    bot.reply_to(message, "type any Social Media Handle starting with '@'")

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(15)
