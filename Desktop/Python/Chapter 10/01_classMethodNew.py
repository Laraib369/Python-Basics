class Rectangle():
    def __init__(self,c,l,w):
        self.color = c
        self.length = l
        self.width = w
    def area(self):
        self.area = (self.length*self.width)
        return self.area
    def perimeter(self):
        self.perimeter = 2*(self.length + self.width) 
        return self.perimeter
    def volume(self):
        self.volume = "2D shape"
        return self.volume


myRect1 = Rectangle("red",2,4)
print(myRect1.color)
print(myRect1.length)
myRect2 = Rectangle("blue",4,8)
print(myRect2.color)
print(f"Color of rect2 is {myRect2.color}")
print(myRect2.area())
print(myRect2.perimeter())
print(myRect2.volume())