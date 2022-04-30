budget = float(input())
statists_cnt = int(input())
clothes_price_per_statist = float(input())

decor_price = budget * 0.10
clothes_price = statists_cnt * clothes_price_per_statist

if statists_cnt > 150:
    clothes_price -= clothes_price * 0.10

total_price = decor_price + clothes_price

if budget >= total_price:
    print(f"Action!\nWingard starts filming with {budget - total_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
