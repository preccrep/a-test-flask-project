from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dp = SQLAlchemy(app)

@app.route('/hello')
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

name = 'preccrep'
movies = [
{'title': 'My Neighbor Totoro', 'year': '1988'},
{'title': 'Dead Poets Society', 'year': '1989'},
{'title': 'A Perfect World', 'year': '1993'},
{'title': 'Leon', 'year': '1994'},
{'title': 'Mahjong', 'year': '1996'},
{'title': 'Swallowtail Butterfly', 'year': '1996'},
{'title': 'King of Comedy', 'year': '1999'},
{'title': 'Devils on the Doorstep', 'year': '1999'},
{'title': 'WALL-E', 'year': '2008'},
{'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)


import os
import sys

WIN = sys.platform.startswith('win')
# if WIN:
#     prefix = 'sqlite:///'
# else:
#     prefix = 'sqlite:////'
prefix = 'sqlite:///'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

import click

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """
    initialize the database
    :param drop: the input option
    :return: a prompting message
    """
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialize the database.')

