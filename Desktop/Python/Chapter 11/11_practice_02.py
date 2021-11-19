class Animals():
    animaltype = "Mammal"


class Pets(Animals):
    petcolour = "white"

class dogs(Pets):
    @staticmethod
    def bark():
        print("BOow Bow")

d = dogs()
d.bark()
print(d.petcolour)
print(d.animaltype)

