import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    
    userGuess = int(input("Enter your guess : "))
    guesses += 1
    if (userGuess == randNumber):
        print("Your guess is right!!!")
    else:
        if (userGuess>randNumber):
            print("Enter a smaller number")

        else:
            print("Enter a larger number")
    

print(f"You guessed the number in {guesses} chances")
with open("highscore.txt", "r") as f:
    highscore = int (f.read())

if (guesses< highscore) :
    print("This is the Highscore")
    with open ("highscore.txt" , "w") as f:
        f.write(guesses)
