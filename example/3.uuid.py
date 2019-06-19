import uuid

from flask import Flask

app = Flask(__name__)


@app.route('/getuuid/')
def get_uuid():
    return str(uuid.uuid4())


@app.route('/useuuid/<uuid:name>/')
def use_uuid(name):
    print(name)
    return '获取到了uuid'


if __name__ == '__main__':
    app.run()
