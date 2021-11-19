import random

def gameWin(computer,b):
    if computer == b :
        return None
    elif computer == "s":
        if b == "w":
            return False
        elif b == "g":
            return True
    elif computer == "w":
        if b == "s":
            return True
        elif b == "g":
            return False
    elif computer == "g":
        if b == "s":
            return False
        elif b == "w":
            return True




print("Computer Turn : Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    computer = "s"
elif randNo == 2:
    computer = "w"
elif randNo ==3:
    computer = "g"

b = input("Your Turn : Snake(s) Water(w) or Gun(g)?")

a= gameWin(computer,b)

print(f"You Chose {b}")
print(f"Computer Chose {computer}")
if a== None:
    print("The game is a Tie")
elif a:
    print("You Win")
else:
    print("You Lose")
