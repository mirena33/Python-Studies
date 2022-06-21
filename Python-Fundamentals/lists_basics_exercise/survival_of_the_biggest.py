numbers_list_strings = input().split(" ")
numbers_to_remove = int(input())
numbers_list_integers = list()

for element in numbers_list_strings:
    numbers_list_integers.append(int(element))

numbers_list_strings.clear()

while numbers_to_remove > 0:
    min_number = min(numbers_list_integers)
    numbers_list_integers.remove(min_number)
    numbers_to_remove -= 1

for el in numbers_list_integers:
    numbers_list_strings.append(str(el))

print(", ".join(numbers_list_strings))

# Another solution:

# import sys
#
# numbers_list_strings = input().split(" ")
# numbers_to_remove = int(input())
# numbers_list_integers = list()
#
# for element in numbers_list_strings:
#     numbers_list_integers.append(int(element))
#
# numbers_list_strings.clear()
#
# while numbers_to_remove > 0:
#     smallest_num = sys.maxsize
#
#     for number in numbers_list_integers:
#
#         if number < smallest_num:
#             smallest_num = number
#
#     numbers_list_integers.remove(smallest_num)
#     numbers_to_remove -= 1
#
# for el in numbers_list_integers:
#     numbers_list_strings.append(str(el))
#
# print(", ".join(numbers_list_strings))
