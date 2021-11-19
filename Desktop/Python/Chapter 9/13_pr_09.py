file1 = "log_file.txt"
file2 = "this.txt"

with open(file1) as f:
    content1=f.read()

with open(file2) as f:
    content2=f.read()

if content1==content2:
    print("file1 and file2 have same content")

else:
    print("file1 and file are not same")
