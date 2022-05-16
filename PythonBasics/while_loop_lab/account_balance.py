money_sum = 0

while True:
    data = input()

    if data == "NoMoreMoney":
        break

    amount = float(data)

    if amount < 0:
        print("Invalid operation!")
        break
    else:
        money_sum += amount
        print(f"Increase: {amount:.2f}")

print(f"Total: {money_sum:.2f}")
