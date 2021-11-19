i = 4 
for i in range(4):
    if i==0 :
        for j in range(4):
            print("*",end=" ")
    if i ==1 :
        for j in range(4):
            if j==0 or j==1 or j==2 :
                print("*",end=" ")
    if i == 2:
        for j in range(4):
            if j == 0 or j ==1:
                print("*",end=" ")
    if i == 3:
        for j in range(4):
            if j==0 :
                print("*",end=" ")
    print()