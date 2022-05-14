tabs_cnt = int(input())
salary = int(input())
fine = 0

for i in range(0, tabs_cnt):
    current_tab = input()

    if current_tab == "Facebook":
        fine += 150
    elif current_tab == "Instagram":
        fine += 100
    elif current_tab == "Reddit":
        fine += 50

if salary <= fine:
    print("You have lost your salary.")
else:
    print(salary - fine)
