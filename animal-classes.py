class Animal():
    def __init__(self, age):
        self.age = age
    def isBaby(self):
        if self.age < 1:
            return True
        else:
            return False

class Dogs(Animal):
    def __init__(self, colour, age):
        self.colour = colour
        Animal.__init__(self, age)

def test_animal_class():
    fox = Animal(12)
    print("Object fox should return 12 for age\n  Result: {}".format(fox.age))
    fox.age = 1
    print("Object fox should return 1 for age\n  Result: {}".format(fox.age))
    print("Object fox should return False for age\n  Result: {}".format(fox.isBaby()))

def test_dog_subclass():
    dog = Dogs("Red", 12)
    print("Object dog should return 12 for age\n  Result: {}".format(fox.age))

if __name__ == "__main__":
    test_animal_class()
    test_dog_subclass()