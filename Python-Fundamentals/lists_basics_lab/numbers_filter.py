lines_cnt = int(input())
numbers = list()  # numbers = [int(input()) for _ in range(lines_cnt)]
filtered_numbers = list()

for i in range(lines_cnt):
    curr_number = int(input())
    numbers.append(curr_number)

command = input()

if command == "even":
    for element in numbers:
        if element % 2 == 0:
            filtered_numbers.append(element)

elif command == "odd":
    for element in numbers:
        if element % 2 != 0:
            filtered_numbers.append(element)

elif command == "negative":
    for element in numbers:
        if element < 0:
            filtered_numbers.append(element)

elif command == "positive":
    for element in numbers:
        if element >= 0:
            filtered_numbers.append(element)

print(filtered_numbers)

# Another approach

# for num in numbers:
#     filter_command = (
#             (command == "even" and num % 2 == 0) or
#             (command == "odd" and num % 2 != 0) or
#             (command == "negative" and num < 0) or
#             (command == "positive" and num >= 0)
#     )
#
#     if filter_command:
#         filtered_numbers.append(num)
#
# print(filtered_numbers)
