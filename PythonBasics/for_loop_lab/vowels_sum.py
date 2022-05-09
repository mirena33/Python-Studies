text = input()
counter = 0

for i in text:
    if i == "a":
        counter += 1
    elif i == "e":
        counter += 2
    elif i == "i":
        counter += 3
    elif i == "o":
        counter += 4
    elif i == "u":
        counter += 5

print(counter)
