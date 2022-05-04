month = input()
nights_cnt = int(input())
apartment_total_price = 0
studio_total_price = 0
apartment_price_per_night = 0
studio_price_per_night = 0


if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65

    if nights_cnt > 14:
        studio_price_per_night -= studio_price_per_night * 0.3
    elif nights_cnt > 7:
        studio_price_per_night -= studio_price_per_night * 0.05

elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70

    if nights_cnt > 14:
        studio_price_per_night -= studio_price_per_night * 0.2

elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights_cnt > 14:
    apartment_price_per_night -= apartment_price_per_night * 0.1

studio_total_price = studio_price_per_night * nights_cnt
apartment_total_price = apartment_price_per_night * nights_cnt

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
