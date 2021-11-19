try:
    a = int(input("Enter your number: "))
    c = 1/a

except Exception as e:
    print(e)

finally:
    print("We are done")