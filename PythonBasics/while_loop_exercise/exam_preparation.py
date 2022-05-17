allowed_failed_marks_cnt = int(input())
failed_marks_counter = 0
marks_sum = 0
problems_cnt = 0
last_problem = ""
has_failed = True

while allowed_failed_marks_cnt > failed_marks_counter:
    problem_name = input()

    if problem_name == "Enough":
        has_failed = False
        break

    problem_mark = int(input())

    if problem_mark <= 4:
        failed_marks_counter += 1

    marks_sum += problem_mark
    problems_cnt += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {allowed_failed_marks_cnt} poor grades.")
else:
    print(f"Average score: {marks_sum / problems_cnt:.2f}")
    print(f"Number of problems: {problems_cnt}")
    print(f"Last problem: {last_problem}")
