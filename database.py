import sqlite3

DB_NAME = "pos_agent_tracker.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        type TEXT,
        amount REAL,
        charge REAL,
        profit REAL,
        cash_box REAL,
        cash_wallet REAL,
        total_money REAL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_transaction(data):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (date, type, amount, charge, profit, cash_box, cash_wallet, total_money, description)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()

def get_all_transactions():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    records = cursor.fetchall()

    conn.close()
    return records
