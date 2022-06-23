def define_data_type(value_type, value):
    if value_type == "int":
        return int(value) * 2
    elif value_type == "real":
        return f"{float(value) * 1.5:.2f}"
    elif value_type == "string":
        return f"${value}$"


input_type = input()
input_value = input()
print(define_data_type(input_type, input_value))
