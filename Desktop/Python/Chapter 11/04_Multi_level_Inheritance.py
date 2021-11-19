class Person():
    country = "India"
    def takeBreath(self):
        print("I am breathing")

class Employee():
    company = "Honda"

    def getSalary(self):
       print(f"The Salary is {self.getSalary}")

    def takeBreath(self):
        print(f"I am happily breathing")


class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No Salary for Programmers")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()