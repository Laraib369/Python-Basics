myDict = {
    "ghar" : "home",
    "phir" : "again",
    "tum" : "you",

}
print("Your options are :",myDict.keys())
word = input("Enter the word :\n")
print("The translation is : ",myDict.get(word) )
