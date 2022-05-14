tournaments_cnt = int(input())
rank_list_points = int(input())
initial_points = rank_list_points

winner_cnt = 0

for i in range(0, tournaments_cnt):
    tournament_stage = input()

    if tournament_stage == "W":
        rank_list_points += 2000
        winner_cnt += 1
    elif tournament_stage == "F":
        rank_list_points += 1200
    elif tournament_stage == "SF":
        rank_list_points += 720

print(f"Final points: {rank_list_points}")
print(f"Average points: {(rank_list_points - initial_points) // tournaments_cnt}")
print(f"{winner_cnt / tournaments_cnt * 100:.2f}%")
