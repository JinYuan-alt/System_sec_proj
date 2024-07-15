import time

passwd=['Nooun90']

from flask import Flask, render_template, session, url_for, redirect, request, sessions, abort
import uuid, datetime

app=Flask(__name__)

app.secret_key='Crazy_Willy_Jones'

failed_attempts=[]

app.config['temp']= datetime.timedelta(days=1)

@app.route("/")
def first():
    myuuid = str(uuid.uuid4())
    session['temp'] = "temp" + myuuid
    return render_template("login.html")

@app.route("/",methods=['GET',"POST"])
def login():
    password = request.form.get("password")
    username = request.form.get("username")
    if password == passwd[0]:
        session.pop('temp', None)
        perma=str(uuid.uuid4())
        session['temp']=username+password+perma
        return render_template("home.html", sesh_id=session['temp'])
    if password!=passwd[0]:
        failed_attempts.append('failed')
        print(failed_attempts)
        if len(failed_attempts)>3:
            return render_template('error.html')
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
