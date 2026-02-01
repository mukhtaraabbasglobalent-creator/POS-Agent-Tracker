from database import get_all_transactions
from datetime import datetime

def daily_summary():
    records = get_all_transactions()
    today = datetime.now().strftime("%Y-%m-%d")
    
    total_deposit = 0
    total_withdrawal = 0
    total_charge = 0
    total_profit = 0
    total_money = 0

    for record in records:
        date, t_type, amount, charge, profit, cash_box, cash_wallet, total, desc = record[1:]
        if date.startswith(today):
            if t_type.lower() == "deposit":
                total_deposit += amount
            elif t_type.lower() == "withdrawal":
                total_withdrawal += amount
            total_charge += charge
            total_profit += profit
            total_money += total

    print("\n=== Daily Summary ===")
    print(f"Total Deposit: ₦{total_deposit}")
    print(f"Total Withdrawal: ₦{total_withdrawal}")
    print(f"Total Charges: ₦{total_charge}")
    print(f"Total Profit: ₦{total_profit}")
    print(f"Total Business Money: ₦{total_money}")
    print("====================\n")

def monthly_summary():
    records = get_all_transactions()
    current_month = datetime.now().strftime("%Y-%m")
    
    total_deposit = 0
    total_withdrawal = 0
    total_charge = 0
    total_profit = 0
    total_money = 0

    for record in records:
        date, t_type, amount, charge, profit, cash_box, cash_wallet, total, desc = record[1:]
        if date.startswith(current_month):
            if t_type.lower() == "deposit":
                total_deposit += amount
            elif t_type.lower() == "withdrawal":
                total_withdrawal += amount
            total_charge += charge
            total_profit += profit
            total_money += total

    print("\n=== Monthly Summary ===")
    print(f"Total Deposit: ₦{total_deposit}")
    print(f"Total Withdrawal: ₦{total_withdrawal}")
    print(f"Total Charges: ₦{total_charge}")
    print(f"Total Profit: ₦{total_profit}")
    print(f"Total Business Money: ₦{total_money}")
    print("======================\n")
