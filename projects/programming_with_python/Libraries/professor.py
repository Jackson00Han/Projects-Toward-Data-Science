"""One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()"""

import random


def main():

    # Prompt the user for a lever
    n = get_level()

    incorrect = 0
    total_number = 0

    while total_number < 10 :

        x = generate_integer(n)
        y = generate_integer(n)
        sol = x + y
        wrong = 0
        while wrong <3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != sol:
                    print("EEE")
                    wrong += 1
                    if wrong == 3:
                        incorrect += 1
                        total_number += 1
                        print(f"{x} + {y} = {sol}")
                else:
                    total_number += 1
                    break
            except ValueError:
                print("EEE")
                wrong += 1
                if wrong == 3:
                    incorrect += 1
                    total_number += 1
                    print(f"{x} + {y} = {sol}")
    print(f"Score: {10 - incorrect}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except ValueError:  # Handle if the input is not a number
            continue


def generate_integer(n):

    if n == 1:
        return random.randint(0, 9)
    if n in [2, 3]:
        return random.randint(10 ** (n-1), (10 ** n)-1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()