import random

def main():
    print("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.")
    user_choice = int(input())
    comp_choice = random.randint(1, 3)
    if user_choice == 1:
        print("You chose Rock")
    elif user_choice == 2:
        print("You chose Paper")
    elif user_choice == 3:
        print("You chose Scissors")
    
    if comp_choice == 1 and user_choice == 3:
        print("Computer chose Rock. You lose.")
    elif comp_choice == 2 and user_choice == 1:
        print("Computer chose Paper. You lose.")
    elif comp_choice == 3 and user_choice == 2:
        print("Computer chose Scissors. You lose.")
    if user_choice == 1 and comp_choice == 3:
        print("Computer chose Rock. You win.")
    elif user_choice == 2 and comp_choice == 1:
        print("Computer chose Paper. You win.")
    elif user_choice == 3 and comp_choice == 2:
        print("Computer chose Scissors. You win.")
    elif user_choice == comp_choice:
        print("It's a draw.")

if __name__ == "__main__":
    main()