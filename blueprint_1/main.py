# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 14:27

from flask import Flask
from orders import add_orders
from goods import add_goods

app = Flask(__name__)
app.register_blueprint(add_orders)
app.register_blueprint(add_goods)


@app.route('/')
def index():
    return "index page"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
