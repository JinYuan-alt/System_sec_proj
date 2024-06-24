passwd=['Nooun90']

from flask import Flask, render_template, session, url_for, redirect, request, sessions
import random, string

app=Flask(__name__)

app.secret_key='Crazy_Willy_Jones'


@app.route("/")
def first():
    return render_template("login.html")

@app.route("/",methods=['GET',"POST"])
def login():
    password=request.form.get("password")
    username=request.form.get("username")
    if password == passwd[0]:
        return render_template("home.html")
    return render_template("login.html")


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run()
