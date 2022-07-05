class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        result = ""
        if self.owner is None and money >= self.price:
            self.owner = owner
            result = f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif money < self.price:
            result = "Sorry, not enough money"
        else:
            result = "Car already sold"

        return result

    def sell(self):
        if self.owner is None:
            return f"Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner is None:
            result = f"{self.model} {self.type} is on sale: {self.price}"
        else:
            result = f"{self.model} {self.type} is owned by: {self.owner}"
        return result
