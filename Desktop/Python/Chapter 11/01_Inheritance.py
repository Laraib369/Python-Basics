class Employee:
    company = "Google"
  

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    language = "python"

    def getlanguage(self):
        print(f"The language is {self.language}")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)