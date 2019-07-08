#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
