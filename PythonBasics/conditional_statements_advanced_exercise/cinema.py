screening_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns
profit = 0

if screening_type == "Premiere":
    profit = seats * 12.00
elif screening_type == "Normal":
    profit = seats * 7.50
elif screening_type == "Discount":
    profit = seats * 5.00

print(f"{profit:.2f} leva")

