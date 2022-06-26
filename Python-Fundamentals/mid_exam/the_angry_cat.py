price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_of_items = input()

left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]

left_sum = 0
right_sum = 0
entry_point_element = price_ratings[entry_point]

if type_of_items == "cheap":
    for price in left_side:
        if price < entry_point_element:
            left_sum += price

    for price in right_side:
        if price < entry_point_element:
            right_sum += price


elif type_of_items == "expensive":
    for price in left_side:
        if price >= entry_point_element:
            left_sum += price

    for price in right_side:
        if price >= entry_point_element:
            right_sum += price

if left_sum > right_sum:
    print(f"Left - {left_sum}")
elif right_sum > left_sum:
    print(f"Right - {right_sum}")
elif left_sum == right_sum:
    print(f"Left - {left_sum}")
