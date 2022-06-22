def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result


numbers = list(map(float, input().split(" ")))
print(abs_numbers(numbers))
