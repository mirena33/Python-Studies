days_count = int(input())
total_food = float(input())

total_eaten_food = 0
total_eaten_food_by_cat = 0
total_eaten_food_by_dog = 0
biscuit_grams = 0

for i in range(1, days_count + 1):
    dog_food_per_day = int(input())
    cat_food_per_day = int(input())

    total_eaten_food_by_cat += cat_food_per_day
    total_eaten_food_by_dog += dog_food_per_day

    if i % 3 == 0:
        biscuit_grams += (dog_food_per_day + cat_food_per_day) * 0.1

total_eaten_food = total_eaten_food_by_cat + total_eaten_food_by_dog

print(f"Total eaten biscuits: {round(biscuit_grams)}gr.")
print(f"{total_eaten_food / total_food * 100:.2f}% of the food has been eaten.")
print(f"{total_eaten_food_by_dog / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{total_eaten_food_by_cat / total_eaten_food * 100:.2f}% eaten from the cat.")
