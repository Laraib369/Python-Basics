class Employee():
    company = "Bharat Gas"
    salary = 5600
    salaryBonus = 500
    
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus


    @totalSalary.setter
    def totalSalary(self,Val):
        self.salaryBonus =Val - self.salary
e = Employee()
print(e.totalSalary)

e.totalSalary=5800
print(e.salaryBonus)