def calculations(action, first_num, second_num):
    result = 0

    if action == "multiply":
        result = first_num * second_num
    elif action == "divide":
        result = first_num // second_num
    elif action == "add":
        result = first_num + second_num
    elif action == "subtract":
        result = first_num - second_num

    return result


data_action = input()
first_number = int(input())
second_number = int(input())
print(calculations(data_action, first_number, second_number))
