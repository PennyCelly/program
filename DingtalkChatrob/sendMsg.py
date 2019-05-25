# coding=gbk
from dingtalkchatbot.chatbot import DingtalkChatbot
# WebHook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=bb40264ec71a993915182f1efff35f47b1ae65ea543d501e7637a7b87123dcf8'
# 初始化机器人小丁
xiaoding = DingtalkChatbot(webhook)
# Text消息@所有人
# xiaoding.send_text(msg='打这么多局，不睡觉吗', is_at_all=True)
# Text消息之@指定用户
at_mobiles = ['15951907321',             # 达达
              # '18936039173',             # 大杰哥
              # '18013828063',             # 狗子哥
              # '13770713366',             # 奶爸
              # '18351953113'              # 春春
              ]
xiaoding.send_text(msg='还等什么呢', at_mobiles=at_mobiles)

