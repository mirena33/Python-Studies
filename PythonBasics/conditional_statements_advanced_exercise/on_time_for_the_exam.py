exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total_time = exam_hour * 60 + exam_minute
arrival_total_time = arrival_hour * 60 + arrival_minute
time_difference = abs(exam_total_time - arrival_total_time)

if arrival_total_time > exam_total_time:
    print("Late")
    if time_difference >= 60:
        hours_late = time_difference // 60
        minutes_late = time_difference % 60
        print(f"{hours_late}:{minutes_late:02d} hours after the start")
    else:
        print(f"{time_difference} minutes after the start")

elif arrival_total_time <= exam_total_time and time_difference <= 30:
    print("On time")
    if time_difference > 0:
        print(f"{time_difference} minutes before the start")

else:
    print("Early")
    if time_difference >= 60:
        hours_early = time_difference // 60
        minutes_early = time_difference % 60
        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f"{time_difference} minutes before the start")
