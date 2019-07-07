from flask import Flask


class DefaultConfig(object):
    '''默认配置'''
    SECRET_KEY = 'sdfghjhgfdsfghjhgfdfgeghg'


# app = Flask(__name__)
app = Flask(__name__, static_url_path='/s', static_folder='static')  # 静态目录默认static
# 设置
app.config.from_object(DefaultConfig)  # 从类对象读
app.config.from_pyfile('setting.py')  # 从文件读
# 设置环境变量需要从项目根路径设置，环境变量是一个临时的系统变量
app.config.from_envvar('PROJECT_SETIING', silent=True)  # 从环境变量读,silent=True表示有错安静处理，不报错，默认False


@app.route('/')
def index():
    # 读取配置
    print(app.config['SECRET_KEY'])
    print(app.config['SECRET_KEY2'])
    print(app.config['NAME'])
    return 'hello, world'
