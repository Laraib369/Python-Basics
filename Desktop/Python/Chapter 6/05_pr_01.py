Num1 = input("Enter the first number : ")
Num2 = input("Enter the second number : ")
Num3 = input("Enter the third number : ")
Num4 = input("Enter the forth number : ")

if(Num1>Num4):
    f1 = Num1
else:
    f1 = Num4

if(Num2>Num3):
    f2 = Num2
else: 
    f2 = Num3

if(f1>f2):
    print("f1 is the greatest",f1)     
else:
    print("f2 is the greatest",f2)       