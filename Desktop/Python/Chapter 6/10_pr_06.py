Marks = int(input("Enter the marks :\n"))

if (Marks>=90):
    grade = "Exc"
elif(Marks>=80):
    grade ="Good"
elif(Marks>=70):
    grade = "B"
elif(Marks>=60):
    grade = "C"
elif(Marks>=50):
    grade = "D " 
else:
    grade = "Fail"

print("Your grade is: ",grade)
