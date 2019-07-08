#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
一、session的设置
二、flask的session存放的位置（flask将session放在cookie中，flask中的session为浏览器session）
    可以引用flask-session指定session的储存位置
三、需求：如何删除session和设置session的有效时间, 以及session默认存储时间？？？
    flask默认存储时间：当浏览器关闭。 （31天，需要依赖于开启配置）

"""
from flask import Flask, session

app = Flask(__name__)


class DefautConfig(object):
    SECRET_KEY = 'WGH345SASVB'


app.config.from_object(DefautConfig)


@app.route('/')
def index():
    # 设置session,设置前必须配置密钥，且flask中session存在与浏览器中
    session['user'] = 'laowang'
    return 'session set ok'


@app.route('/get')
def get_session():
    # 获取session
    username = session.get('user', None)
    return 'username is {}.'.format(username)


# 设置session的有效期
@app.route("/session")
def set_session_time():
    session['name'] = 'zhangsan'
    session.permanent = True
    # 指定session的过期时间
    app.permanent_session_lifetime = 86400
    return "ok"


# 删除session
@app.route('/delete')
def del_session():
    session.pop("user", None)
    return "delete session ok."


if __name__ == "__main__":
    app.run(debug=True)
