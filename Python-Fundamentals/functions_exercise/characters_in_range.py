def chars_in_range(first, second):
    collected_chars = []
    for symbol in range(ord(first) + 1, ord(second)):
        collected_chars.append(chr(symbol))

    return " ".join(collected_chars)


first_char = input()
second_char = input()
result = chars_in_range(first_char, second_char)
print(result)
