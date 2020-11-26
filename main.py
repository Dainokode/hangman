import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
user_guess = input("Choose a letter\n").lower()

for letter in chosen_word:
    if user_guess == letter:
        print("right")
    else:
        print("wrong")

print(chosen_word)
