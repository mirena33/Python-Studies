budget = float(input())
video_card_cnt = int(input())
processor_cnt = int(input())
RAM_memory_cnt = int(input())

video_card_price = video_card_cnt * 250
processor_price = processor_cnt * (video_card_price * 0.35)
RAM_memory_price = RAM_memory_cnt * (video_card_price * 0.1)
total_price = video_card_price + processor_price + RAM_memory_price

if video_card_cnt > processor_cnt:
    total_price -= total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")

