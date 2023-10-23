"""One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased."""

# implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively.
# Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

# Programe
# 1. Build a menu dictionary
# 2. Prompt the user for an item, and assign it to a variable input_value, case insensitively,
# 3. Find the price of the item from the menu and assign it to a variable: total_value
# 4. Format of total_value, print it with f""
# 5. If have not seen "d", continue prompting the user to input an item, until see "d" and break loop


def main():
    # Create a menu dictionary
    menu = {
        "baja taco": 4.00,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

    total = 0

    while True:

        try:
            item = input("Item: ")
            item = item.strip().lower()

            if item in menu:
                price = menu[item]
                total = total + price
                print(f"Total: ${total:.2f}")

        except EOFError:
            print()
            break

if __name__ == "__main__":
    main()
