from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def url_test_for():
    print(url_for('hello'))
    print(url_for('user_page', name='preccrep'))
    print(url_for('user_page', name='vigohack'))
    print(url_for('url_test_for'))
    print(url_for('url_test_for', num=2))
    return 'test_page'


