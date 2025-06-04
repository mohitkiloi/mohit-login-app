from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
import pandas as pd
import sqlite3
import os
import requests
from detect_anomaly import detect_single_login

app = Flask(__name__)
app.secret_key = 'super_secret_key_here'

LOG_FILE = 'logs.csv'
ALERT_FILE = 'alert_report.csv'

# Ensure log files exist
for file, cols in [
    (LOG_FILE, ['timestamp', 'email', 'status', 'ip', 'location', 'screen_resolution', 'user_agent', 'suspicious']),
    (ALERT_FILE, ['timestamp', 'email', 'ip', 'reason', 'score'])
]:
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        pd.DataFrame(columns=cols).to_csv(file, index=False)

# Authenticate user
def verify_user(email, password):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT password, role FROM users WHERE email=?", (email,))
    user = cur.fetchone()
    conn.close()
    return user if user and user[0] == password else None

# Get geolocation from IP
def get_location(ip):
    try:
        res = requests.get(f'https://ipapi.co/{ip}/json/').json()
        return f"{res.get('city')}, {res.get('country_name')}"
    except:
        return "Unknown"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        screen_res = request.form.get("screen_resolution", "unknown")
        ip = request.headers.get("X-Forwarded-For", request.remote_addr)
        location = get_location(ip)
        user_agent = request.headers.get("User-Agent")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        user_data = verify_user(email, password)
        status = "success" if user_data else "failure"
        role = user_data[1] if user_data else None

        log_row = {
            "timestamp": timestamp,
            "email": email,
            "status": status,
            "ip": ip,
            "location": location,
            "screen_resolution": screen_res,
            "user_agent": user_agent
        }

        # Run anomaly detection safely
        try:
            suspicious, reason, score = detect_single_login(log_row)
        except:
            suspicious, reason, score = False, "Detection Failed", 0.0

        log_row["suspicious"] = "yes" if suspicious else "no"

        # Save to logs.csv
        logs = pd.read_csv(LOG_FILE)
        logs = pd.concat([logs, pd.DataFrame([log_row])], ignore_index=True)
        logs.to_csv(LOG_FILE, index=False)

        # Save to alert_report.csv if suspicious
        if suspicious:
            alert = {
                "timestamp": timestamp,
                "email": email,
                "ip": ip,
                "reason": reason,
                "score": score
            }

            if os.path.exists(ALERT_FILE) and os.path.getsize(ALERT_FILE) > 0:
                alerts = pd.read_csv(ALERT_FILE)
            else:
                alerts = pd.DataFrame(columns=["timestamp", "email", "ip", "reason", "score"])

            alerts = pd.concat([alerts, pd.DataFrame([alert])], ignore_index=True)
            alerts.to_csv(ALERT_FILE, index=False)
            flash("⚠️ Suspicious login detected!", "danger")

        if status == "success":
            session["email"] = email
            session["role"] = role
            return redirect(url_for("landing"))
        else:
            flash("❌ Login failed. Please try again.", "warning")

    return render_template("login.html")

@app.route("/landing")
def landing():
    if "email" in session:
        return render_template("landing.html", email=session["email"], role=session["role"])
    return redirect(url_for("login"))

@app.route("/dashboard/<role>")
def dashboard(role):
    if "role" in session and session["role"] == role:
        return render_template("dashboard.html", user=session["email"], dept=role)
    flash("🚫 Unauthorized access!", "danger")
    return redirect(url_for("landing"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
