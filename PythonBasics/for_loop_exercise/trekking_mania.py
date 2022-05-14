group_cnt = int(input())

total_people = 0
mussala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(0, group_cnt):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group < 6:
        mussala += people_in_group
    elif people_in_group < 13:
        montblanc += people_in_group
    elif people_in_group < 26:
        kilimanjaro += people_in_group
    elif people_in_group < 41:
        k2 += people_in_group
    else:
        everest += people_in_group

print(f"{mussala / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")
