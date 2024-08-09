from flask import Flask, render_template, session, url_for, redirect, request, sessions, abort
import uuid, datetime
from PIL import Image

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def image():
    if request.method == 'POST' and 'txt' in request.form and 'img' in request.form:
         image=request.form.get('img')
         text=request.form['txt']
         print(text)
    return render_template('post.html')


if __name__ == '__main__':
    app.run()
