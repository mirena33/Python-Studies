player_name = input()
max_player_points = 0
winner_name = ""

while player_name != "Stop":
    current_player_points = 0

    for letter in player_name:
        number = int(input())

        if chr(number) == letter:
            current_player_points += 10
        else:
            current_player_points += 2

        if current_player_points >= max_player_points:
            max_player_points = current_player_points
            winner_name = player_name

    player_name = input()

print(f"The winner is {winner_name} with {max_player_points} points!")
