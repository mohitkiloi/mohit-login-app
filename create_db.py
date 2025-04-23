import sqlite3
import csv

# Connect to SQLite DB (creates new file)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE users (
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
''')

# Read from CSV and insert into table
with open("users.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("INSERT INTO users (email, password, role) VALUES (?, ?, ?)",
                       (row["email"], row["password"], row["role"]))

conn.commit()
conn.close()

print("✅ users.db created successfully from users.csv")
