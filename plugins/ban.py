from connection import database_query
import config
import sqlite3
import telebot
bot = telebot.TeleBot(config.TOKEN)
def blocked(message):
    try:
        if message.chat.id == config.main_id:
            #fromm = str(message.from_user.id)
            #name = message.from_user.first_name
            get = database_query("SELECT user_id FROM USERS WHERE messageid = ?",(message.reply_to_message.message_id,))
            for i in get:
                print(i[0])
                get2 = database_query("SELECT user_id FROM blocked WHERE user_id = ?",(i[0],))
                if get2 == []:
                    bot.send_message(i[0],config.ban)
                    bot.send_message(message.chat.id, "you blocked " + str(i[0]))
                    database_query("INSERT INTO blocked VALUES (?)",(i[0],))
        else:
            bot.send_message(message.chat.id, "you are not admin!")
    except Exception as ee:
        print("error in block" + str(ee))