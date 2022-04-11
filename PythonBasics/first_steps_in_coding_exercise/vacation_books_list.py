total_book_pages_cnt = int(input())
pages_per_hour = int(input())
days_to_read_the_book = int(input())

total_hours_to_read_book = total_book_pages_cnt / pages_per_hour
hours_to_read_per_day = round(total_hours_to_read_book / days_to_read_the_book)

print(hours_to_read_per_day)

