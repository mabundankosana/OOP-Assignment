
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Fish(Animal):
    def move(self):
        return "Swimming 🐟"


class Bird(Animal):
    def move(self):
        return "Flying ✈️"

class Cat(Animal):
    def move(self):
        return "Walking 🐾"


fish = Fish()
bird = Bird()
cat = Cat()


animals = [fish, bird, cat]
for animal in animals:
    print(animal.move())
