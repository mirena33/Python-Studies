from math import ceil

people_cnt = int(input())
elevator_capacity = int(input())
courses = 0

if elevator_capacity != 0:
    courses = ceil(people_cnt / elevator_capacity)

print(courses)
