"""Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()"""

def main():
    # Prompt the user for the time
    time = input("What time is it? ")

    # Remove whitespaces on the two sides of the time
    time = time.strip()

    # Convert time to floats in 24-hour time
    time = convert(time)

    # Identify the meal time
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    elif time < 0 or time >24:
        print("This is not a correct time")
        exit()
    else:
        print("")


# Define a function to convert time to be float 24-hour format
def convert(time):
    if time.lower().endswith("p.m."):
        time = time.replace("p.m.", "").strip()
        # Define a threshold to put 12-hour format back to 24-hour format later
        t = 1
    elif time.lower().endswith("a.m."):
        time = time.replace("a.m.", "").strip()
        t = 0
    else:
        t = 0

    # Convert the time to floats
    x, y = time.split(":")

    x = int(x) + 12 * t
    y = int(y)
    y = float(y/60)

    return x + y

if __name__ == "__main__":
    main()