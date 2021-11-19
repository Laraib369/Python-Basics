myDict = {
    "kar" : "Do",
    "Bol" : "Speak",
    "namaste" : "Hello",
    "alvida" : "Bye"
}
print("The options are" , myDict.keys())
a = input("Enter the hindi word\n")
# print("The meaning of this word is :\n " , myDict[a])
print("The meaning of your words is:", myDict.get(a))