#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
一、上下文：
    1、请求上下文：
        request: 封装了HTTP请求的内容，针对的是http请求。可以通过他获取整个请求中的请求报文信息
        session: 用来记录请求会话中的信息，针对的是用户信息。

    2、应用上下文：
        current_app:
            1、在多文件操作时，想在别的文件中使用app, 一般不直接导入，而是使用current_app代表app。
            2、它本身是一个代理，werkzeug.local.LocalProxy，是app代理人

        g对象:
            1、一个临时变量，充当中间媒介的作用，我们可以通过它在一次请求调用的多个函数间传递一些数据。每次请求都会重设这个变量。

三、上下文原理：
    问题：当并发2个请求到
        /articles/articles?channel_id=123
        /articles/articles?channel_id=124

四、上下文的生命周期：
    1、request:生命周期为一次请求期间，当请求处理完成后，生命周期也就完结了
    2、session: 如果没设置过期时间，那么浏览器关闭失效，否则，过期时间失效。
    3、current_app: 生命周期最长，只要当前程序实例还在运行，都不会失效.
    4、g对象:生命周期为一次请求期间，当请求处理完成后，生命周期也就完结了

五、区别是什么：
    1、请求上下文：保存了客户端和服务器交互的数据
    2、应用上下文：flask 应用程序运行过程中，保存的一些配置信息，比如说程序名，数据库连接，应用信息等。

"""

from flask import Flask, request, current_app, g

app = Flask(__name__)


class Config(object):
    SECRET_KEY = "123dfghjk45hytr6"


app.config.from_object(Config)
# 动态添加属性
app.redis = "123"


# current_app的使用
@app.route("/")
def index():
    print(current_app.redis)
    print(current_app.config["SECRET_KEY"])
    return "index"


@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    return 'you wanna get articles of channel {}'.format(channel_id)


# g对象的使用
def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id={} user_name={}'.format(user_id, user_name))


@app.route('/')
def get_user_profile():
    g.user_id = 2
    g.user_name = 'laowang'
    db_query()
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)