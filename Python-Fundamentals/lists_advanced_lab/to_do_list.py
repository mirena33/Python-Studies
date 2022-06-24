tasks = []
command = input().split("-")

while command[0] != "End":
    priority = int(command[0])
    task = command[1]
    tasks.append((priority, task))

    command = input().split("-")

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
