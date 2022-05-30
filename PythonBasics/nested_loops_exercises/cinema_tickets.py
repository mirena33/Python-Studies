movie_name = input()
standard_tickets = 0
kid_tickets = 0
student_tickets = 0

while movie_name != 'Finish':
    free_places = int(input())
    current_movie_tickets = 0
    ticket_type = ""

    while free_places > current_movie_tickets and ticket_type != 'End':
        ticket_type = input()

        if ticket_type == 'standard':
            standard_tickets += 1
            current_movie_tickets += 1
        elif ticket_type == 'student':
            student_tickets += 1
            current_movie_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
            current_movie_tickets += 1

    current_movie_percent = (current_movie_tickets / free_places) * 100
    print(f"{movie_name} - {current_movie_percent:.2f}% full.")
    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets

avr_kid_percent = (kid_tickets / total_tickets) * 100
avr_student_percent = (student_tickets / total_tickets) * 100
avr_standard_percent = (standard_tickets / total_tickets) * 100
print(f'Total tickets: {total_tickets}')
print(f"{avr_student_percent:.2f}% student tickets.")
print(f"{avr_standard_percent:.2f}% standard tickets.")
print(f"{avr_kid_percent:.2f}% kids tickets.")
