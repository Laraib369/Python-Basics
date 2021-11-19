def percent(marks):
    return(((marks[0]+marks[1]+marks[2]+marks[3])/400)*100)

marks1 = [45,56,6,89]
percentage1 = percent(marks1)

marks2 = [56,67,43,56]
percentage2 = percent(marks2)

print(percentage1,percentage2)