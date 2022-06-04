cats_cnt = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
total_food = 0

for i in range(cats_cnt):
    food_grams = float(input())
    total_food += food_grams

    if food_grams < 200:
        group_1 += 1
    elif food_grams < 300:
        group_2 += 1
    else:
        group_3 += 1

cat_food_per_day = (total_food / 1000) * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {cat_food_per_day:.2f} lv.")
