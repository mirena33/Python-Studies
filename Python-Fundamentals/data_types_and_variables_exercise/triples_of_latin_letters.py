letters = int(input())

for first_letter in range(97, 97 + letters):
    for second_letter in range(97, 97 + letters):
        for third_letter in range(97, 97 + letters):
            triple = chr(first_letter) + chr(second_letter) + chr(third_letter)
            print(triple)
