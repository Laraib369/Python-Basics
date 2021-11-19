# Reads first line
f = open("sample.txt")
data = f.readline()
print(data)
# Reads 2nd line
data = f.readline()
print(data)
f.close()