pounds = int(input())
dollars = pounds * 1.31

print(f"{dollars:.3f}")

# Another solution:

# from forex_python.converter import CurrencyRates
#
# amount = int(input("Enter an amount in pounds: "))
# c = CurrencyRates()
# current_rate = c.get_rate("GBP", "USD")
# result = current_rate * amount
# print(f"Your cash in dollars is: {result:.3f}")
