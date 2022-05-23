destination = input()
saved_money = 0

while destination != "End":
    budget = float(input())

    while True:
        amount = float(input())
        saved_money += amount

        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money = 0
            break

    destination = input()
