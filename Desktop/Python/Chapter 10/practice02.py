class Calculator():
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The square of the number {self.number} is {self.number ** 2}")

    def cube(self):
        print(f"The cube of the number {self.number} is {self.number ** 3}")
    
    def root(self):
        print(f"The square root of the  number {self.number} is {self.number ** 0.5}")

a = Calculator(2)
a.square()
a.cube()
a.root()
