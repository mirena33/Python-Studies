def repeat_string(string, cnt):
    return string * cnt


input_string = input()
counter = int(input())
print(repeat_string(input_string, counter))

# Another solution:
# result = lambda a, b: a * b
# input_string = input()
# counter = int(input())
# print(result(input_string, counter))
