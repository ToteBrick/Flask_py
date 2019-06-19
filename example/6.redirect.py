from flask import Flask, abort,redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('https://www.baidu.com')

# 异常处理
@app.errorhandler(404)
def error(e):
    return '您请求的页面不存在了，请确认后再次访问！%s' % e


if __name__ == '__main__':
    app.run()
