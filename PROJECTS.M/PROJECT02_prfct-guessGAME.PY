import random
randNumber = random.randint(1, 100)
print(randNumber)  # This use for hide & unhide the random num
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess : "))
    guesses += 1
    if(userGuess == randNumber):
        print("You guessed it right !")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong ! Enter a smallar number :")
        else:
            print("You guessed it wrong ! Enter a larger  number :")

print(f"You guessed the number in {guesses} turns !")
with open("PROJECT02-hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("You have just broken the hiscore !")
    with open("PROJECT02-hiscore.txt", "w") as f:
        f.write(str(guesses))
