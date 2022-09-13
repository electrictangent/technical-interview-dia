class Animal():
    def __init__(self, age):
        self.age = age
    def isBaby(self):
        if self.age < 1:
            return True
        else:
            return False

def test_animal_class():
    fox = Animal(12)
    print("Object fox should return 12 for age\n  Result: {}".format(fox.age))
    fox.age = 1
    print("Object fox should return 1 for age\n  Result: {}".format(fox.age))
    print("Object fox should return False for age\n  Result: {}".format(fox.isBaby()))


if __name__ == "__main__":
    test_animal_class()