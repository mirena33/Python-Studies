strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)  # or raspberries_price * 0.6
bananas_price = raspberries_price - (raspberries_price * 0.8)  # or raspberries_price * 0.2

total_price_strawberries = strawberries_kg * strawberries_price
total_price_bananas = bananas_kg * bananas_price
total_price_oranges = oranges_kg * oranges_price
total_price_raspberries = raspberries_kg * raspberries_price
total_sum = total_price_strawberries + total_price_bananas + total_price_oranges + total_price_raspberries

print(f"{total_sum:.2f}")
