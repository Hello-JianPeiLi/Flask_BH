# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/11 11:30

from flask import Flask,abort

app = Flask(__name__)


@app.route('/index')
def index():
    return 'index'

def item():
    return abort(404)