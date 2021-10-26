# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 15:14
from . import app_cart
from flask import render_template


@app_cart.route('/get_cart')
def get_cart():
    return render_template('cart.html')
