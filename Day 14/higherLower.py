# This is the higher lower game. The user is given two options and they have to guess which one has more followers on Instagram.

import random

def get_random_account():
    accounts = [
        {"name": "Instagram", "followers": 500000000},
        {"name": "Cristiano Ronaldo", "followers": 300000000},
        {"name": "Ariana Grande", "followers": 250000000},
        {"name": "Dwayne Johnson", "followers": 200000000},
        {"name": "Selena Gomez", "followers": 150000000},
        {"name": "Kim Kardashian", "followers": 100000000}
    ]
    return random.choice(accounts)

if __name__ == "__main__":
    print("Welcome to the Higher Lower Game!")
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    while True:
        print(f"Compare A: {account_a['name']} with {account_a['followers']} followers.")
        print("VS")
        print(f"Compare B: {account_b['name']} with {account_b['followers']} followers.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if (guess == 'A' and account_a['followers'] > account_b['followers']) or (guess == 'B' and account_b['followers'] > account_a['followers']):
            score += 1
            print(f"Correct! Your current score is: {score}")
            account_a = account_b
            account_b = get_random_account()
            while account_a == account_b:
                account_b = get_random_account()
        else:
            print(f"Wrong! Final score: {score}")
            break