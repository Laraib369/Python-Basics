def remove_and_split(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "   Harry is a good   "
n = remove_and_split(this,"harry")
# print(this)
print(this.strip())