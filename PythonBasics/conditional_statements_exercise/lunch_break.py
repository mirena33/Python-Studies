from math import ceil

series = input()
episode_length_minutes = int(input())
break_minutes = int(input())

lunch_minutes = break_minutes * 0.125
relax_minutes = break_minutes * 0.25
time_left = break_minutes - (lunch_minutes + relax_minutes)

if time_left >= episode_length_minutes:
    print(f"You have enough time to watch {series}"
          f" and left with {ceil(time_left - episode_length_minutes)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series},"
          f" you need {ceil(episode_length_minutes - time_left)} more minutes.")
