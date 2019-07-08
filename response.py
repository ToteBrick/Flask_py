#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    mstr = 'aaaaaa'
    mint = 10
    return render_template('index.html', my_str=mstr, my_int=mint)


from flask import redirect, url_for


@app.route('/demo2')
def demo2():
    return redirect(url_for('index'))  # 跳转首页


from flask import jsonify


@app.route('/demo3')
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    return jsonify(json_dict)


'''
响应可以返回一个元组，这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。
status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
'''


@app.route('/demo4')
def demo4():
    return '状态码为 200', 200, {'name': 'Python'}


@app.route('/demo5')
def demo5():
    resp = make_response('make response测试')
    resp.headers['Header'] = 'it is a test header'
    resp.status = '405 not allow'
    return resp


if __name__ == '__main__':
    app.run()
