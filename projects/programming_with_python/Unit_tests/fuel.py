"""Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError."""


# Prompt the user to input a fraction X/Y, where X and Y are integers, convert it to a percentage rounded to the nearest integer, e.g. 1/3 -> 33%. if fraction is 1% or less, then output E; if fraction is 99% or more, output F.
# If X or Y is not integer, Y < X, or Y is 0, prompt the user again.

# Program:
# 1. Prompt the user to input a fraction,
# 2. Assign x and y values by split fractions
# 3. Convert x and y to integer format; Catch ValueError exception, if so print and prompt the user again
# 4. Check if x and y satisfy the requirement, if not prompt the user again
# 5. convert the fraction into a float rounded in 2 digit, then assign it to a new variable after timing 100, after that, assign a new variable by joining it and the symbol "%"
# 6. Print the new variable

def main():

    while True:
        fraction = input("Fraction: ")

        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if x > y or y == 0:
                continue

            z = round((x / y) * 100)

            if z <= 1:
                print("E")
                break
            elif z >= 99:
                print("F")
                break
            else:
                print(f"{z}%")
                break

        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()