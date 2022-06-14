data = int(input())
positives = list()
negatives = list()

for i in range(data):
    curr_number = int(input())

    if curr_number < 0:
        negatives.append(curr_number)
    else:
        positives.append(curr_number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
