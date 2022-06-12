snowball_cnt = int(input())

best_value = 0
best_weight = 0
best_time = 0
best_quality = 0

for _ in range(snowball_cnt):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = int((snowball_weight / snowball_time) ** snowball_quality)

    if best_value < value:
        best_value = value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality

print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
