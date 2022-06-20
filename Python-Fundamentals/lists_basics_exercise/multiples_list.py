factor = int(input())
count = int(input())
multiples_list = list()
element = 0

for i in range(count):
    element += factor
    multiples_list.append(element)


multiples_list.sort()
print(multiples_list)
