flowers_type = input()
flowers_cnt = int(input())
budget = int(input())

price_per_flower = 0
discount_percent = 0
higher_rate_percent = 0

if flowers_type == "Roses":
    price_per_flower = 5
    if flowers_cnt > 80:
        discount_percent = 0.1

elif flowers_type == "Dahlias":
    price_per_flower = 3.80
    if flowers_cnt > 90:
        discount_percent = 0.15

elif flowers_type == "Tulips":
    price_per_flower = 2.80
    if flowers_cnt > 80:
        discount_percent = 0.15

elif flowers_type == "Narcissus":
    price_per_flower = 3
    if flowers_cnt < 120:
        higher_rate_percent = 0.15

elif flowers_type == "Gladiolus":
    price_per_flower = 2.50
    if flowers_cnt < 80:
        higher_rate_percent = 0.2

total_price = flowers_cnt * price_per_flower
total_price -= total_price * discount_percent
total_price += total_price * higher_rate_percent

if budget >= total_price:
    print(f"Hey, you have a great garden with"
          f" {flowers_cnt} {flowers_type} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")

