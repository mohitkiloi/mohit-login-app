import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

users = [f"user{i:02d}@mh-cybersolutions.de" for i in range(1, 31)]
roles = ['developer', 'admin', 'hr', 'finance', 'security', 'marketing']
resolutions = ["1920x1080", "1366x768", "1024x768", "1536x864", "800x600"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.68.0",
    "Python-urllib/3.8"
]

attack_types = ["normal", "brute_force", "credential_stuffing", "geo_spoofing", "bot_login", "insider_threat"]


def generate_log_row(user, attack_type):
    ip = fake.ipv4()
    location = fake.city() + ", " + fake.country()
    screen_res = random.choice(resolutions)
    user_agent = random.choice(user_agents)
    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 10000))

    if attack_type == "normal":
        status = "success" if random.random() > 0.05 else "failure"
    elif attack_type == "brute_force":
        status = "failure"
    elif attack_type == "credential_stuffing":
        status = "failure"
    elif attack_type == "geo_spoofing":
        location = fake.city() + ", Russia"
        status = "success" if random.random() > 0.2 else "failure"
    elif attack_type == "bot_login":
        screen_res = "800x600"
        user_agent = "Python-urllib/3.8"
        status = "success" if random.random() > 0.2 else "failure"
    elif attack_type == "insider_threat":
        status = "success"
        timestamp = timestamp.replace(hour=random.choice([2, 3, 4]))
    else:
        status = "failure"

    return {
        "timestamp": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        "email": user,
        "status": status,
        "ip": ip,
        "location": location,
        "screen_resolution": screen_res,
        "user_agent": user_agent,
        "attack_type": attack_type
    }

logs = []
for _ in range(10000):
    user = random.choice(users)
    attack_type = random.choices(attack_types, weights=[60, 10, 10, 10, 5, 5])[0]
    logs.append(generate_log_row(user, attack_type))

pd.DataFrame(logs).to_csv("logs.csv", index=False)
print("Generated 10,000 fake login logs into logs.csv")
