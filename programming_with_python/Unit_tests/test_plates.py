"""In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py"""

from plates import is_valid


def test_true():

    assert is_valid("AAA222") == True
    assert is_valid("ab2") == True
    assert is_valid("ab20") == True
    assert is_valid("ab") == True
    assert is_valid("cs50") == True

def test_false():
    assert is_valid("cs05") == False
    assert is_valid("PI3.14") == False
    assert is_valid("1202") == False
    assert is_valid("ab1cs") == False
    assert is_valid("2") == False
    assert is_valid("a") == False
    assert is_valid("ab12345") == False
