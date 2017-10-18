#This is a guess the number game

import random
secretNumber = random.randint(1, 20)
print("I'm thinking of a random number between 1 and 20")

#The player gets 6 tries to figure out the number
for guessesTaken in range(1,7) :
    #print('Take a guess')
    guess = int(raw_input("Take a guess : "))

    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed the number in "+str(guessesTaken) + " guesses!")
else :
    print("Nope. The number I was thinking of was " + str(secretNumber))

