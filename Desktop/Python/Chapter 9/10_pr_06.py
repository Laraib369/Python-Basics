with open ("log_file.txt") as f:
    content = f.read().lower()
    if "python"in content:
        print(" Yes!!! python is present")
    else:
        print("python is absent")