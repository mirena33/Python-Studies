products = {}

while True:
    command = input()
    if command == 'statistics':
        break

    command = command.split(': ')
    product = command[0]
    quantity = int(command[1])

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

print('Products in stock:')
product_representation = [f'- {item}: {str(products[item])}' for item in products]
print('\n'.join(product_representation))
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
