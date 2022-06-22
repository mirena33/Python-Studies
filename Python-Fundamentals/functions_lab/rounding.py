numbers = list(map(float, input().split(" ")))
numbers = list(map(lambda x: round(x), numbers))
print(numbers)

# Another solution:
# print(list(map(lambda x: round(float(x)), input().split(" "))))
