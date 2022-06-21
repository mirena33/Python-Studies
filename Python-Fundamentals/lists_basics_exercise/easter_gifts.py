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
            gifts_list[required_index] = gift

    elif command_name == "JustInCase":
        gifts_list[-1] = gift

    command = input()

while "None" in gifts_list:
    gifts_list.remove("None")

print(" ".join(gifts_list))
