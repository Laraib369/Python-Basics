class Employee():
    company = "Google"
    salary = "1000"

laraib = Employee()
harry = Employee()

Employee.company = "YouTube"

print(laraib.company)
print(harry.company)


# laraib.salary =2000
# harry.salary = 4000

print(laraib.salary)
print(harry.salary)