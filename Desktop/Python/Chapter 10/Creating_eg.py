class Student():
    def __init__(self,smart,boring,topper):
        self.smart = smart
        self.boring = boring
        self.topper = topper

rahul = Student(100,10,"yes")
abhi = Student(70,60,"No")
print(rahul.smart)
print(rahul.topper)
print(abhi.topper)