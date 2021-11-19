class Student():
    def __init__(self,firstn,lastn,M,P,C):
        self.firstname = firstn
        self.lastname = lastn
        self.maths = M
        self.physics = P
        self.chem = C
    def percent(self):
        self.percent= (self.maths + self.physics + self.chem)/300*100
        return self.percent
        
Student1 = Student("Rahul","Shaik",91,97,91)
Student2 = Student("Mehak","Singh",90,96,92)
print(Student1.percent())

