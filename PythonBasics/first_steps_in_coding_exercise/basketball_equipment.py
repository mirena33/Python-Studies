basketball_fee = int(input())

shoes = basketball_fee - basketball_fee * 0.4
jumpsuit = shoes - shoes * 0.2
ball = jumpsuit * 0.25
accessories = ball * 0.2

total_basketball_fees = basketball_fee + shoes + jumpsuit + ball + accessories
print(total_basketball_fees)


