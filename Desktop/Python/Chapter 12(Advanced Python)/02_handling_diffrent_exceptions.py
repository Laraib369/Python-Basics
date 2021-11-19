
try:
    a = input("Enter the number : ")
    a = int(a)
    c = 1/a
    print(f"The answer is {c}")
except ValueError as e:
    print("Exception 1 detected")
    print(e)

except ZeroDivisionError as e:
    print("Exception 2 detected")
    print(e)
    

print("Thanks!!!!")