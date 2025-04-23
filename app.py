from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import jsonify
import sqlite3
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

LOG_FILE = 'logs.csv'

if not os.path.exists(LOG_FILE):
    pd.DataFrame(columns=['timestamp', 'email', 'status', 'role', 'action']).to_csv(LOG_FILE, index=False)

def verify_user(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE email=?", (email,))
    record = cursor.fetchone()
    conn.close()
    if record and record[0] == password:
        return record[1]
    return None

def log_event(email, status, role, action):
    if 'favicon.ico' in action:
        return
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df = pd.read_csv(LOG_FILE)
    df.loc[len(df.index)] = [timestamp, email, status, role, action]
    df.to_csv(LOG_FILE, index=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    role = verify_user(email, password)
    if role:
        session['email'] = email
        session['role'] = role
        log_event(email, 'success', role, 'login')
        return redirect(url_for('landing'))

    else:
        flash('Invalid credentials. Try again.')
        log_event(email, 'fail', 'unknown', 'login')
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    log_event(email, 'success', role, 'logout')
    session.clear()
    return redirect(url_for('home'))

@app.route('/<role>')
def dashboard(role):
    user_role = session.get('role')
    email = session.get('email', 'unknown')
    if user_role == role:
        log_event(email, 'success', role, f'access:{role}')
        return render_template(f"{role}.html", email=email, role=role)
    else:
        log_event(email, 'unauthorized', user_role, f'attempted_access:{role}')
        flash('Unauthorized access.')
        return redirect(url_for('home'))

@app.route('/admin')
def admin():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("admin.html", email=email, role=role)

@app.route('/developer')
def developer():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("developer.html", email=email, role=role)

@app.route('/security')
def security():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("security.html", email=email, role=role)

@app.route('/marketing')
def marketing():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("marketing.html", email=email, role=role)

@app.route('/hr')
def hr():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("hr.html", email=email, role=role)

@app.route('/finance')
def finance():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template("finance.html", email=email, role=role)

@app.route('/log_unauthorized', methods=['POST'])
def log_unauthorized():
    data = request.json
    email = session.get('email', 'unknown')
    user_role = session.get('role', 'unknown')
    attempted_role = data.get('attempted_role', 'unknown')
    log_event(email, 'unauthorized', user_role, f"attempted_access:{attempted_role}")
    return jsonify({'status': 'logged'})

@app.route('/landing')
def landing():
    email = session.get('email', 'unknown')
    role = session.get('role', 'unknown')
    return render_template('landing.html', email=email, role=role)

if __name__ == '__main__':
    app.run(debug=True, port=5001)