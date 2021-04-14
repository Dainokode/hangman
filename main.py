import random
from database import stages, logo, word_list

# pick random word
random_word = random.choice(word_list)
# print(random_word)

# create a display list with each letter of random word replaced by underscores
display = []
for letter in random_word:
    display += "_"

print(logo)

lives = 6
game_over = False
wrong_guesses = set()
# repeat until there are no more blanks in display
while not game_over:
    # prompt user for a letter
    guess = input("Choose a letter: ")

    if guess in wrong_guesses:
        print(f"You already typed {guess}")

    # loop through random_word, if user guess matches letter than replace ubderscore with letter
    for index in range(len(random_word)):
        if guess in random_word[index]:
            display[index] = guess
            print(display)

    # determine if user won or lost
    if not "_" in display:
        print("You won!")
        game_over = True
    elif not guess in random_word and not guess in wrong_guesses:
        wrong_guesses.add(guess)
        lives -= 1;
        print(f"The letter {guess} is not in the word.")
        print(stages[lives])
        print(f"{display}\n")
        if lives == 0:
            print(f"You lost. The word was {random_word}.")
            game_over = True
