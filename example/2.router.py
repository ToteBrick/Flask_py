from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/user/<username>/')
def user(username, age=20):
    return username + ''

@app.route('/usepath/<path:name>/', methods=['GET', 'POST'])
def use_path(name):
    return str(name)


if __name__ == '__main__':
    app.run()
