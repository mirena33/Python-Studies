location_cnt = int(input())

for i in range(location_cnt):
    expected_avg_gold_per_day = float(input())
    days = int(input())
    mined_gold_per_location = 0

    for j in range(days):
        mined_gold_per_day = float(input())
        mined_gold_per_location += mined_gold_per_day

    avg_mined_gold_per_location = mined_gold_per_location / days
    if avg_mined_gold_per_location >= expected_avg_gold_per_day:
        print(f"Good job! Average gold per day: {avg_mined_gold_per_location:.2f}.")
    else:
        print(f"You need {expected_avg_gold_per_day - avg_mined_gold_per_location:.2f} gold.")
