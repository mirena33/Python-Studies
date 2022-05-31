max_goals = 0
best_player = ""
hat_trick = False

player_name = input()

while player_name != "END":
    player_goals = int(input())

    if player_goals > max_goals:
        max_goals = player_goals
        best_player = player_name

    if player_goals >= 3:
        hat_trick = True

    if player_goals >= 10:
        break

    player_name = input()

if hat_trick:
    print(f"{best_player} is the best player!\nHe has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!\nHe has scored {max_goals} goals.")
