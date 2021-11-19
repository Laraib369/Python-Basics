myDict = {
    "fast" : "In a Quick Manner",
    "harry" : "A Coder",
    "marks": [1,2,3],
    "anotherdict": {'Harry': 'Player'},
    1: 2
}

# print(type(myDict.keys())) #prints the keys of dictionary
# print((myDict.values())) #prints the value of keys
# print(myDict.items()) # Prints the key,value for all items of dictionary
print(myDict)
updatedDict = {
    'Lovish' : 'Friend'
}
myDict.update(updatedDict)
print(myDict)

print(myDict.get("harry"))
print(myDict['harry'])

# the diffrence between .get & [] syntax
print(myDict.get("harry2")) #returns none
print(myDict["harry2"]) #throws an error
