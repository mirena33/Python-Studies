class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def name_of_attendees(self):
        return ", ".join(self.people)

    def count_of_attendees(self):
        return len(self.people)


party = Party()

while True:
    name = input()

    if name == "End":
        break

    party.invite(name)

print(f"Going: {party.name_of_attendees()}")
print(f"Total: {party.count_of_attendees()}")
