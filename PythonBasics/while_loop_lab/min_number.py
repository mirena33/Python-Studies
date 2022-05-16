import sys

data = input()
min_number = sys.maxsize

while data != "Stop":
    current_number = int(data)
    if current_number < min_number:
        min_number = current_number
    data = input()

print(min_number)
