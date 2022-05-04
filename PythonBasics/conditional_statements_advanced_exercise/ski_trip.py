days = int(input())
room_type = input()
review = input()

discount_percent = 0
total_price = 0
price_per_night = 0

if room_type == "apartment":
    price_per_night = 25

    if days < 10:
        discount_percent = 0.3
    elif days <= 15:
        discount_percent = 0.35
    elif days > 15:
        discount_percent = 0.5

elif room_type == "president apartment":
    price_per_night = 35

    if days < 10:
        discount_percent = 0.1
    elif days <= 15:
        discount_percent = 0.15
    elif days > 15:
        discount_percent = 0.2

elif room_type == "room for one person":
    price_per_night = 18

total_price = price_per_night * (days - 1)
total_price -= total_price * discount_percent

if review == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")
