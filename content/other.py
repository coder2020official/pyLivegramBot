import telebot
import sqlite3
import config
bot = telebot.TeleBot(config.TOKEN)
def other(message):
    try:
        db = sqlite3.connect('users.db', check_same_thread=False)
        sql = db.cursor()
        if message.chat.id != config.main_id:
            if message.forward_from == None:
                sql.execute("SELECT user_id FROM blocked WHERE user_id = ?",(message.from_user.id,))
                db.commit()
                if sql.fetchone() is not None:
                    bot.send_message(message.chat.id, config.banned)
                else:
                    q = bot.forward_message(config.main_id, message.chat.id, message.message_id)
                    sql.execute("INSERT OR IGNORE INTO USERS VALUES(?,?,?,?)",(message.from_user.id,message.from_user.first_name, q.message_id, message.text))
                    db.commit()
                    bot.send_message(message.chat.id, config.text_message)
                    print(message.message_id)
            else:
                bot.send_message(message.chat.id, config.notallowed)
        elif message.chat.id == config.main_id:
            if message.reply_to_message is None:
                bot.forward_message(config.main_id, message.chat.id, message.message_id)
                sql.execute("INSERT OR IGNORE INTO USERS VALUES(?,?,?,?)",(message.from_user.id,message.from_user.first_name, message.message_id, message.text))
                db.commit()
                bot.send_message(message.chat.id, config.text_message)
            elif message.reply_to_message is not None:
                print(message.reply_to_message.message_id)
                sql.execute("SELECT user_id FROM USERS WHERE messageid = ?",(message.reply_to_message.message_id,))
                db.commit()
                Lusers = sql.fetchall()
                for i in Lusers:
                    bot.copy_message(i[0],message.chat.id, message.message_id)
        sql.close()
        db.close()
    except telebot.apihelper.ApiException:
        bot.send_message(message.chat.id, config.blocked)