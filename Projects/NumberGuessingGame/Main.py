# Create a list of numbers from 1 to 100
# use a random.choice() to get a number and create a function to wrap this
# Ask user the input what level he wants to choose Easy, Hard
# Based on user chooses level set the chances
# create a for loop and iterate till chance values becomes 0
# In for loop validate whether guessed number is equal to random number choosen
import random
import art


def getRandomNumber():
    return random.randint(1, 100)


def getNumberOfAttempts(gameLevel):
    chances = 0
    if game_level == "easy":
        chances = 10
        print("You have 10 attempts to guess a number")
    elif game_level == "Hard":
        chances = 5
        print("You have 5 attempts to guess a number")
    return chances


def validateTheGuess(guessNumber, randomNumber, chancesToPlay):
    if guessNumber == randomNumber:
        print("You won as number guessed is correct!")
        chancesToPlay = 0
        return chancesToPlay
    elif guess_number > random_number:
        print("TOO HIGH")
        chancesToPlay -= 1
        print(f"You have {chances_to_play} attempts to guess the number")
        print("Guess Again")
        return chancesToPlay
    else:
        print("TOO LOW")
        chancesToPlay -= 1
        print(f"You have {chances_to_play} attempts to guess the number")
        print("Guess Again")
        return chancesToPlay


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

game_level = input("Choose a difficulty level type 'easy' or 'Hard' \n")
chances_to_play = getNumberOfAttempts(game_level)
random_number = getRandomNumber()
print(random_number)

while chances_to_play > 0:
    guess_number = int(input("Enter the number to guess: \n"))
    chances_to_play = validateTheGuess(guess_number, random_number, chances_to_play)
