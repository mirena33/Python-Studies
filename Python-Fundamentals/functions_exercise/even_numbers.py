numbers = [int(s) for s in input().split(" ")]
numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)

# Another solution:
# numbers = [int(s) for s in input().split(" ") if int(s) % 2 == 0]
# print(numbers)
