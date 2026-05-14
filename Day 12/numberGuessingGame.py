import random

guess = random.randint(1, 100)

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    print("Choose a difficulty level. Type 'easy' for 10 attempts or 'hard' for 5 attempts:")
    
    difficulty = input().lower()
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty level. Defaulting to 'hard'.")
        attempts = 5

    while attempts > 0:
        try:
            user_guess = int(input(f"You have {attempts} attempts left. Enter your guess: "))
            if user_guess < guess:
                print("Too low! Try again.")
            elif user_guess > guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the number!")
                break
            attempts -= 1
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts == 0:
        print(f"Game over! The correct number was {guess}.")