budget = int(input())
season = input()
fishers_cnt = int(input())
boat_rent = 0
discount = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishers_cnt <= 6:
    discount = 0.1
elif fishers_cnt <= 11:
    discount = 0.15
elif fishers_cnt >= 12:
    discount = 0.25

boat_rent -= boat_rent * discount

if fishers_cnt % 2 == 0 and season != "Autumn":
    boat_rent -= boat_rent * 0.05

if budget >= boat_rent:
    print(f"Yes! You have {budget - boat_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_rent - budget:.2f} leva.")
