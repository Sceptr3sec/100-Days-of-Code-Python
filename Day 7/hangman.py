#lets play hangman

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chances = 6
print(f"The chosen word is {chosen_word}")
display = []
for letter in chosen_word:
    display += "_"
print(display)
guess = input("Guess a letter: ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        chances -= 1
        print(f"You have {chances} chances left.")
print(display)
