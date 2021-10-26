# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/26 15:11
from flask import Blueprint

app_cart = Blueprint('app_cart', __name__, template_folder='templates', static_folder='static')
# 全局的templates和static的最高级，如果同文件，优先渲染工程下最外层的templates和static

from . import view
