# coding=gbk
from dingtalkchatbot.chatbot import DingtalkChatbot
# WebHook��ַ
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=bb40264ec71a993915182f1efff35f47b1ae65ea543d501e7637a7b87123dcf8'
# ��ʼ��������С��
xiaoding = DingtalkChatbot(webhook)
xiaoding.send_link(title='����û�뵽��ĳСda��Ȼ...',
                   text='�����������ӵ�...',
                   message_url='http://t.cn/E6107Jl?m=4359980473344586&u=5886546337", '
                               'pic_url="https://tvax4.sinaimg.cn/crop.273.161.1532.1532.180/006qnlBLly8fgjmxyq16gj31kw1hj7cv.jpg')
