
import random


def game():
    print("Welcome to Blackjack!")
    # Initialize the game state, such as player and dealer hands, scores, etc.
    # Implement the game logic, including dealing cards, calculating scores, and determining the winner.
    # You can use a simple representation for cards and hands, such as lists or dictionaries.
    # Include options for the player to hit or stand, and handle the dealer's actions accordingly.
    # Finally, display the results of the game and ask if the player wants to play again.
    face_cards = {"Jack": 10, "Queen": 10, "King": 10}
    cards = list(int(x) for x in face_cards.keys()) + list(range(1, 11))
    player_hand = []
    dealer_hand = []
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    choice = input("Do you want to hit or stand? (hit/stand): ")
    if choice.lower() == "hit":
        player_hand += [int(random.choice(cards))]
        dealer_hand += [int(random.choice(cards))]
        for _ in range(2):
            print(f"Your hand: {player_hand}")
            print(f"Dealer's hand: {dealer_hand[0]} and a hidden card")
        # Calculate scores and determine the winner
        # This is a simplified version of the game logic, and you can expand it to include more features and rules as needed.
            if sum(player_hand) > 21:
                print("You bust! Dealer wins.")
            elif sum(dealer_hand) > 21:
                print("Dealer busts! You win.")
            elif sum(player_hand) > sum(dealer_hand):
                print("You win!")
            elif sum(player_hand) < sum(dealer_hand):
                print("Dealer wins!")
            else:
                print("It's a tie!")

def main():
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()