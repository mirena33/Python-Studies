gifts_list = input().split(" ")
command = input()

while command != "No Money":
    command_list = command.split(" ")
    command_name = command_list[0]
    gift = command_list[1]

    if command_name == "OutOfStock":
        for index, item in enumerate(gifts_list):
            if gifts_list[index] == gift:
                gifts_list[index] = "None"

    elif command_name == "Required":
        required_index = int(command_list[2])

        if 0 <= required_index < len(gifts_list):
            gifts_list.remove(gifts_list[required_index])
            gifts_list.insert(required_index, gift)

    elif command_name == "JustInCase":
        gifts_list.pop()
        gifts_list.append(gift)

    command = input()

for element in gifts_list:
    if element == "None":
        gifts_list.remove(element)

print(" ".join(gifts_list))
