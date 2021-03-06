import os
from flask import Flask, request
import telepot
from pprint import pprint
try:
    from Queue import Queue
except ImportError:
    from queue import Queue

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '357359911:AAHxnKF-bXuVQKUVxsaV_FTqXSJg8AkbFDE' # put your token in heroku app as environment variable
SECRET = '/bot' + TOKEN
URL = 'https://mobibotassistant.herokuapp.com/' #  paste the url of your application

UPDATE_QUEUE = Queue()
BOT = telepot.Bot(TOKEN)


technoconf = -1001070076534
me = 94026383
TA= -1001109363260

def on_chat_message(msg):
    pprint(msg)
    content_type, chat_type, chat_id= telepot.glance(msg)
    pprint (content_type)
    pprint (chat_type)
    pprint (chat_id)
    if content_type == 'text' and ('text' in msg) == 'Ассистент, тест':
        BOT.sendMessage(chat_id, 'TESTED')
    if 'forward_from_chat' in msg:
        forwared = msg['forward_from_chat']['id']
        if (forwared == TA) and not (chat_type=='private'):
            Admins = BOT.getChatAdministrators(chat_id)
            message_id = msg['message_id']
            Name = msg['from']['first_name']
            Uname = msg['from']['username']
            from_id = msg['from']['id']
            chat_username=msg['chat']['username']
            for i in range(len(Admins)):
                if 'id' in Admins[i]['user'] != from_id:
                    BOT.kickChatMember('@'+chat_username,from_id)
                    BOT.sendMessage(chat_id,Name+' (@'+Uname+') '+ 'BANNED!')
                    BOT.forwardMessage(me,chat_id,message_id)
                    BOT.sendMessage(me, Name + ' (@' + Uname + ') ' + 'id: #' + str(from_id) + ' BANNED!')
                else:
                    BOT.sendMessage(chat_id, 'SPAM!')


BOT.message_loop({'chat': on_chat_message}, source=UPDATE_QUEUE)  # take updates from queue

@app.route(SECRET, methods=['GET', 'POST'])
def pass_update():
    UPDATE_QUEUE.put(request.data)  # pass update to bot
    return 'OK'

#BOT.setWebhook() # unset if was set previously
#BOT.setWebhook(URL + SECRET)
