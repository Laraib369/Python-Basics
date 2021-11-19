import os


oldname = "sample2.txt"
newname = "python_renamed.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)