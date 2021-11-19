# Write a letter!!!

Letter = ''' Dear |NAME|,
We are happy to break it to you that you have been admitted into MIT !!!

|DATE|
'''
name = input("Name is :\n")
date = input("Date is:\n")
Letter= Letter.replace("|NAME|",name)
Letter= Letter.replace("|DATE|",date)
print(Letter)
