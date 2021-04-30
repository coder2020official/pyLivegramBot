import config
import sqlite3
import telebot
bot = telebot.TeleBot(config.TOKEN)
def blocked(message):
    try:
        db = sqlite3.connect("./users.db", check_same_thread=False)
        sql = db.cursor()
        if message.chat.id == config.main_id:
            #fromm = str(message.from_user.id)
            #name = message.from_user.first_name
            sql.execute("SELECT user_id FROM USERS WHERE messageid = ?",(message.reply_to_message.message_id,))
            db.commit()
            Lusers = sql.fetchall()
            for i in Lusers:
                print(i[0])
                sql.execute("SELECT user_id FROM blocked WHERE user_id = ?",(i[0],))
                if sql.fetchone() is None:
                    bot.send_message(i[0],config.ban)
                    bot.send_message(message.chat.id, "you blocked " + str(i[0]))
                    sql.execute("INSERT INTO blocked VALUES (?)",(i[0],))
                    db.commit()
        else:
            bot.send_message(message.chat.id, "you are not admin!")
        sql.close()
        db.close()
    except Exception as ee:
        print("error in block" + str(ee))