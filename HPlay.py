from flask import Flask, render_template,request

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired




from flask_nav import Nav
from flask_nav.elements import Navbar,Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)





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
            return dash()
        elif request.form['action'] == "forgot":
            return render_template('login.html')


    return render_template('index.html')
@app.route('/dash', methods = ['GET','POST'])
def dash():
    name = ''
    date = ''
    time = ''

    slist = ['testing','adding', 'cards','dfa', 'testing','adding', 'cards','dfa']
    slen = len(slist)

    if (request.method == "POST"):
        print("in posted")
        if(request.form['action'] == 'create'):
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']

            print(name)
            print(date)
            print(time)
            return render_template('dash.html',slist = slist, slen =slen)
    return render_template('dash.html',slist = slist, slen = slen)





@app.route('/items/<item>')
def item(item):
    return'<h1> The ITEM PAGE!!! the item is: {}.'.format(item)

if __name__ == '__main__':
    app.run(debug=True)