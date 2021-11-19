def readFile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file not found!!!!{filename}")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")