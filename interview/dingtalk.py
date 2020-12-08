from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings

def send(message, at_mobiles=[]):
    # 引用 settings里面配置的钉钉群消息通知的WebHook地址:
    webhook = settings.DINGTALK_WEB_HOOK

    # 初始化机器人小丁, # 方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook)

    # Text消息@所有人
    xiaoding.send_text(msg=('面试通知: %s' % message), at_mobiles = at_mobiles )