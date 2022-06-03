n = int(input())
is_pure = True

for i in range(n):
    str_data = input()

    if "," in str_data or "." in str_data or "_" in str_data:
        print(f"{str_data} is not pure!")
    else:
        print(f"{str_data} is pure.")
