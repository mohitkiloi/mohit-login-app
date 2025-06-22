import sqlite3

# Connect to or create the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

# Define user roles
roles = ['developer', 'admin', 'hr', 'finance', 'security', 'marketing']

# Generate 30 users with passwords and rotating roles
users = []
for i in range(1, 31):
    email = f"user{i:02d}@mh-cybersolutions.de"
    password = f"pass{i:02d}"
    role = roles[i % len(roles)]
    users.append((email, password, role))

# Insert users into the database
cursor.executemany("""
INSERT OR IGNORE INTO users (email, password, role)
VALUES (?, ?, ?)
""", users)

conn.commit()
conn.close()

print("Created users.db with 30 users.")
