number = int(input())
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("True")
else:
    print("False")
