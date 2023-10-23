"""In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or more functions that collectively test your implementation of validate thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_numb3rs.py"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    
    matches = re.search(r"^([0-9]*)\.([0-9]*)\.([0-9]*)\.([0-9]*)$", ip)
    if matches:
        ip1 = matches.group(1)
        ip2 = matches.group(2)
        ip3 = matches.group(3)
        ip4 = matches.group(4)
    else:
        return False

    try:
        ip1 = int(ip1)
        ip2 = int(ip2)
        ip3 = int(ip3)
        ip4 = int(ip4)

    except ValueError:
        return False

    else:
        if not (0 <= ip1 <= 255):
            return False
        elif not (0 <= ip2 <= 255):
            return False
        elif not (0 <= ip3 <= 255):
            return False
        elif not (0 <= ip4 <= 255):
            return False
        else:
            print(f"{ip1}.{ip2}.{ip3}.{ip4}")
            return True



if __name__ == "__main__":
    main()










