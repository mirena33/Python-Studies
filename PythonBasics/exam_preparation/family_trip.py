budget = float(input())
nights_cnt = int(input())
price_per_night = float(input())
additional_costs_percent = int(input())

additional_costs_amount = budget * (additional_costs_percent / 100)

if nights_cnt > 7:
    price_per_night -= price_per_night * 0.05

trip_price = price_per_night * nights_cnt + additional_costs_amount

if budget >= trip_price:
    print(f"Ivanovi will be left with {budget - trip_price:.2f} leva after vacation.")
else:
    print(f"{trip_price - budget:.2f} leva needed.")
