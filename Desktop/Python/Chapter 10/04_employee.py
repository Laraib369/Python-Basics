# Class Attributes: Attributes that are same for all employees.

class Employee():
    company = "Google"

laraib = Employee()
harry = Employee()

Employee.company = "YouTube"

print(laraib.company)
print(harry.company)

# Instance Attributes: Attributes that are diffrent for employees.eg.number,name

laraib.salary =2000
harry.salary = 4000

print(laraib.salary)
print(harry.salary)