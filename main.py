import random
import database

# List of words & random word
word_list = ["anto", "carla", "afro", "fanta"]
chosen_word = random.choice(word_list)

# code testing
print(f"The chosen word is {chosen_word}")

# list containing blanks for each word of the chosen word
display = []
for letter in chosen_word:
    display += "_"

# user guess and game logic
game_over = False
lives_left = 6

while not game_over:
    print(display)
    user_guess = input("Choose a letter: ").lower()

    # compare user guess to position in chosen word
    for position in range(len(chosen_word)):
        if chosen_word[position] == user_guess:
            display[position] = chosen_word[position]

    # subtract a life if guess is not equal to chosen word - print correct ascii based on lives
    if chosen_word != user_guess:
        lives_left -= 1 
        if lives_left == 5:
            print(database.stages[5])
        elif lives_left == 4: 
             print(database.stages[4])
        elif lives_left == 3:
            print(database.stages[3])    
        elif lives_left == 2:  
            print(database.stages[2])  
        elif lives_left == 1:    
            print(database.stages[1])
        elif lives_left == 0:    
            print(database.stages[0])
            game_over = True
            print("You lose.") 

    # if not more _ the loop stops(you win)
    if "_" not in display:
        game_over = True
        print("Congratulations, you win.") 
        
 