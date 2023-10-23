"""In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py, three or more functions that collectively test your implementation of convert thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py"""


import re


def main():
        print(convert(input("Hours: ")))


def convert(s):
    def world_time(time, unit):
        # Check 12:00 or 12 format
        if ":" in time:
            time_hour, time_minute = map(int, time.split(":"))
        else:
            time_hour = int(time)
            time_minute = 0

        if unit == "PM":
            if 1 <= time_hour <= 11:
                time_hour += 12
            elif time_hour == 12:
                pass
            else:
                raise ValueError
        else:  # AM
            if time_hour == 12:
                time_hour = 0
            elif 1 <= time_hour <= 11:
                pass
            else:
                raise ValueError

        return f"{time_hour:02d}:{time_minute:02d}"

    time = re.match(
        r"^((?:[0-1]?[0-9]:[0-5][0-9])|(?:[0-1]?[0-9])) ((?:AM)|(?:PM)) to ((?:[0-1]?[0-9]:[0-5][0-9])|(?:[0-1]?[0-9])) ((?:AM)|(?:PM))$",
        s,
    )
    if time:
        start = time.group(1)
        start_unit = time.group(2)
        end = time.group(3)
        end_unit = time.group(4)

        return f"{world_time(start, start_unit)} to {world_time(end, end_unit)}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()

