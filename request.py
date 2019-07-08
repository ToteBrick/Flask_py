#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


# /user?name=Tom&age=18 字符串参数
@app.route('/user')
def user_profile():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'name is {},age is {}.'.format(name, age)

# 上传图片
@app.route('/upload/', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.jpg')
    return 'upload ok'


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
