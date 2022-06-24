def palindrome_filter(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
palindrome = input()
palindrome_list = [w for w in words if palindrome_filter(w)]

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")
