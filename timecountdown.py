# -*- coding: utf-8 -*-﻿
'''__author__ = 'Sergey'
from datetime import datetime
from datetime import date
rus = datetime(int(2017), int(5), int(31))
now = datetime.now()
import datetime
out = datetime.timedelta(now, rus)
print(out)'''
#continuous-integration
import telebot

technoconf = -1001070076534
me = 94026383
sup = "BQADAgADrQEAAm29TQUoveU--qPBlAI"
token = "162565626:AAFLNGoG9eDiR0r_5w9_WYcHZgErnIbS68w"
bot = telebot.TeleBot(token)

import datetime


rus = datetime.datetime(2017, 6, 9, 10, 00)
math = datetime.datetime(2017, 6, 2, 10, 00)
phys = datetime.datetime(2017, 6, 7, 10, 00)
it = datetime.datetime(2017, 5, 29, 10, 00)

# print('Русский через',c)
# bot.send_message(technoconf, "Русский через")
# bot.send_message(technoconf, drus)

@bot.message_handler(commands=['rus'])
def handle_text(message):
    now = datetime.datetime.now()
    drus = rus - now
    bot.send_message(message.chat.id, drus, reply_to_message_id=message.message_id)


@bot.message_handler(commands=['math'])
def handle_text(message):
    now = datetime.datetime.now()
    dmath = math - now
    bot.send_message(message.chat.id, dmath, reply_to_message_id=message.message_id)


@bot.message_handler(commands=['phys'])
def handle_text(message):
    now = datetime.datetime.now()
    dphys = phys - now
    bot.send_message(message.chat.id, dphys, reply_to_message_id=message.message_id)


@bot.message_handler(commands=['ikt'])
def handle_text(message):
    now = datetime.datetime.now()
    dit = it - now
    bot.send_message(message.chat.id, dit, reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Скока до русича?":
        now = datetime.datetime.now()
        drus = rus - now
        bot.send_message(message.chat.id, drus, reply_to_message_id=message.message_id)
    if message.text == "Скока до матеши?":
        now = datetime.datetime.now()
        dmath = math - now
        bot.send_message(message.chat.id, dmath, reply_to_message_id=message.message_id)
    if message.text == "Скока до физеки?":
        now = datetime.datetime.now()
        dphys = phys - now
        bot.send_message(message.chat.id, dphys, reply_to_message_id=message.message_id)
    if message.text == "Скока до икт?":
        now = datetime.datetime.now()
        dit = it - now
        bot.send_message(message.chat.id, dit, reply_to_message_id=message.message_id)
    if message.text == "Люблю тебя":
        bot.send_message(message.chat.id, "Мур <3", reply_to_message_id=message.message_id)
    if message.text == "Скока до сессии?":
        bot.send_message(message.chat.id, "Неделя", reply_to_message_id=message.message_id)
    if message.text == "Скажи физика круто":
        bot.send_message(message.chat.id, "физика круто", reply_to_message_id=message.message_id)    
    if message.text == "Ботай":
        bot.send_message(message.chat.id, "или умри")



@bot.message_handler(content_types=['new_chat_member'])
def on_user_joins(message):
    bot.send_sticker(message.chat.id, sup, reply_to_message_id=message.message_id)

bot.polling(none_stop=True, interval=0)
