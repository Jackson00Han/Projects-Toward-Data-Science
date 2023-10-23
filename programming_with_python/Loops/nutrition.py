""""The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

""""

def main():

    # Prompt the user to input a fruit (case-insensitively)
    fruit = input("Item: ")

    calory = get_calory(fruit)

    if calory is not None:
        print(f"Calories: {calory}")
    else:
        print("")

def get_calory(x):
    x = x.lower()

    # Build a dictionary to store nutrition information
    dic_fruit_nutrition = {"apple": "130", "avocado": "50", "banana": "110", "cantaloupe": "50", "grapefruit": "60", "grapes": "90", "honeydew Melon": "50",
                 "kiwifruit": "90", "lemon": "15", "nectarine": "60", "orange": "80", "peach": "60", "pear": "100", "pineapple": "50", "plums": "70",
                 "strawberries": "50", "sweet cherries": "100", "tangerine": "50", "watermelon": "80"
    }
    
    if x in dic_fruit_nutrition:
        return int(dic_fruit_nutrition[x])
    else:
        return None

main()
