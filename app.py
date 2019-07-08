from flask import Flask, Blueprint
from goods import goods

app = Flask(__name__)
user_bp = Blueprint('user', __name__)
app.register_blueprint(user_bp)
app.register_blueprint(goods)


@user_bp.route('/user')
def user_profile():
    return 'user_profile'


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
