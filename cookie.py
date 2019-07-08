#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def set_cookie():
    '''设置cookie,并响应'''
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'tom', max_age=3600)
    return resp


# 获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp


# 删除cookie
@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('hello world')
    response.delete_cookie('username')
    return response


if __name__ == '__main__':
    app.run()
