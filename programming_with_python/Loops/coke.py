"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination."""

def main():
    amount_due = 50

    while 0 < amount_due:
        print(f"Amount Due: {amount_due}")

        # Prompt the user to insert coin
        insert = int(input("Insert Coin: "))

        # Only 25, 10, and 5 work
        if insert not in [5, 10, 25]:
            insert = 0
        else:
            insert = insert

        amount_due -= insert

    if amount_due == 0:
        print("Change Owed: 0")
    else:
        print(f"Change Owed: {-amount_due}")


if __name__ == "__main__":
    main()