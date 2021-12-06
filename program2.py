import random

guessNums = random.randint(0,100)
userGuess= []

while userGuess != guessNums:
    userGuess = int(input("Guess the number: "))
    if userGuess > guessNums:
        print("Greater than")
    elif userGuess < guessNums:
        print("Less then")