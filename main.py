import telebot #module for bots


#some plugins that will be connected
from plugins.ban import blocked
from plugins.unban import unblocked
from content.text import text
from content.other import other
from plugins.start import start
from plugins.everyone_message import message_everyone


#database connection and creation
from connection import *
create_db_new()
    

#main file that registers all commands

#config file
import config


#we use pytelegrambotapi library.
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start2(message):
    start(message)
@bot.message_handler(commands=["ban"])
def bloc(message):
    blocked(message)
@bot.message_handler(commands=["unban"])
def some(message):
    unblocked(message)
@bot.message_handler(commands=["admin_message"])
def reklama(message):
    if message.chat.id == config.main_id:
        bot.send_message(message.chat.id, "your message to be sent: ")
        bot.register_next_step_handler(message, textrek)
    else:
        pass
def textrek(message):
    message_everyone(message)
@bot.message_handler(content_types=['text'])
def tex(message):
    text(message)
#photo #stikeri #video        
@bot.message_handler(content_types=['photo','sticker','video','audio','voice','location','animation','contact','document','dice','poll'])
def other2(message):
    other(message)
bot.polling(none_stop=True)