import pandas as pd
import random
from datetime import datetime, timedelta

credentials = [
    ("mohit.hooda@mh-cybersolutions.de", "admin"),
    ("rohit.hooda@mh-cybersolutions.de", "developer"),
    ("ayush.mehta@mh-cybersolutions.de", "developer"),
    ("anika.sharma@mh-cybersolutions.de", "developer"),
    ("lisa.schmidt@mh-cybersolutions.de", "security"),
    ("felix.berger@mh-cybersolutions.de", "security"),
    ("kavya.pandey@mh-cybersolutions.de", "security"),
    ("ravi.kumar@mh-cybersolutions.de", "hr"),
    ("sophie.muller@mh-cybersolutions.de", "hr"),
    ("julia.neumann@mh-cybersolutions.de", "finance"),
    ("rahul.yadav@mh-cybersolutions.de", "finance"),
    ("meera.das@mh-cybersolutions.de", "marketing"),
    ("thomas.meyer@mh-cybersolutions.de", "marketing"),
    ("anjali.rai@mh-cybersolutions.de", "marketing"),
    ("nikhil.singh@mh-cybersolutions.de", "developer"),
    ("tina.joseph@mh-cybersolutions.de", "security"),
    ("arun.k@mh-cybersolutions.de", "hr"),
    ("nadia.fischer@mh-cybersolutions.de", "finance"),
    ("steven.bauer@mh-cybersolutions.de", "marketing"),
]

logs = []
start_time = datetime.now()

for _ in range(500):
    email, role = random.choice(credentials)
    timestamp = start_time - timedelta(seconds=random.randint(0, 3600))
    status = random.choices(["success", "fail"], weights=[0.85, 0.15])[0]
    logs.append({
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "email": email,
        "role": role,
        "action": "login_attempt",
        "status": status
    })

df = pd.DataFrame(logs)
df.to_csv("logs.csv", index=False)
print("[INFO] Fake logs written to logs.csv")

