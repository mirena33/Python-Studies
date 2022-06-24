office_mood = list(map(int, input().split(" ")))
improvement_factor = int(input())

office_happiness = [x * improvement_factor for x in office_mood]
average_happiness = sum(office_happiness) / len(office_happiness)
happy_employees = list(filter(lambda x: x >= average_happiness, office_happiness))

if len(happy_employees) >= len(office_mood) / 2:
    print(f"Score: {len(happy_employees)}/{len(office_mood)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(office_mood)}. Employees are not happy!")
