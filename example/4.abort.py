from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def hello():
    abort(404)  # abort函数被触发，其后面的语句将不会执行。其类似于python中raise
    return 'hello', 666

# 异常处理
@app.errorhandler(404)
def error(e):
    return '您请求的页面不存在了，请确认后再次访问！%s' % e


if __name__ == '__main__':
    app.run()
