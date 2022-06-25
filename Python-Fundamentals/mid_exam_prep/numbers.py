numbers = list(map(int, input().split(" ")))
avg_value = sum(numbers) / len(numbers)

result = [num for num in sorted(numbers, reverse=True) if num > avg_value]
print(result)

if len(result) != 0:
    print(*result[:5], sep=" ")
else:
    print("No")
