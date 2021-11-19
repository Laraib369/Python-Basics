n = 3
for i in range(3):
    if(i == 0 or i == 2 ):
        for j in range(3):
            print("*",end=' ')

    if(i==1):
        for j in range(3):
            if (j==0 or j==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()