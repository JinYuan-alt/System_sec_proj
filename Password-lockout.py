passwd=['Nooun90']

from flask import Flask, render_template, session, url_for, redirect, request, sessions
import random, string

app=Flask(__name__)

app.secret_key='Crazy_Willy_Jones'

letters = string.ascii_lowercase
final_str = []
seshid=""
beta_str = ''.join(random.choice(letters) for i in range(8))
for i in range(len(beta_str)):
    final_str.append(beta_str[i])
for i in range(len(final_str)):
    if (i + 1) % 2 == 0 and final_str[i] != final_str[-1]:
        final_str.insert(random.randint(0, 9),i)
for i in range(len(final_str)):
    temp=final_str[i]
    seshid=seshid+str(temp)

print("Random string of random length","is:", seshid)

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
