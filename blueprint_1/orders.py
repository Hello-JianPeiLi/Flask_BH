# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 14:27

from flask import Blueprint

add_orders = Blueprint('add_orders', __name__)


@add_orders.route('/get_orders')
def orders():
    return 'orders page'
