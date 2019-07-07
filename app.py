from flask import Flask, Blueprint

app = Flask(__name__)
user_bp = Blueprint('user', __name__)
app.register_blueprint(user_bp)


@user_bp.route('/user')
def user_profile():
    return 'user_profile'


@app.route('/')
def index():
    return 'index'
