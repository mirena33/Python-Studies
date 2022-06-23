def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False


numbers = input().split(", ")

for num in numbers:
    if is_palindrome(num):
        print("True")
    else:
        print("False")
