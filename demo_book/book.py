# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/22 10:01
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

pymysql.install_as_MySQLdb()
app = Flask(__name__)
db = SQLAlchemy(app)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = r"mysql://root:123456@127.0.0.1:3306/flask"
    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 秘钥
    SECRET_KEY = "SLKDFGJLWIEORF"


app.config.from_object(Config)


class Author(db.Model):
    """作者"""
    __tablename__ = 'tbl_authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship('Book', backref='author')


class Book(db.Model):
    """书籍"""
    __tablename__ = 'tbl_books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('tbl_authors.id'))


class AuthorBookForm(FlaskForm):
    """作者表单模型"""
    author_name = StringField(label="作者", validators=[DataRequired("请输入作者")])
    book_name = StringField(label="书籍", validators=[DataRequired("请输入数据")])
    submit = SubmitField(label="保存")


@app.route('/', methods=['POST', 'GET'])
def index():
    # 创建表单对象
    form = AuthorBookForm()
    if request.method == 'post':
        if form.validate_on_submit():
            # 验证表单成功
            author_name = form.author_name.data
            book_name = form.book_name.data
            # print(author_name)
            # 保存数据库
            author = Author(name=author_name)
            print(author.name)
            print(author.id)
            db.session.add(author)
            db.session.commit()

            book = Book(name=book_name, author_id=author.id)
            # book = Book(name=book_name, author=author)
            db.session.add(book)
            db.session.commit()
    # 查询数据库
    authors = Author.query.all()
    return render_template('index.html', authors=authors, form=form)


@app.route('/delete_book', methods=['POST'])
def delete_book():
    """删除图书"""
    req_data = request.get_json()
    book_id = req_data.get('book_id')
    print(req_data)

    # 业务处理
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"code": 1, "msg": "删除成功"})


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # # 生成数据
    # au_xi = Author(name='我吃西红柿')
    # au_qian = Author(name='萧潜')
    # au_san = Author(name='唐家三少')
    # db.session.add_all([au_xi, au_qian, au_san])
    # db.session.commit()
    # bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
    # bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
    # bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
    # bk_san = Book(name='冰火魔厨', author_id=au_san.id)
    # # 把数据提交给用户会话
    # db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
    # # 提交会话
    # db.session.commit()
    app.run(debug=True)
