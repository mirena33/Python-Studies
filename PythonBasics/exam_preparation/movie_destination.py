movie_budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0
discount = 0
increase = 0

if season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
        discount = 0.3

    elif destination == "Sofia":
        price_per_day = 12500
        increase = 0.25

    elif destination == "London":
        price_per_day = 20250

elif season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
        discount = 0.3

    elif destination == "Sofia":
        price_per_day = 17000
        increase = 0.25

    elif destination == "London":
        price_per_day = 24000

total_price = days * price_per_day
total_price += total_price * increase
total_price -= total_price * discount

diff = abs(movie_budget - total_price)

if movie_budget >= total_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
