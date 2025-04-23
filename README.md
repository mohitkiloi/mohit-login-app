
# Mohit Hooda Cyber Solutions GmbH - Employee Login Portal

🚀 A secure, role-based web login portal built with **Flask**. Simulates enterprise login for employees, with full logging, authentication, and CI/CD integration readiness.

---

## 🌟 Features
- Role-based login (developer, security, marketing, HR, finance, admin)
- Colorful UI with Ghibli-style background
- Authentication via SQLite database (`users.db`)
- Logs every login attempt and role-based access in `logs.csv`
- Landing page shows buttons to select roles (access-controlled)
- Unauthorized access attempts are logged and alerted
- Ready for Jenkins CI/CD integration

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Database**: SQLite (`users.db`)
- **Logging**: CSV via Pandas
- **Frontend**: HTML/CSS + Jinja2 templating
- **Deployment Ready**: GitHub + Jenkins CI/CD

---

## 🔧 Setup Instructions

1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/flask-login-app.git
    cd flask-login-app
    ```

2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create the database from CSV:
    ```bash
    python create_db.py
    ```

5. Run the Flask app:
    ```bash
    python app.py
    ```

6. Visit: [http://localhost:5001](http://localhost:5001)

---

## 👤 Roles & Sample Logins

| Role     | Email                                | Password      |
|----------|--------------------------------------|---------------|
| Admin    | mohit.hooda@mh-cybersolutions.de     | admin123      |
| Dev      | rohit.hooda@mh-cybersolutions.de     | devpass123    |
| HR       | ravi.kumar@mh-cybersolutions.de      | hrpass123     |
| Finance  | julia.neumann@mh-cybersolutions.de   | finpass123    |
| ...      | ...                                  | ...           |

*(Full list in `users.csv`)*

---

## 📝 Logging Format

Logs are stored in `logs.csv` as:

```
timestamp,email,status,role,action
2025-04-23 19:51:39,rohit.hooda@mh-cybersolutions.de,success,developer,login
```

---

## 🔒 Security Notes
- Access only allowed to user's assigned role
- Unauthorized access is logged and redirected
- `favicon.ico` requests are filtered

---

## 🛠️ CI/CD (Jenkins)
Use this repo as a GitHub source for Jenkins pipeline to:
- Pull latest code
- Run Flask app locally or on server
- Monitor logs

---

## 📷 Preview
![Login UI](static/images/background.jpg)

---

## 📬 Contact
Created by **Mohit Hooda**  
"# demo" 
