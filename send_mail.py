# -*- coding: UTF-8 -*-
# @Author   : xiaoyan
# @Date    : 2020/9/10
# @File     : send_mail
# @SoftWare : PyCharm
import os
# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':
    # send_mail('来自明爸爸的邮件问候', '访问www.baidu.com，有爸爸送你的惊喜', '284023242@qq.com', ['408697356@qq.com'],)
    subject, from_email, to = '来自明爸爸的再次问候', '284023242@qq.com', '408697356@qq.com'
    text_content = '访问www.baidu.com了没，逆子'
    html_content = '<p>访问<a href="www.baidu.com" target=blank>www.baidu.com</a>呀，逆子</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()