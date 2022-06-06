input_string = input()
index_list = []

for i in range(len(input_string)):
    if input_string[i].isupper():
        index_list.append(i)

print(index_list)
