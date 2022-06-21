fires = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
valid_cells = list()

for curr_fire in fires:
    fire_cell_info = curr_fire.split(" = ")
    fire_type = fire_cell_info[0]
    fire_value = int(fire_cell_info[1])

    if fire_type == "High":
        if 81 <= fire_value <= 125:
            if water - fire_value < 0:
                continue
        else:
            continue

    elif fire_type == "Medium":
        if 51 <= fire_value <= 80:
            if water - fire_value < 0:
                continue
        else:
            continue

    elif fire_type == "Low":
        if 1 <= fire_value <= 50:
            if water - fire_value < 0:
                continue
        else:
            continue

    valid_cells.append(fire_value)
    water -= fire_value
    total_effort += fire_value * 0.25

print("Cells:")
for cell in valid_cells:
    print(f"- {cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {sum(valid_cells)}")
