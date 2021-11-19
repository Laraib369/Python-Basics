n = 3
for i in range(3):
    print(" " * (n-i-1),end="")
    print("*" * (2*i + 1),end="")
    print(" " * (n-i-1))

# n = 3
# for i in range(3):
#     if(i==0):
#         for j in range(3):
#             if(j==2):
#                 print("*")
#             else:
#                 print(" ",end=" ")

# for i in range(3):
#     if(i==1):
#         for j in range(3):
#             if(j==0 or j==4):
#                 print(" ")
#             else:
#                 print("*",end=" ")