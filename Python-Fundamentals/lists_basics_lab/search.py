input_lines = int(input())
key_word = input()
search_list = list()

for i in range(input_lines):
    curr_string = input()
    search_list.append(curr_string)

print(search_list)

for i in range(len(search_list) - 1, -1, -1):
    element = search_list[i]

    if key_word not in element:
        search_list.remove(element)

print(search_list)
