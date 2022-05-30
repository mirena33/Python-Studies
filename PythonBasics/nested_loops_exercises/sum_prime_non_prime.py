data = input()
prime_sum = 0
non_prime_sum = 0

while data != "stop":
    current_number = int(data)
    if current_number < 0:
        print("Number is negative.")
        data = input()
        continue

    if current_number == 1 or current_number == 0:
        non_prime_sum += current_number
    else:
        is_prime = True
        # improvement: for div in range(2, ceil(current_number / 2) + 1):
                                         # ceil(sqrt(current_number)) + 1
        for div in range(2, current_number):
            if current_number % div == 0:
                is_prime = False
                break

        if is_prime:
            prime_sum += current_number
        else:
            non_prime_sum += current_number

    data = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
