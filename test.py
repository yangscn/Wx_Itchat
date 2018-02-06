#coding=utf8

import itchat
import time 
from itchat.content import *
import requests
import json

def  getTulingmsg(info):
    appkey='e3c6f9d7746b42f5963df78ed1a4d585'
    tl_url='http://www.tuling123.com/openapi/api?key=%s&info=%s' % (appkey,info)
    req = requests.get(tl_url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

def get_groupID(name):
    gi = itchat.search_chatrooms(name=name)
    return gi[0]['UserName']


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    item = get_groupID(u'101办公室')
    if msg['ToUserName'] == item or msg['FromUserName']==item:
        print(msg.text)
        itchat.send(u'%s' % getTulingmsg(msg['Text']),toUserName=item)

@itchat.msg_register(TEXT)
def text_reply(msg):
    item = 'filehelper'
    if msg['ToUserName'] == item:
        print(msg.text)
        itchat.send(u'%s' % getTulingmsg(msg['Text']),toUserName=item)


# itchat.auto_login(True)
# itchat.run(True)
print(itchat.check_login())
itchat.auto_login(hotReload=True)

itchat.run(debug=False,blockThread=True)

