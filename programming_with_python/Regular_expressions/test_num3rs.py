import pytest

from numb3rs import validate


def test_format():

    assert validate("1.1.1") == False
    assert validate("1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("1..1.1.1") == False
    assert validate("122.0.222.132") == True

def test_int():
    assert validate("1.a.1.1") == False
    assert validate("cat") == False
    assert validate("0.0.0.0") == True

def test_range():
    assert validate("1.1.1.256") == False
    assert validate("256.1.1.20") == False
    assert validate("1.256.1.20") == False
    assert validate("1.1.256.20") == False
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True

