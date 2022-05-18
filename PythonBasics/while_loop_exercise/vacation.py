vacation_price = float(input())
saved_money = float(input())

days_counter = 0
spending_days = 0

while saved_money < vacation_price:
    action = input()
    amount = float(input())

    days_counter += 1

    if action == "spend":
        saved_money -= amount
        if saved_money < 0:
            saved_money = 0

        spending_days += 1

    elif action == "save":
        saved_money += amount
        spending_days = 0

    if spending_days == 5:
        print(f"You can't save the money.\n{days_counter}")
        break

else:
    print(f"You saved the money for {days_counter} days.")
