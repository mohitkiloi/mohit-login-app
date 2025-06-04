# 🔐 Mohit Login App — AI-Powered Secure Login Detection System

An advanced Flask-based login application that detects suspicious login behavior using machine learning (Isolation Forest), logs events, and visualizes results using Streamlit. CI/CD pipeline powered by Jenkins.

---

## 🚀 Features

* 🔐 **Flask Web App** — Email/password-based login system with user roles
* 🧠 **AI Detection** — Isolation Forest model flags suspicious logins in real-time
* 📊 **Streamlit Dashboard** — View alerts, model performance, and metrics
* 📁 **Logging** — All login attempts saved to `logs.csv` with metadata
* ⚙️ **Jenkins Pipeline** — Automates log generation, model training, detection, and reporting
* 🧾 **Reports** — Anomaly alerts saved to `alert_report.csv`, AI metrics in `metrics_report.json`

---

## 📂 Project Structure

```
mohit-login-app/
├── app.py                  # Flask login system
├── create_users_db.py     # Generate users.db with credentials
├── generate_fake_logs.py  # Simulate login attempts (10K logs)
├── train_model.py         # Train Isolation Forest model
├── detect_anomaly.py      # Flag suspicious activity
├── streamlit_app.py       # Streamlit alert dashboard
├── requirements.txt       # Python dependencies
├── Jenkinsfile            # Jenkins pipeline definition
├── gnn/                   # (Phase 2) GNN login graph detection
├── jenkins/email_alert.sh # Email script for alerts
├── logs.csv               # All login attempts
├── alert_report.csv       # AI-detected anomalies
├── experiments/           # Model metrics JSON
└── templates/ & static/   # HTML and JS for frontend
```

---

## 🛠️ Setup Instructions

### 📦 Requirements

* Python 3.8+
* pip
* (Optional) Jenkins + GitHub + Streamlit

### 🧪 Local Development

```bash
git clone https://github.com/mohitkiloi/mohit-login-app.git
cd mohit-login-app
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt

python create_users_db.py
python generate_fake_logs.py
python train_model.py
python detect_anomaly.py
python app.py
```

Then open: `http://localhost:5000`

### 📊 Launch Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 🧠 AI Model (Isolation Forest)

* Features used:

  * login status (success/failure)
  * screen resolution
  * user-agent length
  * location string length
* Trained on 10,000+ logs
* Model saved as `model.joblib`

---

## ⚙️ Jenkins Pipeline Stages

1. Clone Git repo
2. Set up virtual environment
3. Generate logs
4. Train AI model
5. Run anomaly detection
6. Display logs & alerts
7. Archive results (CSV + JSON)

---

## 🔐 Sample Login Credentials

| Email                                                             | Password | Role      |
| ----------------------------------------------------------------- | -------- | --------- |
| [user01@mh-cybersolutions.de](mailto:user01@mh-cybersolutions.de) | pass01   | developer |
| [user02@mh-cybersolutions.de](mailto:user02@mh-cybersolutions.de) | pass02   | admin     |

---

## 📃 License

This project is part of a Master's thesis by Mohit Hooda — for academic & educational purposes.

---

## 🤝 Contact

For questions, issues, or collaborations:
📧 [mohit.hooda.student@gmail.com](mailto:mohit.hooda.student@gmail.com)
