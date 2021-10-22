# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/11 09:48

from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    print('这是主页')
    return '这是主页'


@app.route('/login')
def login():
    print('这是登录页面')
    return '这是登录页面'


@app.before_first_request
def before_first_request():
    """只有服务器第一次请求触发"""
    print('---before_first_request')


@app.before_request
def before_request():
    """请求前触发"""
    print('---before_request')


@app.after_request
def after_handle_request(response):
    """视图结束后触发，若有异常，则不会触发"""
    print('---after_handle_request')
    return response


@app.teardown_request
def teardown_request(response):
    """请求结束后触发"""
    print('---teardown_request')
    return response


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, port=7890)
