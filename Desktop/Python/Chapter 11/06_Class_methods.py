class Employee():
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changeSalary(self,sal):
    #     self.__class__.salary = sal
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)

# A class method is method which is bound to the class and not the object of the class.
# You can change the class attribute.