import datetime
from database import create_tables, add_transaction
from calculations import calculate_charge, calculate_profit, calculate_total_money

def main():
    create_tables()
    print("=== POS Agent Tracker ===")

    while True:
        print("\n1. Add Transaction")
        print("2. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            t_type = input("Transaction Type (Deposit/Withdrawal): ")
            amount = float(input("Amount: "))
            cash_box = float(input("Cash in Box: "))
            cash_wallet = float(input("Cash in Wallet: "))
            desc = input("Description: ")

            charge = calculate_charge(amount)
            profit = calculate_profit(amount, charge)
            total_money = calculate_total_money(cash_box, cash_wallet)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            add_transaction((date, t_type, amount, charge, profit, cash_box, cash_wallet, total_money, desc))

            print("\nTransaction Saved!")
            print(f"Charge: ₦{charge}")
            print(f"Profit: ₦{profit}")
            print(f"Total Business Money: ₦{total_money}")

        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
