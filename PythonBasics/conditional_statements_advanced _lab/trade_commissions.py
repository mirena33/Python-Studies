city = input()
profit_volume = float(input())
commission = 0
is_input_valid = True

if city == "Sofia":
    if 0 <= profit_volume <= 500:
        commission = profit_volume * 0.05
    elif 500 < profit_volume <= 1000:
        commission = profit_volume * 0.07
    elif 1000 < profit_volume <= 10000:
        commission = profit_volume * 0.08
    elif profit_volume > 10000:
        commission = profit_volume * 0.12
    else:
        is_input_valid = False

elif city == "Varna":
    if 0 <= profit_volume <= 500:
        commission = profit_volume * 0.045
    elif 500 < profit_volume <= 1000:
        commission = profit_volume * 0.075
    elif 1000 < profit_volume <= 10000:
        commission = profit_volume * 0.10
    elif profit_volume > 10000:
        commission = profit_volume * 0.13
    else:
        is_input_valid = False

elif city == "Plovdiv":
    if 0 <= profit_volume <= 500:
        commission = profit_volume * 0.055
    elif 500 < profit_volume <= 1000:
        commission = profit_volume * 0.08
    elif 1000 < profit_volume <= 10000:
        commission = profit_volume * 0.12
    elif profit_volume > 10000:
        commission = profit_volume * 0.145
    else:
        is_input_valid = False

else:
    is_input_valid = False

if is_input_valid:
    print(f"{commission:.2f}")
else:
    print("error")
