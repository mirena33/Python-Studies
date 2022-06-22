def type_of_grade(grade):
    grade_type = None

    if grade <= 2.99:
        grade_type = "Fail"
    elif grade <= 3.49:
        grade_type = "Poor"
    elif grade <= 4.49:
        grade_type = "Good"
    elif grade <= 5.49:
        grade_type = "Very Good"
    elif grade <= 6.00:
        grade_type = "Excellent"

    return grade_type


score = float(input())
print(type_of_grade(score))
