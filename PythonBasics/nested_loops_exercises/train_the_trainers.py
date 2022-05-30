jury_cnt = int(input())
presentation = input()
total_jury_marks = 0
final_assessment = 0

while presentation != "Finish":
    grade_sum = 0
    for i in range(jury_cnt):
        current_grade = float(input())
        grade_sum += current_grade
        final_assessment += current_grade

    average_grade = grade_sum / jury_cnt
    total_jury_marks += jury_cnt

    print(f"{presentation} - {average_grade:.2f}.")

    presentation = input()

print(f"Student's final assessment is {final_assessment / total_jury_marks:.2f}.")
