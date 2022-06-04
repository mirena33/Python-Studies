data_input = input()
kids_cnt = 0
adults_cnt = 0

while data_input != "Christmas":
    age = int(data_input)

    if age <= 16:
        kids_cnt += 1
    else:
        adults_cnt += 1

    data_input = input()

toys_money = kids_cnt * 5
sweaters_money = adults_cnt * 15

print(f"Number of adults: {adults_cnt}")
print(f"Number of kids: {kids_cnt}")
print(f"Money for toys: {toys_money}")
print(f"Money for sweaters: {sweaters_money}")
