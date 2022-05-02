budget = float(input())
season = input()
travel_location = ""
accommodation = ""

if budget <= 100:
    travel_location = "Bulgaria"

    if season == "summer":
        accommodation = "Camp"
        budget = budget * 0.3
    elif season == "winter":
        accommodation = "Hotel"
        budget = budget * 0.7

elif budget <= 1000:
    travel_location = "Balkans"

    if season == "summer":
        accommodation = "Camp"
        budget = budget * 0.4
    elif season == "winter":
        accommodation = "Hotel"
        budget = budget * 0.8

elif budget > 1000:
    travel_location = "Europe"
    accommodation = "Hotel"
    budget = budget * 0.9

print(f"Somewhere in {travel_location}")
print(f"{accommodation} - {budget:.2f}")
