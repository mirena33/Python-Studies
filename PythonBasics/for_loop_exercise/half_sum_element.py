import sys

n = int(input())
total_sum = 0
max_number = -sys.maxsize

for i in range(0, n):
    curr_number = int(input())
    total_sum += curr_number

    if curr_number > max_number:
        max_number = curr_number

total_sum -= max_number

if total_sum == max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {abs(max_number - total_sum)}")
