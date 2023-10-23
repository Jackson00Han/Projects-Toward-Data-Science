# Who Owes Who (WOW)

#### Video Demo:  <https://youtu.be/mHyWHlJDj0k>u[]

### Jackson Han, Copenhagen, Denmark. Email: jackson.sz.han@gmail.com

#### Description:

Introducing **Who Owns Who (WOW)** - the solution to all your group expenditure woes!

Going on a trip or shopping spree with friends? WOW is here to ensure there's no confusion about who owes what. This program seamlessly calculates and provides a clear breakdown of group expenses, all settled in **euros**.

**How to Use WOW?**

All you need to do is launch the command line and provide the name of the person who paid, the item description, and the amount paid. WOW takes care of the rest.

For instance, Jackson, Yun, and Han are on vacation in Legoland. So far, Jackson has paid 980 DKK for Legoland tickets, Yun has paid 30 EUR for train tickets, and Han has paid 120 DKK for drinks.
You may input:

```$ python wow.py jackson legoland_tickets 980 DKK```
```$ python wow.py yun train_tickets 30 EUR```
```$ python wow.py han drinks 120 DKK```

Then the output will be

[{'name': 'Jackson', 'item': ['legoland_tickets'], 'paid': 131.36729222520108}, {'name': 'Yun', 'item': ['train_tickets'], 'paid': 30.0}, {'name': 'Han', 'item': ['drinks'], 'paid': 16.0857908847185}]
Han owes Jackson 43.07 EUR
Yun owes Jackson 29.15 EUR

Here, the final result is converted to Euros rounded to two decimal places.

### Note
- **Supported Currencies:** Currently, WOW supports five currencies: CNY, DKK, EUR, GBP, and USD. Any other
  currencies input or incorrect format will cause the program to exit with the message, "Please change currency."
- **Clearing Data:** When you want to clear the data, you may input
  ```python wow.py clear```
- **Argument Count:** The program is designed to accept precisely 5 arguments. Deviating from this will result in an error message. The only
  exception to this is when you want to clear data.
- **Valid Price Input:** Ensure the price is entered in numerals. Using words like "ten" will result in the message "Please input a valid
  price" and the program will exit.
