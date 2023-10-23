#Even if you haven’t studied physics (recently or ever!), you might have heard that E=mc^2, wherein E represents energy (measured in Joules), m represents mass (measured in kilograms), and 
#  crepresents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

#In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

def main():
    # define light speed
    c = 300000000 # light speed in meters per second

    # prompt the user for mass in kilograms
    mass = int(input("m: "))

    # calculate the energy
    energy = mass * c ** 2

    # output the equivalent energy in joules
    print(f"E: {energy}")

main()