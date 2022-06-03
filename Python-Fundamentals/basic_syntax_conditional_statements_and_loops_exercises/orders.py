n = int(input())
total_price = 0

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())

    if (0.01 > price_per_capsule or price_per_capsule > 100.00) or (1 > days or days > 31) \
            or (1 > capsule_needed_per_day or capsule_needed_per_day > 2000):
        continue

    current_order_price = (capsule_needed_per_day * days) * price_per_capsule
    total_price += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")

print(f"Total: ${total_price:.2f}")
