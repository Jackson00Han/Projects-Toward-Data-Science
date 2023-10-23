"""When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase."""

def main():
    # Prompt the user for a input
    text = input("Input: ")
    text = text.strip()

    output = shorten(text)

    print(f"Output: {output}")


def shorten(text):

    new_text = []

    for char in text:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            new_text.append(char)
        else:
            continue

    return "".join(new_text)

if __name__ == "__main__":
    main()