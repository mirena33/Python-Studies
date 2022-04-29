travel_price = float(input())
puzzles_cnt = int(input())
dolls_cnt = int(input())
bears_cnt = int(input())
minions_cnt = int(input())
trucks_cnt = int(input())

profit = puzzles_cnt * 2.60 + dolls_cnt * 3 + bears_cnt * 4.10 + minions_cnt * 8.20 + trucks_cnt * 2
toys_cnt = puzzles_cnt + dolls_cnt + bears_cnt + minions_cnt + trucks_cnt

if toys_cnt >= 50:
    profit -= profit * 0.25

profit -= profit * 0.1

if profit >= travel_price:
    print(f"Yes! {profit - travel_price:.2f} lv left.")
else:
    print(f"Not enough money! {travel_price - profit:.2f} lv needed.")
