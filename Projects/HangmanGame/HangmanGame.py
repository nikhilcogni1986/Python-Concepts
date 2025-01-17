import random
import hangman_art
import hangman_words_list

lives = 7

# Create a list with random words and pick a random word and print it
words_list = hangman_words_list.word_list
word_to_be_checked = random.choice(words_list)

print(hangman_art.logo)
print(word_to_be_checked)

placeholder = ""
for letter in word_to_be_checked:
    placeholder += "_"
print(placeholder)

game_over = False
correct_letter = []
while not game_over:

    # create a loop and ask user to guess the letter to match the word
    print(f"***************{lives}/7 LIVES ARE LEFT******************************")
    guess = input("Guess a letter to check if its is present in the word\n").lower()
    print(guess)

    if guess in correct_letter:
        print(f"You already guessed {guess}")

    display = ""

    for letter in word_to_be_checked:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)

    # If guess is not in chosen word then reduce the lives count by 1
    if guess not in word_to_be_checked:
        lives -= 1
        print(f"You guessed {guess} which is not in the word. you lose a life")

        if lives == 0:
            game_over = True
            print("****************YOU LOSE*****************************")

    if "_" not in display:
        game_over = True
        print("****************YOU WIN*****************************")

    print(hangman_art.stages[lives])
