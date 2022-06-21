factor = int(input())
count = int(input())
multiples_list = list()
element = 0

for i in range(1, count + 1):
    element = i * factor
    multiples_list.append(element)

print(multiples_list)
