from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    mydict = {'key': 'silence is gold'}
    mylist = ['Speech', 'is', 'silver']
    myintvar = 0

    return render_template('index.html',
                           mydict=mydict,
                           mylist=mylist,
                           myintvar=myintvar
                           )


if __name__ == '__main__':
    app.run(debug=True)
