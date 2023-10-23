"""I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit."""

import random

def main():

    while True:

        level = input("Level: ")

        # Level should be an integer
        if not level.isdigit():
            continue
        level = int(level)

        # Level shoudl be in [1, 100]
        if (level == 0) or (100 < level):
            continue

        # Guess should be in the range of level
        rand = random.randint(1, level)
        while True:
            guess = input("Guess: ")

            if guess.isdigit():
                guess = int(guess)
                if level < guess:
                    continue
                if guess < rand:
                    print("Too small!")
                elif rand < guess:
                    print("Too large!")
                else:
                    print("Just right!")
                    exit()
if __name__ == "__main__":
    main()



