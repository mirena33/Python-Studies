energy = int(input())
won_battles_cnt = 0

while True:
    action = input()

    if action == "End of battle":
        print(f"Won battles: {won_battles_cnt}. Energy left: {energy}")
        break

    distance = int(action)

    if energy >= distance:
        energy -= distance
        won_battles_cnt += 1

        if won_battles_cnt % 3 == 0:
            energy += won_battles_cnt

    else:
        print(f"Not enough energy! Game ends with {won_battles_cnt} won battles and {energy} energy")
        break
