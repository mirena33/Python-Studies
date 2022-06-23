def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


first_number = int(input())
second_number = int(input())
print(f"{factorial(first_number) / factorial(second_number):.2f}")

# Another solution with for loop:

# def factorial(num):
#     for fact in range(1, num):
#         num *= fact
#     return num
