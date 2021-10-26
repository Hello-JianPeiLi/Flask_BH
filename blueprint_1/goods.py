# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 14:37
from flask import Blueprint

add_goods = Blueprint('add_goods', __name__)


@add_goods.route('/get_goods')
def goods():
    return 'goods page'
