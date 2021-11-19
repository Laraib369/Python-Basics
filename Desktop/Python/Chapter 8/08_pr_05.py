# n = 3
# for i in range(3):
#     if i==0 :
#         for j in range(3):
#             print("*",end=" ")
#     if i==1 :
#         for j in range(3):
#             if j==2 :
#                 print(" ",end=' ')
#             else:
#                 print("*",end=" ")
#     if i==2 :
#         for j in range(3):
#             if j==0:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print()          

n=4
for i in range(4):
    print("*" * (n-i))
  