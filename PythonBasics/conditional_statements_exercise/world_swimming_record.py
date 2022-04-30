record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

total_time = distance_in_meters * time_in_seconds_per_meter
added_time = (distance_in_meters // 15) * 12.5
total_time += added_time

if total_time >= record_in_seconds:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")


