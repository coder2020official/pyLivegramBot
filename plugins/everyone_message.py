from connection import database_query, database_query_spec
import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
def message_everyone(message):
    usrs = database_query_spec("SELECT user_id FROM user")
    for i in usrs:
        try:
            bot.copy_message(i[0],message.chat.id, message.message_id)
        except:
            print("error!!")