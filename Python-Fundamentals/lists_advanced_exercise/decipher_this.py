messages = input().split(" ")
final_message = []

for message in messages:
    current_message = ""
    number = int("".join([d for d in message if d.isdigit()]))

    current_message += chr(number)
    message = message.replace(str(number), '')

    if len(message) >= 2:
        message = message[-1] + message[1:-1] + message[0]

    current_message += message
    final_message.append(current_message)

print(" ".join(final_message))
