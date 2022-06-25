def check_chairs(rooms_cnt):
    total_free_chairs = 0
    needed_chairs = 0

    for number_of_room in range(1, rooms_cnt + 1):
        room_info = input().split(" ")
        free_chairs = room_info[0]
        visitors = int(room_info[1])
        difference = len(free_chairs) - visitors

        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")

    return total_free_chairs, needed_chairs


number_of_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(number_of_rooms)

if total_free_chairs >= needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
