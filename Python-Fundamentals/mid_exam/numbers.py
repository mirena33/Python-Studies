numbers = list(map(int, input().split(" ")))

while True:
    data = input().split(" ")
    if data[0] == "Finish":
        print(*numbers, sep=" ")
        break

    command = data[0]
    value = int(data[1])

    if command == "Add":
        numbers.append(value)

    elif command == "Remove":
        numbers.remove(value)

    elif command == "Replace":
        replacement = int(data[2])

        if value in numbers:
            value_index = numbers.index(value)
            numbers[value_index] = replacement

    elif command == "Collapse":
        numbers = list(filter(lambda x: x >= value, numbers))
