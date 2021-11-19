class Calculator():
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number **3}")
    def squareRoot(self):
        print(f"The squre root of {self.number} is {self.number **0.5}")

    @staticmethod
    def greet():
        print("***Goodmorning***")


a = Calculator(8)
a.greet()
a.square()
a.cube()
a.squareRoot()