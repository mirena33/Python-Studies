input_data = input()
total_steps = 0

while input_data != "Going home":
    steps = int(input_data)
    total_steps += steps

    if total_steps >= 10000:
        break

    input_data = input()

if input_data == "Going home":
    home_steps = int(input())
    total_steps += home_steps

if total_steps >= 10000:
    print(f"Goal reached! Good job!\n{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")
