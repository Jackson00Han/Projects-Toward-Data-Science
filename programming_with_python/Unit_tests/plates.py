"""In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()"""

# This code should correctly check for:

## Length between 2 and 6 characters.
## The first two characters being alphabetic.
## No numbers appearing in the middle of the string.
## The first number not being '0'.
## No invalid characters like spaces, punctuation marks, etc.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Check that the first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Initialize a threshhold
    seen_digit = False

    # Iterate through the string
    for char in s:
        if char.isalpha():
            # If we've seen a digit already, a letter should not come after it
            if seen_digit:
                return False
        elif char.isdigit():
            # If this is the first digit and it's '0', that's invalid
            if not seen_digit and char == '0':
                return False
            # Update the flag since we've now seen a digit
            seen_digit = True
        else:
            # Any other characters are invalid
            return False

    # If all checks pass, the plate is valid
    return True

main()
