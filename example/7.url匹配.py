from flask import Flask
from werkzeug.routing import BaseConverter


class Regex_url(BaseConverter):
    def __init__(self, url_map, *args):
        super(Regex_url, self).__init__(url_map)
        self.regex = args[0]


app = Flask(__name__)
app.url_map.converters['re'] = Regex_url

# 匹配3到5个字母
@app.route('/user/<re("[a-z]{3,5}"):id>')
def hello(id):
    return 'hello %s' % id


if __name__ == '__main__':
    app.run()
