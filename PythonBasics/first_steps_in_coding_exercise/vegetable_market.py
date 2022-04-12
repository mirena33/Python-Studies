vegetables_per_kilo = float(input())
fruit_per_kilo = float(input())
total_kg_vegetables = int(input())
total_kg_fruit = int(input())

total_cost_in_leva = vegetables_per_kilo * total_kg_vegetables + fruit_per_kilo * total_kg_fruit
total_cost_in_euro = total_cost_in_leva / 1.94
print("{:.2f}".format(total_cost_in_euro))



