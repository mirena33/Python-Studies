budget = float(input())
flour_price = float(input())

breads_cnt = 0
coloured_eggs_cnt = 0
eggs_price = flour_price * 0.75
milk_price = flour_price + flour_price * 0.25
bread_price = flour_price + eggs_price + milk_price * 0.25

while budget >= bread_price:
    breads_cnt += 1
    coloured_eggs_cnt += 3
    if breads_cnt % 3 == 0:
        coloured_eggs_cnt -= breads_cnt - 2
    budget -= bread_price

print(f"You made {breads_cnt} loaves of Easter bread!"
      f" Now you have {coloured_eggs_cnt} eggs and {budget:.2f}BGN left.")
