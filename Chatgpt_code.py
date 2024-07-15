from flask import Flask, request, session, redirect, url_for, render_template_string
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Configuration
MAX_FAILED_ATTEMPTS = 3
LOCKOUT_TIME = 300  # Lockout period in seconds (5 minutes)

# In-memory storage for demonstration purposes
users = {'user': 'password'}  # Replace with your user storage
failed_attempts = {}
lockout_timers = {}


@app.route('/')
def home():
    if 'username' in session:
        return f"Hello, {session['username']}! <a href='/logout'>Logout</a>"
    return render_template_string('''
        <form method="post" action="/login">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
        {% if error %}
            <p style="color:red;">{{ error }}</p>
        {% endif %}
    ''')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in lockout_timers and time.time() < lockout_timers[username]:
        return render_template_string('''
            <p style="color:red;">Account locked. Try again later.</p>
            <a href="/">Back to login</a>
        ''')

    if username in users and users[username] == password:
        session['username'] = username
        if username in failed_attempts:
            del failed_attempts[username]
        return redirect(url_for('home'))

    if username not in failed_attempts:
        failed_attempts[username] = 0

    failed_attempts[username] += 1

    if failed_attempts[username] >= MAX_FAILED_ATTEMPTS:
        lockout_timers[username] = time.time() + LOCKOUT_TIME
        return render_template_string('''
            <p style="color:red;">Too many failed attempts. Account locked for 5 minutes.</p>
            <a href="/">Back to login</a>
        ''')

    return render_template_string('''
        <p style="color:red;">Invalid username or password.</p>
        <a href="/">Back to login</a>
    ''', error="Invalid username or password.")


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
