def is_perfect(num):
    sum_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_divisors += divisor

    if num == sum_divisors:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_perfect(number))
