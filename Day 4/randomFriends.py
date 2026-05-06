
import random


def main():
    friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
    random_friend = random.choice(friends)
    print(f"Your random friend is: {random_friend}")


if "__main__":
    main()