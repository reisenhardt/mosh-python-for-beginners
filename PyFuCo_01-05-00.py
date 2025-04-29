has_good_credit = True
price = 1000000


if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Your down payment is {int(down_payment)} US $")
