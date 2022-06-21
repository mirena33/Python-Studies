input_data = input().split(", ")

for digit in input_data:
    if digit == "0":
        input_data.remove(digit)
        input_data.append(digit)

numbers_integers = list()
for num in input_data:
    numbers_integers.append(int(num))

print(numbers_integers)
