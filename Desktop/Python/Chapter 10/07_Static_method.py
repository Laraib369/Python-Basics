class Employee():
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")

    @staticmethod
    def greet():
        print("Goodmorning,Sir")

harry = Employee()
harry.greet()
harry.getSalary()
# Employee.getSalary(harry)