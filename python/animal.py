class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return f"generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return f"Woof"

if __name__ == "__main__":
    tucker = Dog("Golden Doodle")
    print(tucker.make_sound())
    print(tucker.species)
