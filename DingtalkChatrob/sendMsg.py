# coding=gbk
from dingtalkchatbot.chatbot import DingtalkChatbot
# WebHook��ַ
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=bb40264ec71a993915182f1efff35f47b1ae65ea543d501e7637a7b87123dcf8'
# ��ʼ��������С��
xiaoding = DingtalkChatbot(webhook)
# Text��Ϣ@������
# xiaoding.send_text(msg='����ô��֣���˯����', is_at_all=True)
# Text��Ϣ֮@ָ���û�
at_mobiles = ['15951907321',             # ���
              # '18936039173',             # ��ܸ�
              # '18013828063',             # ���Ӹ�
              # '13770713366',             # �̰�
              # '18351953113'              # ����
              ]
xiaoding.send_text(msg='����ʲô��', at_mobiles=at_mobiles)

