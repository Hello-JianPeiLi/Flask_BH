# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/12 17:37
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SDFLKSJGLSDGJLSD'


@app.route('/index')
def index():
    return render_template('flask_dd.html', name='PYTHON')


if __name__ == '__main__':
    app.run(debug=True, port=6677)
