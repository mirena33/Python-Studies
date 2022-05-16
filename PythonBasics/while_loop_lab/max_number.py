import sys

data = input()
max_number = -sys.maxsize

while data != "Stop":
    current_number = int(data)
    if current_number > max_number:
        max_number = current_number
    data = input()

print(max_number)
