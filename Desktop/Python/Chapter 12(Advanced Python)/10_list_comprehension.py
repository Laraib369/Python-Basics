a = [3,4,5,6,7,8,9,0,7,7,6,5,4,4444,4,4,33,2,2,4,6,777,8,8889,10]
# b = []
# for item in a:
#     if item%2 == 0:
#         b.append(item)
# print(b)

b = [i for i in a if i%2==0]
print(b)
