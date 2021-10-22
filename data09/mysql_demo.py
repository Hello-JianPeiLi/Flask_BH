# -*- coding:utf-8 -*-
# Author: JianPei
# @Time : 2021/10/21 09:33
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
db = SQLAlchemy(app)


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/flask"

    # 设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)


class Role(db.Model):
    """角色身份表"""
    __tablename__ = "tbl_roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

    users = db.relationship("User", backref="tbl_roles")

    def __repr__(self):
        return "Role table:%s" % self.name


class User(db.Model):
    """用户表"""
    __tablename__ = "tbl_users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        return "User table:%s" % self.name


if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    # ro1 = Role(name="admin")
    # ro2 = Role(name="user")
    # db.session.add_all([ro1, ro2])
    # db.session.commit()
    # us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    # us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    # us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    # us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    # db.session.add_all([us1, us2, us3, us4])
    # db.session.commit()
    app.run(debug=True)
