#Implement the convert Function:

# This function takes a string as input.
# It searches for emoticons :) and :( in the string.
# It replaces :) with the emoji 🙂 and :( with the emoji 🙁.
# It returns the modified string.

#Implement the main Function:

# This function doesn’t take any parameters.
# It prompts the user to enter a string.
# It calls the convert function with the user’s input.
# It prints the result returned by the convert function.
# Call main at the End:

#Ensure that the main function is called when the script runs by placing a call to main() at the end of the file.

def main():
    # prompt users for input
    user_input = input("Please enter some text: ")
    # Call the convert function to replace emoticons with emojis
    converted_text = convert(user_input)

    print(converted_text)


def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    modified_text = text.replace(":)", "🙂")
    modified_text = modified_text.replace(":(", "🙁")
    return modified_text

# Call the main function
main()