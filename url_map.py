import json


from flask import Flask

app = Flask(__name__, static_url_path='/s', static_folder='static')  # 静态目录默认static


@app.route('/a')
def a():
    return a


@app.route('/b')
def b():
    return b


@app.route('/')
def index():
    # rules_iterator = app.url_map.iter_rules()
    rules_iterator = app.url_map.iter_rules(endpoint='a')  # 遍历时指定特定路由视图函数
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})  # 遍历所有路由
    # return json.dumps(
    #     {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ['index', 'static']})  # 排除首页及路由
