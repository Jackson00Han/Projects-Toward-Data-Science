import sys
import json
import re
import requests

### Who Owns Who ###

def main():

    # Get input values
    name, item, pay, unit = process_arguments(sys.argv)
    name = name.lower().capitalize()
    pay = float(pay)
    unit = unit.upper()
    # Convert currency
    rate = get_rate(unit)
    pay /= rate

    # convert json data to Python data -- list
    data = load_data()
    # Initialize a boolean value for the loop later
    found = False
    for person in data:
        if person["name"] == name:
            found = True
            if item in person["item"]:
                person["paid"] += pay
                person["paid"] = round(person["paid"], 2)
            else:
                person["item"].append(item)
                person["paid"] += pay
                person["paid"] = round(person["paid"], 2)
                break
        else:
            continue

    if not found:
        data.append({"name": name, "item": [item], "paid": pay})

    # Save data
    save_data(data)

    # Output who owns whom and how much
    # Calculate total and average payment
    total_paid = sum(entry['paid'] for entry in data)
    average_payment = total_paid / len(data)

    # This will store a simplified version of who owes whom
    settlements = {}

    for entry in data:
        name = entry['name']
        amount_paid = entry['paid']
        difference = average_payment - amount_paid
        settlements[name] = difference

    # Output
    wow = show_debts(settlements)
    print(f"{data}\n{wow}" if wow else data)


def process_arguments(args):
    l = len(args)

    if l < 5:
        if l == 2 and args[1].lower() == "clear":
            save_data([]) # Empty the data.json file
            sys.exit("All data has been cleared")
        else:
            sys.exit("Too few arguments")
        return # <-- Add this return statement

    if 5 < l:
        sys.exit("Too many arguments")
        return

    if not re.search(r"^-?\d*(\.\d+)?$", args[3], re.IGNORECASE):
        sys.exit("Please input a valid price")
        return

    if not re.search(r"^(CNY|DKK|EUR|GBP|USD)$", args[4], re.IGNORECASE):
        sys.exit("Please change currency")
        return

    return args[1], args[2], args[3], args[4]

def get_rate(unit):
    # change currency to EURO
    if unit != "EUR":
        rates = requests.get("https://api.exchangerate-api.com/v4/latest/EUR").json()
        return rates["rates"][unit]
    else:
        return 1.0

def show_debts(settlements):
    results = []
    # Now, settle up
    while any(abs(val) > 1e-9 for val in settlements.values()):  # Using a small threshold instead of checking for 0 due to floating point imprecision
        # Find the person who owes the most
        payer = max(settlements, key=settlements.get)

        # Find the person who is owed the most
        payee = min(settlements, key=settlements.get)

        # Amount to settle between payer and payee
        settle_amount = min(settlements[payer], -settlements[payee])

        # Append the transaction to results
        results.append(f"{payer} owes {payee} {settle_amount:.2f} EUR")


        # Update the settlements
        settlements[payer] -= settle_amount
        settlements[payee] += settle_amount
    return '\n'.join(results)

def load_data(filename="data.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()