from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'


@app.route('/user/<username>/')
def user(username, age=20):
    return username + ''


if __name__ == '__main__':
    app.run()
