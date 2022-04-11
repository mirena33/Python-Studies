pens_cnt = int(input())
markers_cnt = int(input())
detergent_litres = int(input())
discount_percent = int(input()) / 100

total_sum = pens_cnt * 5.80 + markers_cnt * 7.20 + detergent_litres * 1.20
total_sum_with_discount = total_sum - (total_sum * discount_percent)

print(total_sum_with_discount)
