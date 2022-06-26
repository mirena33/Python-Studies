needed_experience = float(input())
battles_cnt = int(input())
gained_experience = 0

for i in range(1, battles_cnt + 1):
    battle_exp = float(input())

    if i % 3 == 0:
        battle_exp += battle_exp * 0.15

    if i % 5 == 0:
        battle_exp -= battle_exp * 0.1

    if i % 15 == 0:
        battle_exp += battle_exp * 0.05

    gained_experience += battle_exp

    if gained_experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {i} battles.")
        break
else:
    print(
        f"Player was not able to collect the needed experience, {needed_experience - gained_experience:.2f} more needed.")
