student_name = input()
grade = 1
grades_sum = 0
failed_years = 0

while grade <= 12:
    current_mark = float(input())

    if current_mark < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue

    grade += 1
    grades_sum += current_mark
else:
    avg_grade = grades_sum / 12
    print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")
