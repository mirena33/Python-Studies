width = int(input())
length = int(input())
height = int(input())
data = input()

available_space = width * length * height
needed_space = 0

while data != "Done":
    boxes_cnt = int(data)
    needed_space += boxes_cnt

    if needed_space >= available_space:
        break

    data = input()

if available_space >= needed_space:
    print(f"{available_space - needed_space} Cubic meters left.")
else:
    print(f"No more free space! You need {needed_space - available_space} Cubic meters more.")
