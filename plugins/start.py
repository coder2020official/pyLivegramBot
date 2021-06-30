from connection import database_query
import telebot
import config
import sqlite3
bot = telebot.TeleBot(config.TOKEN)
def start(message):
    try:
        bot.send_message(message.chat.id, config.start)
        info = database_query("SELECT user_id FROM user WHERE user_id = ?",(message.from_user.id,))
        if info == []:
            database_query("INSERT INTO user VALUES(?)",(message.from_user.id,))
    except Exception as e:
        print(str(e))