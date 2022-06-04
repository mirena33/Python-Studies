import math

avg_speed = float(input())
fuel_litres_for_100_km = float(input())

time_going_and_returning = math.ceil(768800 / avg_speed) + 3
needed_fuel = (768800 * fuel_litres_for_100_km) / 100

print(time_going_and_returning)
print(f"{needed_fuel:g}")

