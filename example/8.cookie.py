from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def set_cookie():
    '''设置cookie,并响应'''
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'simon')
    return resp


# 获取cookie
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp


if __name__ == '__main__':
    app.run()
