from validator_collection import checkers

def main():

    print(check(input("What's your email address ")))




def check(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()