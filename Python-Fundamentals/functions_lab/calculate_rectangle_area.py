def rectangle_area(width, height):
    return width * height


input_width = int(input())
input_height = int(input())
print(rectangle_area(input_width, input_height))

# Another solution:
# result = lambda w, h: w * h
# print(result(input_width, input_height))
