from flask import Flask, render_template,request
# from firebase import Firebase

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired




from flask_nav import Nav
from flask_nav.elements import Navbar,Subgroup, View, Link, Text, Separator

app = Flask(__name__)
nav = Nav(app)
# Config = {
#   apiKey: "AIzaSyBvMBbXcJGyptkPjVu_c6s1obmA97SXEOE",
#   authDomain: "huzzahplay.firebaseapp.com",
#   databaseURL: "https://huzzahplay.firebaseio.com",
#   projectId: "huzzahplay",
#   storageBucket: "huzzahplay.appspot.com",
#   messagingSenderId: "843161759149",
#   appId: "1:843161759149:web:60cdd3bb2df7ababffc524",
#   measurementId: "G-63902Y2BQB"
# };

# firebase = Firebase(config)





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
    # auth = firebase.auth()
    user = ''


    if(request.method == "POST"):


        if request.form['action'] == "login":
            uname = request.form['uname']
            psw = request.form['psw']

            print(uname)
            print(psw)
            # user = auth.sign_in_with_email_and_password(uname, psw)
            return dash()
        elif request.form['action'] == "forgot":
            return render_template('login.html')


    return render_template('index.html')

@app.route('/dash', methods = ['GET','POST'])
def dash():
    name = ''
    date = ''
    time = ''
    session = ''
    print("dash")



    slist = ['session1','session2', 'session3','session4', 'session5','session6', 'session7','session8']
    slen = len(slist)

    if (request.method == "POST"):
        print("in posted")
        print(request.form['action'])

        if(request.form['action'] == 'create'):
            name = request.form['name']
            date = request.form['date']
            time = request.form['time']

            print(name)
            print(date)
            print(time)
            return render_template('dash.html',slist = slist, slen =slen)

    return render_template('dash.html',slist = slist, slen = slen)

@app.route('/session/<session>')
def session(session):
        #get all student sessions
    students = ['James & Kevin','Angie & Kate','Martin & Elvin', 'Camila & Sarah']
    stlen = len(students)

    return render_template('student.html', students = students, stlen= stlen, session = session)

@app.route('/individual/<session>/<individual>')
def individual(session, individual):
    #get individual sessions
    names = ["James","Kevin"]
    story1 = ["When I go to the arcade with my best friend, there are lots of games to play.","In the game, X-Men you can be a different super heros.","You also need to save people."]
    story2 = ["I spend lots of time there with my friends.","The point of the game is to beat every robot.","Then you can go to the next level."]
    storylen = len(story1)


    return render_template('individual.html', story1 = story1,story2 = story2, storylen= storylen, session = session, names=names, individual= individual)



@app.route('/items/<item>')
def item(item):
    return'<h1> The ITEM PAGE!!! the item is: {}.'.format(item)

if __name__ == '__main__':
    app.run(debug=True)