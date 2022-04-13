mackerel_price_per_kilo = float(input())
sprat_price_per_kilo = float(input())
bonito_kilos = float(input())
scad_kilos = float(input())
mussels_kilos = float(input())

bonito_price_per_kilo = mackerel_price_per_kilo * 0.6 + mackerel_price_per_kilo
bonito_price = bonito_kilos * bonito_price_per_kilo

scad_price_per_kilo = sprat_price_per_kilo * 0.8 + sprat_price_per_kilo
scad_price = scad_kilos * scad_price_per_kilo

mussels_price = mussels_kilos * 7.50

total_price = bonito_price + scad_price + mussels_price
print("{:.2f}".format(round(total_price, 2)))



