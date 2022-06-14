a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

temp = a
a = b
b = temp

print("After:")
print(f"a = {a}")
print(f"b = {b}")

# Another solution:

# print("Before:")
# print(f"a = {a}")
# print(f"b = {b}")
#
# # a, b = b, a
#
# print("After:")
# print(f"a = {a}")
# print(f"b = {b}")
