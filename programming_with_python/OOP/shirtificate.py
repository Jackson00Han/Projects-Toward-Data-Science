"""Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.

In a file called shirtificate.py, implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely. And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!"""

from fpdf import FPDF
from PIL import Image



def main():

    name = input("Name: ").strip()


    # Create a pdf file
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 32)
    pdf.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")  # 0-width means full width, align 'C' is center

    # Add an image on the center
    with Image.open("shirtificate.png") as img:
        w, h = img.size
    r = w / h
    width = 190
    height = width / r

    image_x = (210 - width) / 2
    image_y =(297 - height) / 2
    pdf.image("shirtificate.png", x=image_x, y=image_y, w=width, h = height)

    # Add username on top of the shirt
    pdf.set_y(image_y + 50)  # Approximate position at the center of the shirt
    pdf.set_text_color(255, 255, 255)  # Set text color to white
    pdf.set_font("Arial", "B", 24)
    pdf.cell(width, 10, name, align="C")

    # Output a pdf file
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()