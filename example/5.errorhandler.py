from flask import Flask,abort
app = Flask(__name__)
@app.route('/')
def hello():
    abort(404) # abort函数被触发，其后面的语句将不会执行。其类似于python中raise
    return 'hello',666


if __name__ == '__main__':
    app.run()