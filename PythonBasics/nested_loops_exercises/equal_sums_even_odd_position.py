first_number = int(input())
second_number = int(input())
is_equal = False

for i in range(first_number, second_number + 1):
    current_num_to_str = str(i)
    even_sum = 0
    odd_sum = 0

    for j, digit in enumerate(current_num_to_str):
        if j % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(f"{current_num_to_str}", end=" ")
