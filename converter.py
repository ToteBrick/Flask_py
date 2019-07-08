#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.routing import BaseConverter
from flask import Flask

'''
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
'''
app = Flask(__name__)


@app.route('/user/<int:user_id>')  # 指定类型
def user(user_id):
    print(type(user_id))
    return 'user id is {}'.format(user_id)


# 自定义转换器
class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


# 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: mobile
app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_codes/<mobile:mob_num>')
def send_sms_code(mob_num):
    return 'send sms code to {}'.format(mob_num)


if __name__ == '__main__':
    app.run()
