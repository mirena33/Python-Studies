sums_list_as_string = input().split(", ")
beggars_cnt = int(input())
final_list = list()
index_counter = 0

# list comprehension:
# sums_list_as_digits = [int(i) for i in sums_list_as_string]

sums_list_as_digits = list()
for element in sums_list_as_string:
    sums_list_as_digits.append(int(element))

while index_counter < beggars_cnt:
    sum_for_current_beggar = 0
    for current_index in range(index_counter, len(sums_list_as_digits), beggars_cnt):
        sum_for_current_beggar += sums_list_as_digits[current_index]
    index_counter += 1
    final_list.append(sum_for_current_beggar)

print(final_list)
