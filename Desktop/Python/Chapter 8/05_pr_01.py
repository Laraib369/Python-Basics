def great(num1,num2,num3):
    if (num1 > num2 ):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = great(3,80,78)
print("The greatest of these three are",m)