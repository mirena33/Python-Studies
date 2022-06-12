n = int(input())
left_bracket_counter = 0
right_bracket_counter = 0
is_balanced = True

for i in range(n):
    data_input = input()

    if data_input == "(":
        left_bracket_counter += 1
    elif data_input == ")":
        right_bracket_counter += 1

        if left_bracket_counter - right_bracket_counter != 0:
            is_balanced = False

if left_bracket_counter == right_bracket_counter and is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
