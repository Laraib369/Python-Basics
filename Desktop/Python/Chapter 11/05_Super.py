class Person():
    country = "India"
    def takeBreath(self):
        print("I am Breathing")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"The salary is {self.getSalary}")

    def takeBreath(self):
        print(f"I am happily breathing")

class Programmer (Employee):
    company = "Fiverr"
    def getSalary(self):
        print("No salary for programmers")

    def takeBreath(self):
        super().takeBreath()
        print(f"I am a programmer so i'm breathing c++")


p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()


