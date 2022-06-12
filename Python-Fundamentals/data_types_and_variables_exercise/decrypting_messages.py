key = int(input())
lines_input = int(input())
message = ""

for i in range(lines_input):
    curr_char = input()
    message += chr(ord(curr_char) + key)

print(message)
