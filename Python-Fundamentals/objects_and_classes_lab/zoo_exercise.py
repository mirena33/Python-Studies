class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""

        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"

        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"

        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


name_of_the_zoo = input()
lines_cnt = int(input())

zoo = Zoo(name_of_the_zoo)

for i in range(lines_cnt):
    data = input().split(" ")
    species = data[0]
    name = data[1]
    zoo.add_animal(species, name)

chosen_species = input()
print(zoo.get_info(chosen_species))
