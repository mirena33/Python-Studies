start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
combination_counter = 0
flag = False

for i in range(start_interval, end_interval + 1):
    for j in range(start_interval, end_interval + 1):
        combination_counter += 1
        if i + j == magic_number:
            print(f"Combination N:{combination_counter}", end=" ")
            print(f"({i} + {j} = {magic_number})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
