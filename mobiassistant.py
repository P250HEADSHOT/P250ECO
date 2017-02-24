# -*- coding: utf-8 -*-
# continuous-integration

import telepot
import time
from pprint import pprint
technoconf = -1001070076534
me = 94026383
TA= -1001109363260
token = "357359911:AAHxnKF-bXuVQKUVxsaV_FTqXSJg8AkbFDE"
bot = telepot.Bot(token)

def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    if 'forward_from_chat' in msg:
        forwared = msg['forward_from_chat']['id']
        if (forwared == TA):
            Admins = bot.getChatAdministrators(chat_id)
            message_id = msg['message_id']
            Name = msg['from']['first_name']
            Uname = msg['from']['username']
            from_id = msg['from']['id']
            chat_username=msg['chat']['username']
            for i in range(len(Admins)):
                if 'id' in Admins[i]['user'] != from_id:
                    bot.kickChatMember(str('@')+chat_username,from_id)
                    bot.sendMessage(chat_id,Name+str(' (@')+Uname+str(') ')+ str('BANNED!'))
                    bot.forwardMessage(me,chat_id,message_id)
                    bot.sendMessage(me, Name + str(' (@') + Uname + str(') ') + str('id: #') + str(from_id) + str(
                        ' BANNED!'))
                else:
                    bot.sendMessage(chat_id, str('SPAM!'))
    if 'text' in msg=='тест':
        bot.sendMessage(me, str('TESTED'))
bot.message_loop(handle)






while 1:
    time.sleep(10)
