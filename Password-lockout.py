import time

import mysql.connector

passwd=['Nooun90']

from flask import Flask, render_template, session, url_for, redirect, request, sessions, abort
import uuid, datetime
import _mysql_connector
from flask_mysqldb import MySQL
import MySQLdb.cursors

app=Flask(__name__)

app.secret_key='Crazy_Willy_Jones'

failed_attempts=[]

app.config['temp']= datetime.timedelta(days=1)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'ihatenyp1234'
#app.config['MYSQL_DB'] = 'pythonlogin'
#app.config['MYSQL_PORT'] = 3306
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"
#mysql = MySQL(app)

mydb=mysql.connector.Connect(
    host='localhost',
    user='root',
    password='ihatenyp1234',
    database='pythonlogin'
)
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
        a = len(failed_attempts)
        log(session['temp'],password,username,a)
    if a>=5:
        return error(a)
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")
def log(sesh,p,u,a):
    tries = "." + str(a)
    sesh_id=str(sesh)
    user=str(u)
    pasw=str(p)
    f = open("logfile.txt", "a")
    f.write('failed attempt'+' '+str(sesh)+" "+"username"+" "+str(u)+" "+"password"+" "+str(p))
    f.write("\n")
    f.close()
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO tests VALUES(%s,%s,%s)",(sesh_id+tries,user,pasw,))
    mydb.commit()
    count()

def count():
    f = open("logfile.txt","r")
    Lines=f.readlines()
    f.close()

def error(a):
    if a != 0:
        return render_template('error.html')
    time.sleep(a)
    a=0
    return render_template("login.html")

if __name__ == '__main__':
    app.run()
