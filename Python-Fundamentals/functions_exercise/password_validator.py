def length_is_valid(string_password):
    if 6 <= len(string_password) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(string_password):
    # string.isalnum -> checks if string contains only chars or digits(no special symbols)
    if string_password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def is_more_than_two_digits(string_password):
    digit_cnt = 0
    for character in string_password:
        if character.isdigit():
            digit_cnt += 1
    if digit_cnt >= 2:
        return True

    print("Password must have at least 2 digits")
    return False


password = input()
validated = [length_is_valid(password), symbols_are_valid(password), is_more_than_two_digits(password)]

if all(validated):
    print("Password is valid")
