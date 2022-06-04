import math

fan_name = input()
budget = float(input())
beers_cnt = int(input())
chips_cnt = int(input())

beer_price = beers_cnt * 1.20
price_per_chips = beer_price * 0.45
chips_price = math.ceil(price_per_chips * chips_cnt)
total_price = beer_price + chips_price

if budget >= total_price:
    print(f"{fan_name} bought a snack and has {budget - total_price:.2f} leva left.")
else:
    print(f"{fan_name} needs {total_price - budget:.2f} more leva!")
