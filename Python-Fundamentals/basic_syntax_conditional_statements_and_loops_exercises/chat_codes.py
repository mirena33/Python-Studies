n = int(input())

for i in range(n):
    current_code = int(input())

    if current_code == 88:
        print("Hello")
    elif current_code == 86:
        print("How are you?")
    elif current_code < 88 and current_code != 88 and current_code != 86:
        print("GREAT!")
    elif current_code > 88:
        print("Bye.")
