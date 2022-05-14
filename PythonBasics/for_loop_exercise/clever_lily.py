lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

savings = 0
toys_cnt = 0
even_years_cnt = 0
money_gifted = 10

for current_age in range(1, lily_age + 1):
    if current_age % 2 == 0:
        savings += (current_age * 5) - 1
    else:
        toys_cnt += 1

savings += toys_cnt * toy_price

if washer_price <= savings:
    print(f"Yes! {savings - washer_price:.2f}")
else:
    print(f"No! {washer_price - savings:.2f}")
