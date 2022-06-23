def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0

    for i in number:
        digit = int(i)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


input_number = input()
odd_and_even_sum(input_number)
