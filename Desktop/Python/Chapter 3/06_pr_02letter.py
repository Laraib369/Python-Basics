letter ='''Dear, <|NAME|>
Greetings from MIT ,I am happy to let you know that
You are selected!

<|DATE|>'''
name = input("Enter your name \n")
date = input("Date \n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>",date)
print(letter)