budget = int(input())
data = input()

while data != "End":
    product_price = int(data)
    budget -= product_price
    if budget < 0:
        print("You went in overdraft!")
        break

    data = input()
else:
    print("You bought everything needed.")
