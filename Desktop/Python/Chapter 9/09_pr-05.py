list = ["donkey","idiot","fuck","fuck off","duffer"]

with open("list_ab.txt") as f:
    content= f.read()

for word in list:
    content = content.replace(word,"*@#")
    with open("list_ab.txt","w") as f:
        f.write(content)