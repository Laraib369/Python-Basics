# Use open function to read the content of a file
# f = open('sample.txt', 'r')
f = open("sample.txt") #by default it reads r
data = f.read()
print(data)
f.close()