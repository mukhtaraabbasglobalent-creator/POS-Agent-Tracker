import sqlite3
from datetime import datetime

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("pos_agent.db")
cursor = conn.cursor()

# Create transactions table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    location TEXT NOT NULL,
    description TEXT,
    charge REAL NOT NULL,
    profit REAL NOT NULL,
    date TEXT NOT NULL
)
""")
conn.commit()

# Add a transaction
def add_transaction(t_type, amount, location, description, charge, profit):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
    INSERT INTO transactions (type, amount, location, description, charge, profit, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (t_type, amount, location, description, charge, profit, date_str))
    conn.commit()

# Get all transactions
def get_all_transactions():
    cursor.execute("SELECT type, amount, location, description, charge, profit, date FROM transactions")
    rows = cursor.fetchall()
    transactions = []
    for row in rows:
        transactions.append({
            "type": row[0],
            "amount": row[1],
            "location": row[2],
            "description": row[3],
            "charge": row[4],
            "profit": row[5],
            "date": datetime.strptime(row[6], "%Y-%m-%d %H:%M:%S")
        })
    return transactions

# Close connection when done
def close_connection():
    conn.close()
