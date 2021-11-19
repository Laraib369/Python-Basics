
f = open("poems.txt", "r")
t = f.read()
if "twinkle" in t :
    print("twinkle is present")
else:
    print("No twinkle present")
f.close()
