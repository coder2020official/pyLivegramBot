from connection import database_query
import telebot
import sqlite3
import config
bot = telebot.TeleBot(config.TOKEN)
def unblocked(message):
    try:
        if message.chat.id == config.main_id:
            Lusers = database_query("SELECT user_id FROM USERS WHERE messageid = ?",(message.reply_to_message.message_id,))
            for i in Lusers:
                print(str(i[0]) + " mine")
                get_blocked = database_query("SELECT user_id FROM blocked WHERE user_id = ?",(i[0],))
                database_query("DELETE FROM blocked WHERE user_id = ?",(i[0],))
                bot.send_message(i[0],"you were unblocked")
                bot.send_message(message.chat.id, "you unblocked " + str(i[0]))
        else:
            bot.send_message(message.chat.id, "you are not admin!")
    except Exception as ee:
        print("error in block" + str(ee))