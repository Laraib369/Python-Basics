class Complex():
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i


    def __add__(self,c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)

    def __str__(self):
      return  f"{self.real} + {self.imaginary}i"

    def __mul__(self,c):
        mulReal = self.real *c.real  - self.imaginary* c.imaginary
        mulimaginary = self.real * c.imaginary + self.imaginary * c.real
        return Complex(mulReal,mulimaginary)



c1 = Complex(1,4)
c2 = Complex(3,4)
add = c1 + c2
print(add)
mul = c1 * c2
print(mul)