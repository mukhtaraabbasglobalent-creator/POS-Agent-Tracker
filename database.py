from datetime import datetime

# In-memory database for demo purposes; replace with real DB if needed
transactions = []

def add_transaction(t_type, amount, location, description, charge, profit):
    transactions.append({
        "type": t_type,
        "amount": amount,
        "location": location,
        "description": description,
        "charge": charge,
        "profit": profit,
        "date": datetime.now()
    })

def get_all_transactions():
    return transactions
