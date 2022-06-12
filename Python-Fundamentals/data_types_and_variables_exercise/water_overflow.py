lines = int(input())
tank_capacity = 0

for i in range(lines):
    water_litres = int(input())

    if tank_capacity + water_litres > 255:
        print("Insufficient capacity!")
        continue

    tank_capacity += water_litres

print(tank_capacity)
