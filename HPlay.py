from flask import Flask, render_template,request

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

from pyrebase4 import *



from flask_nav import Nav
from flask_nav.elements import Navbar,Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)
config = {
  apiKey: "AIzaSyBvMBbXcJGyptkPjVu_c6s1obmA97SXEOE",
  authDomain: "huzzahplay.firebaseapp.com",
  databaseURL: "https://huzzahplay.firebaseio.com",
  projectId: "huzzahplay",
  storageBucket: "huzzahplay.appspot.com",
  messagingSenderId: "843161759149",
  appId: "1:843161759149:web:60cdd3bb2df7ababffc524",
  measurementId: "G-63902Y2BQB"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


nav.register_element('my_navbar', Navbar('thenav',
    Text('HazzahPlay'),
    Separator(),
    View('Home', 'index'),
    Separator(),
    View('Item One', 'item', item = 1),
    Separator(),
    View('Item two', 'item', item = 2),
    Separator(),
    Link('Google Classroom', 'https://www.google.com'),
    ))

@app.route('/',methods= ['GET','POST'])
def index():
    uname = ''
    psw = ''


    if(request.method == "POST"):

        if request.form['action'] == "login":
            uname = request.form['uname']
            psw = request.form['psw']

            print(uname)
            print(psw)
            user = auth.sign_in_with_email_and_password(email, password)
            print(user)
            return render_template('dash.html')
        elif request.form['action'] == "forgot":
            return render_template('login.html')


    return render_template('index.html')
@app.route('/dash', methods = ['GET','POST'])
def dash():
    name = ''
    date = ''
    time = ''
    if (request.method == "POST"):
        print("in posted")
        if(request.form['action'] == 'create'):
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']

            print(name)
            print(date)
            print(time)
            return render_template('dash.html')
    return render_template('dash.html')





@app.route('/items/<item>')
def item(item):
    return'<h1> The ITEM PAGE!!! the item is: {}.'.format(item)

if __name__ == '__main__':
    app.run(debug=True)