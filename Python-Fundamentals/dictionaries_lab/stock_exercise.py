data = input().split(" ")
inventory = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
products_to_search = input().split(" ")

for product in products_to_search:
    if product not in inventory:
        print(f"Sorry, we don't have {product}")
    else:
        print(f"We have {inventory[product]} of {product} left")
