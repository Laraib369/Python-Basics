i = 3
for i in range(3):
    if (i==0 or i==2):
        for j in range(3):
            print("*",end=" ")

    if (i==1):
        for j in range(3):
            if (j==1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
    print()