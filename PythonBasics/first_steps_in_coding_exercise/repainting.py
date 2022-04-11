nylon_in_sqr_meters = int(input())
paint_in_litres = int(input())
thinner_in_litres = int(input())
work_hours = int(input())

nylon_price = (nylon_in_sqr_meters + 2) * 1.50
paint_price = (paint_in_litres + paint_in_litres * 0.1) * 14.50
thinner_price = thinner_in_litres * 5
bags_price = 0.40

materials_price = nylon_price + paint_price + thinner_price + bags_price
workers_price = (materials_price * 0.3) * work_hours
print(materials_price + workers_price)
