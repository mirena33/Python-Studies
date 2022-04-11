deposit_sum = float(input())
months = int(input())
yearly_interest = float(input()) / 100

month_gain = (deposit_sum * yearly_interest) / 12
final_sum = deposit_sum + (months * month_gain)

print(final_sum)



