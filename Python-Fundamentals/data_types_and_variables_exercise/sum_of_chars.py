number_of_chars = int(input())
chars_sum = 0

for i in range(number_of_chars):
    char = input()
    chars_sum += ord(char)

print(f"The sum equals: {chars_sum}")
