content= True
i = 1
with open ("log_file.txt") as f:
    
    while content:
        content = f.readline()
        

        if "python"in content.lower():
            print(content)
            print(" Yes!!! python is present")
            print(i)
        i+=1
        