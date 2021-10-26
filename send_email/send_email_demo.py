# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/25 17:25
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)


class Config(object):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '发送方Email'
    MAIL_PASSWORD = 'qq邮箱smtp授权码'


app.config.from_object(Config)

mail = Mail(app)


@app.route('/test')
def index2():
    return "test success"


@app.route('/send_email')
def index():
    # sender 发送方，recipients 接收方列表
    msg = Message("THIS IS A TEST", sender='发送方邮件', recipients=['接收方email'])
    # 邮件内容
    msg.body = "Flask test mail"
    # 发送邮件
    mail.send(msg)
    print("发送成功")
    return "send succeed"


if __name__ == '__main__':
    app.run()
