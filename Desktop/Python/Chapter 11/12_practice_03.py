class Employee():
    Salary = 1000
    Increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.Salary * self.Increment 
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.Increment = sai /self.Salary

e = Employee()
print(e.Salary)
print(e.salaryAfterIncrement)
e.salaryAfterIncrement =2000
print(e.Increment)