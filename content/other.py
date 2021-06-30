from connection import database_query
import telebot
import sqlite3
import config
bot = telebot.TeleBot(config.TOKEN)
def other(message):
    try:
        if message.chat.id != config.main_id:
            if message.forward_from == None:
                get = database_query("SELECT user_id FROM blocked WHERE user_id = ?",(message.from_user.id,))
                if get != []:
                    bot.send_message(message.chat.id, config.banned)
                else:
                    q = bot.forward_message(config.main_id, message.chat.id, message.message_id)
                    database_query("INSERT OR IGNORE INTO USERS VALUES(?,?,?,?)",(message.from_user.id,message.from_user.first_name, q.message_id, message.text))
                    bot.send_message(message.chat.id, config.text_message)
                    print(message.message_id)
            else:
                bot.send_message(message.chat.id, config.notallowed)
        elif message.chat.id == config.main_id:
            if message.reply_to_message is None:
                bot.forward_message(config.main_id, message.chat.id, message.message_id)
                database_query("INSERT OR IGNORE INTO USERS VALUES(?,?,?,?)",(message.from_user.id,message.from_user.first_name, message.message_id, message.text))
                bot.send_message(message.chat.id, config.text_message)
            elif message.reply_to_message is not None:
                print(message.reply_to_message.message_id)
                get = database_query("SELECT user_id FROM USERS WHERE messageid = ?",(message.reply_to_message.message_id,))
                for i in get:
                    bot.copy_message(i[0],message.chat.id, message.message_id)
    except telebot.apihelper.ApiException:
        bot.send_message(message.chat.id, config.blocked)