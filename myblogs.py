#-*- coding=utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    name="Hello, Word! I'm coming"
    return name

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/520/<username>')
def goo(username):
    return 'I love you {}'.format(username)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

