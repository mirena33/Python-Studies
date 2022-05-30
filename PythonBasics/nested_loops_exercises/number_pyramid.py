n = int(input())

counter = 1
is_pyramid_rdy = False

for row in range(1, n + 1):
    for col in range(0, row):
        print(f"{counter}", end=" ")
        counter += 1

        if counter > n:
            is_pyramid_rdy = True
            break

    if is_pyramid_rdy:
        break

    print()
