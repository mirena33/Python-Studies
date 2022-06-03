data_input = input()

while data_input != "End":
    if data_input != "SoftUni":

        for ch in data_input:
            print(f"{ch * 2}", end="")

        print()
    data_input = input()
