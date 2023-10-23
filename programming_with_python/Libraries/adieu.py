"""In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 
 names with 
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl"""
def main():

    # Create an empty dictionary to store input names
    original_names = []

    # Create a loop to prompt the user to input names and store names in the dictionary, until seeing EOFError
    while True:

        try:
            name = input("Input: ")
        except EOFError:
            print()
            break
        else:
            original_names.append(name)

    # Print desired text
    l = len(original_names)
    if l == 1:
        print(f"Adieu, adieu, to {name}")
    elif l == 2:
        print(f"Adieu, adieu, to {original_names[0]} and {original_names[-1]}")
    else:
        fore_string = ", ".join(original_names[:l-1])
        print(f"Adieu, adieu, to {fore_string}, and {original_names[l-1]}")


if __name__ == "__main__":
    main()
