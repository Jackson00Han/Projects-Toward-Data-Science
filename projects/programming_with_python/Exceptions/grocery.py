"""Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively."""

def main():
    grocery_dic = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            print()
            break
        else:
            if item not in grocery_dic:
                grocery_dic[item] = 1
            else:
                grocery_dic[item] += 1

    output_grocery(grocery_dic)



def output_grocery(dic):
    grocery_list = list(dic.keys())
    grocery_list.sort()

    for item in grocery_list:
        print(f"{dic[item]} {item}")


if __name__ == "__main__":
    main()





