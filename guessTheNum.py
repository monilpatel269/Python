import random

randomNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while userGuess != randomNumber:
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if userGuess == randomNumber:
        print("You guess the right number!")
    else:
        if userGuess >= randomNumber:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

print(f"You guess the number in {guesses} guesses")
with open("highscore.txt", "r") as f:
    hiscore = int(f.read())

if guesses < hiscore:
    print("You break the hiscore!!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
