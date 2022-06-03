event = input()
needed_coffee = 0

while event != "END":
    if event in ["coding", "dog", "cat", "movie"]:
        needed_coffee += 1
    elif event in ["CODING", "DOG", "CAT", "MOVIE"]:
        needed_coffee += 2

    event = input()

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)
