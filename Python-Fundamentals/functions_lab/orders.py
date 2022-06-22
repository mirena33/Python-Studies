def order(product: str, quantity: int):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return price * quantity


product_name = input()
product_quantity = int(input())
print(f"{order(product_name, product_quantity):.2f}")
