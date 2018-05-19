#-*- coding=utf-8 -*-
from flask import render_template,request
from models import *

app = Flask(__name__)

#remove
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL","postgresql://postgres:test2018@localhost/lecture3") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

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

@app.route('/education/')
def education():
    flights=Flight.query.all()
    return render_template("flights.html",flights=flights)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

