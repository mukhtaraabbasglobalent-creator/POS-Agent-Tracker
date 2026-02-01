import tkinter as tk
from tkinter import messagebox
from database import create_tables, add_transaction
from calculations import calculate_charge, calculate_profit, calculate_total_money
from reports import daily_summary, monthly_summary
from export_reports import export_daily_csv, export_monthly_csv
import datetime

create_tables()

# Main window
root = tk.Tk()
root.title("POS Agent Tracker")
root.geometry("500x400")

# Functions for buttons
def add_transaction_gui():
    t_type = type_var.get()
    try:
        amount = float(amount_entry.get())
        cash_box = float(box_entry.get())
        cash_wallet = float(wallet_entry.get())
        desc = desc_entry.get()

        charge = calculate_charge(amount)
        profit = calculate_profit(amount, charge)
        total_money = calculate_total_money(cash_box, cash_wallet)
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        add_transaction((date, t_type, amount, charge, profit, cash_box, cash_wallet, total_money, desc))
        messagebox.showinfo("Success", f"Transaction Saved!\nCharge: ₦{charge}\nProfit: ₦{profit}\nTotal Money: ₦{total_money}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def show_daily_summary_gui():
    daily_summary()

def show_monthly_summary_gui():
    monthly_summary()

def export_daily_gui():
    export_daily_csv()

def export_monthly_gui():
    export_monthly_csv()

# Widgets
tk.Label(root, text="Transaction Type:").pack()
type_var = tk.StringVar(value="Deposit")
tk.OptionMenu(root, type_var, "Deposit", "Withdrawal").pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Cash in Box:").pack()
box_entry = tk.Entry(root)
box_entry.pack()

tk.Label(root, text="Cash in Wallet:").pack()
wallet_entry = tk.Entry(root)
wallet_entry.pack()

tk.Label(root, text="Description:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Button(root, text="Add Transaction", command=add_transaction_gui).pack(pady=5)
tk.Button(root, text="Daily Summary", command=show_daily_summary_gui).pack(pady=5)
tk.Button(root, text="Monthly Summary", command=show_monthly_summary_gui).pack(pady=5)
tk.Button(root, text="Export Daily Report", command=export_daily_gui).pack(pady=5)
tk.Button(root, text="Export Monthly Report", command=export_monthly_gui).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
