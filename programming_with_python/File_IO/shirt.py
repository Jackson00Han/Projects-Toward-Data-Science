"""After finishing CS50 itself, students on campus at Harvard traditionally receive their very own I took CS50 t-shirt. No need to buy one online, but like to try one on virtually?

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input’s name does not have the same extension as the output’s name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.

If you’d like to run your program on a photo of yourself, first drag the photo over to VS Code’s file explorer, into the same folder as shirt.py. No need to submit any photos with your code. But, if you would like, you’re welcome (but not expected) to share a photo of yourself wearing your virtual shirt in any of CS50’s communities!

"""

import sys

import os

from PIL import Image
from PIL import ImageOps

def main():

    l = len(sys.argv)
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    f1 = f1.strip().lower()
    f2 = f2.strip().lower()


    if l <= 2:
        sys.exit("Too few command-line arguments")

    if 3 < l:
        sys.exit("Too many command-line arguments")

    if (not f1.endswith(".jpg")) and (not f1.endswith(".jpeg")) and (not f1.endswith(".png")) and (not f2.endswith(".jpg")) and (not f2.endswith(".jpeg")) and (not f2.endswith(".png")):
        sys.exit("Invalid input")

    f1_name, f1_ex = os.path.splitext(f1)
    f2_name, f2_ex = os.path.splitext(f2)
    f1_ex = f1_ex.strip()
    f2_ex = f2_ex.strip()

    if f1_ex != f2_ex:
        sys.exit("Input and output have different extensions")

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exit")
    else:
        centering = (0.5, 0.5)
        small_im = ImageOps.fit(image, shirt.size, centering=centering)
        small_im.paste(shirt, shirt)
        small_im.save(f2)






if __name__ == "__main__":
    main()







