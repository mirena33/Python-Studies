cake_width = int(input())
cake_length = int(input())
input_data = input()

cake_total_pieces = cake_width * cake_length

while input_data != "STOP":
    pieces = int(input_data)
    cake_total_pieces -= pieces

    if cake_total_pieces < 0:
        print(f"No more cake left! You need {abs(cake_total_pieces)} pieces more.")
        break
    input_data = input()
else:
    print(f"{cake_total_pieces} pieces are left.")
