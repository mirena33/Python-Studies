people = int(input())
lift = list(map(int, input().split(" ")))

for i in range(len(lift)):
    wagon_space = int(lift[i])
    needed_space = 4 - wagon_space

    if people < needed_space:
        lift[i] += people
        print(f"The lift has empty spots!")
        print(*lift, sep=" ")
        break
    else:
        people -= needed_space
        lift[i] += needed_space
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")
        print(*lift, sep=" ")
    elif people == 0:
        print(*lift, sep=" ")
