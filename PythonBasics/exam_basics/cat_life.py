breed = input()
gender = input()

human_years_life = 0
is_invalid = False

if breed == "British Shorthair":
    if gender == "m":
        human_years_life = 13
    elif gender == "f":
        human_years_life = 14

elif breed == "Siamese":
    if gender == "m":
        human_years_life = 15
    elif gender == "f":
        human_years_life = 16

elif breed == "Persian":
    if gender == "m":
        human_years_life = 14
    elif gender == "f":
        human_years_life = 15

elif breed == "Ragdoll":
    if gender == "m":
        human_years_life = 16
    elif gender == "f":
        human_years_life = 17

elif breed == "American Shorthair":
    if gender == "m":
        human_years_life = 12
    elif gender == "f":
        human_years_life = 13

elif breed == "Siberian":
    if gender == "m":
        human_years_life = 11
    elif gender == "f":
        human_years_life = 12

else:
    is_invalid = True
    print(f"{breed} is invalid cat!")

if not is_invalid:
    human_months_life = human_years_life * 12
    cat_months_life = human_months_life / 6

    print(f"{cat_months_life:g} cat months")
