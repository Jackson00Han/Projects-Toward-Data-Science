from um import count

def test_zero():
    assert count("hello") == 0

def test_normal():
    assert count("um, I'm thinking") == 1

    assert count("um, I'am um thinking") == 2

    assert count("Hi, um, I am um") == 2

def test_punctuation():
    assert count("Hi, um..., good") == 1

def test_number():
    assert count("Hi, um2, I'am um good") == 1

def test_case():
    assert count("Um, Hello") == 1

    assert count("Hi, UM, I'm um good") == 2
