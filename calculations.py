def calculate_charge(amount):
    if 1000 <= amount <= 9999:
        return 100
    elif 10000 <= amount <= 19999:
        return 200
    elif 20000 <= amount <= 49999:
        return 500
    elif 50000 <= amount <= 100000:
        return 1000
    else:
        return 0


def calculate_profit(amount, charge):
    return amount - charge


def calculate_total_money(cash_box, cash_wallet):
    return cash_box + cash_wallet
