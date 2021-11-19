Maths = int(input("Enter the marks: "))
Physics = int(input("Enter the marks :  "))
Chem = int(input("Enter the marks : "))

if(Maths<33 or Physics<33 or Chem<33):
    print("You are Fail")

elif(Maths+Physics+Chem)/3 <40 :
    print("You are fail due to total percentage less than 40")
else: 
    print("Congrats! You are passed")    