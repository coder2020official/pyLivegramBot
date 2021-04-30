import telebot
import sqlite3
import config

bot = telebot.TeleBot(config.TOKEN)
def message_everyone(message):
    db = sqlite3.connect('users.db', check_same_thread=False)
    sql = db.cursor()
    sql.execute("SELECT user_id FROM user")
    Lusers = sql.fetchall()
    for i in Lusers:
        try:
            bot.copy_message(i[0],message.chat.id, message.message_id)
        except:
            print("error!!")
    sql.close()
    db.close()
