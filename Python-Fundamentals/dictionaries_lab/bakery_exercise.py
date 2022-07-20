data = input().split(" ")
products_dict = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i + 1])
    products_dict[key] = value

print(products_dict)

# Another solution with Comprehension:
# products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
# print(products_dict)
