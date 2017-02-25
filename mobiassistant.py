import os
from flask import Flask, request
import telepot

try:
    from Queue import Queue
except ImportError:
    from queue import Queue

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '357359911:AAHxnKF-bXuVQKUVxsaV_FTqXSJg8AkbFDE' # put your token in heroku app as environment variable
SECRET = '/bot' + TOKEN
URL = 'https://mobiassistantbot.herokuapp.com/' #  paste the url of your application

UPDATE_QUEUE = Queue()
BOT = telepot.Bot(TOKEN)

from pprint import pprint
technoconf = -1001070076534
me = 94026383
TA= -1001109363260

def on_chat_message(msg):
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
                    bot.sendMessage(me, Name + str(' (@') + Uname + str(') ') + str('id: #') + str(from_id) + str(' BANNED!'))
                else:
                    bot.sendMessage(chat_id, str('SPAM!'))
    if 'text' in msg=='тест':
        bot.sendMessage(me, str('TESTED'))

BOT.message_loop({'chat': on_chat_message}, source=UPDATE_QUEUE)  # take updates from queue

@app.route(SECRET, methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'

#BOT.setWebhook() # unset if was set previously
#BOT.setWebhook(URL + SECRET)
