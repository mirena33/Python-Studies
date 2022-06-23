def sum_numbers(first, second):
    return first + second


def subtract(sum_of_numbers, third):
    return sum_of_numbers - third


def add_and_subtract(first, second, third):
    return print(subtract(sum_numbers(first, second), third))


first_number = int(input())
second_number = int(input())
third_number = int(input())
add_and_subtract(first_number, second_number, third_number)
