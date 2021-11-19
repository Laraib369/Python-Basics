# Creating an empty set
b = set()
print(type(b))

# Adding value to an empty set
b.add(4)
b.add(5)
b.add(5)#Adding a value repetedely doesn't affect the set

# b.add([4,5,6]) #List cannot be inserted in a set

b.add((4,5,6))# Tuple can be added in a set

# b.add({1,2,3}) #Dictionary cannot be inserted in a set
print(b)


print(len(b)) #prints the length of this set


# b.remove(5) #removes 5
# b.remove(15) # throws an error
# print(b)

print(b.pop())
print(b)