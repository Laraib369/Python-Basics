with open("sample.txt") as f:
    content= f.read()

content= content.replace(content," ")

with open("sample.txt","w") as f:
    content= f.write(content)