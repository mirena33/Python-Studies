students_dict = {}
data = input()

while ":" in data:
    info = data.split(":")
    name = info[0]
    id = info[1]
    course = info[2]

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][id] = name
    data = input()

course = " ".join(data.split("_"))
for key, value in students_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")
