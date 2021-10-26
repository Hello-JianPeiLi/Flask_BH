# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 15:11
from flask import Flask
from cart import app_cart

app = Flask(__name__)
app.register_blueprint(app_cart, url_prefix='/cart')


@app.route('/')
def index():
    return 'index page'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
