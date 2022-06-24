wagons_cnt = int(input())
wagons = [0] * wagons_cnt

command = input()
while command != "End":
    data = command.split(" ")
    current_command = data[0]

    if current_command == "add":
        people = int(data[1])
        wagons[-1] += people

    elif current_command == "insert":
        wagon_index = int(data[1])
        people = int(data[2])
        wagons[wagon_index] += people

    elif current_command == "leave":
        wagon_index = int(data[1])
        people = int(data[2])
        wagons[wagon_index] -= people

    command = input()

print(wagons)
