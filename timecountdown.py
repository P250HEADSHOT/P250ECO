# -*- coding: utf-8 -*-
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
import datetime
import pytz

technoconf = -1001070076534
me = 94026383
sup = "BQADAgADrQEAAm29TQUoveU--qPBlAI"
token = "162565626:AAEF7fXQpxpZkjD1aFGhGkznVvoWE8-e8_Q"
bot = telebot.TeleBot(token)

FMT="%d.%m.%Y %H:%M"
rus = datetime.datetime.strptime("09.06.2017 10:00", FMT)
math = datetime.datetime.strptime("02.06.2017 10:00", FMT)
phys = datetime.datetime.strptime("07.06.2017 10:00", FMT)
it = datetime.datetime.strptime("29.05.2017 10:00", FMT)
#tz = pytz.timezone("Europe/Moscow")
# print('Русский через',c)
# bot.send_message(technoconf, "Русский через")
# bot.send_message(technoconf, drus)

@bot.message_handler(commands=['rus'])
def handle_text(message):
    now = datetime.datetime.now()
    drus = rus - now
    bot.send_message(message.chat.id, "До Русича осталось {} дней, {} часов {} минут {} секунд.".format(drus.days, drus.seconds//3600, drus.seconds%3600//60, drus.seconds%60)
, reply_to_message_id=message.message_id)


@bot.message_handler(commands=['math'])
def handle_text(message):
    now = datetime.datetime.now()
    dmath = math - now
    bot.send_message(message.chat.id, "До Матеши осталось {} дней, {} часов {} минут {} секунд.".format(dmath.days, dmath.seconds//3600, dmath.seconds%3600//60, dmath.seconds%60), reply_to_message_id=message.message_id)


@bot.message_handler(commands=['phys'])
def handle_text(message):
    now = datetime.datetime.now()
    dphys = phys - now
    bot.send_message(message.chat.id, "До Физона осталось {} дней, {} часов {} минут {} секунд.".format(dphys.days, dphys.seconds//3600, dphys.seconds%3600//60, dphys.seconds%60), reply_to_message_id=message.message_id)


@bot.message_handler(commands=['ikt'])
def handle_text(message):
    now = datetime.datetime.now()
    dit = it - now
    bot.send_message(message.chat.id, "До ИКТ осталось {} дней, {} часов {} минут {} секунд.".format(dit.days, dit.seconds//3600, dit.seconds%3600//60, dit.seconds%60), reply_to_message_id=message.message_id)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if ("скока до русича" in str.lower(message.text)) or  ("cкока до русского" in str.lower(message.text)) or ("cколько до русича" in str.lower(message.text)) or ("cколько до русского" in str.lower(message.text)):
        now = datetime.datetime.now()
        drus = rus - now
        bot.send_message(message.chat.id, "До Русича осталось {} дней, {} часов {} минут {} секунд.".format(drus.days, drus.seconds//3600, drus.seconds%3600//60, drus.seconds%60)
, reply_to_message_id=message.message_id)
    if ("cкока до матеши" in str.lower(message.text)) or ("сколько до матеши" in str.lower(message.text)) or ("скока до математики" in str.lower(message.text)) or ("сколько до математики" in str.lower(message.text)):
        now = datetime.datetime.now()
        dmath = math - now
        bot.send_message(message.chat.id, "До Матеши осталось {} дней, {} часов {} минут {} секунд.".format(dmath.days, dmath.seconds//3600, dmath.seconds%3600//60, dmath.seconds%60), reply_to_message_id=message.message_id)
    if ("скока до физеки" in str.lower(message.text)) or ("сколько до физеки" in str.lower(message.text)) or ("скока до физеки" in str.lower(message.text)):
        now = datetime.datetime.now()
        dphys = phys - now
        bot.send_message(message.chat.id, "До Физона осталось {} дней, {} часов {} минут {} секунд.".format(dphys.days, dphys.seconds//3600, dphys.seconds%3600//60, dphys.seconds%60), reply_to_message_id=message.message_id)
    if ("скока до икт" in str.lower(message.text)) or ("сколько до икт" in str.lower(message.text)):
        now = datetime.datetime.now()
        dit = it - now
        bot.send_message(message.chat.id, "До ИКТ осталось {} дней, {} часов {} минут {} секунд.".format(dit.days, dit.seconds//3600, dit.seconds%3600//60, dit.seconds%60), reply_to_message_id=message.message_id)
    if "люблю тебя" in str.lower(message.text):
        bot.send_message(message.chat.id, "Мур <3", reply_to_message_id=message.message_id)
    if message.text == "Скока до сессии?":
        bot.send_message(message.chat.id, "Неделя", reply_to_message_id=message.message_id)
    if message.text == "Скажи физика круто":
        bot.send_message(message.chat.id, "физика круто", reply_to_message_id=message.message_id)
    if "ботай" in str.lower(message.text):
        bot.send_message(message.chat.id, "или умри")
    if message.text == "Андрей":
        bot.send_message(message.chat.id, "расскажи как ты стал джуном")
    if str.lower(message.text) == "пинг":
        bot.send_message(message.chat.id, "понг")
    if message.text == "combot.org/chat/-1001070076534":
        bot.send_message(message.chat.id, "Статистика сообщений конференции")    



@bot.message_handler(content_types=['new_chat_member'])
def on_user_joins(message):
    bot.send_sticker(message.chat.id, sup, reply_to_message_id=message.message_id)

bot.polling(none_stop=True, interval=0)
