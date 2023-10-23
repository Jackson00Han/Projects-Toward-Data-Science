import pytest

from jar import Jar

def test_init():
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(24)
    assert jar.capacity == 24
    assert jar.size == 0

    # Test invalid capacity types
    with pytest.raises(ValueError):
        Jar("a_string")
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(0.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # Test exceeding capacity
    with pytest.raises(ValueError, match="Exceeds jar's capacity."):
        jar.deposit(8)

    # Test depositing negative or invalid values
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit("string")

def test_withdraw():
    jar = Jar()
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    # Test withdrawing more than size
    with pytest.raises(ValueError):
        jar.withdraw(5)

    # Test withdrawing negative or invalid values
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw("string")

def test_capacity_property():
    jar = Jar(10)
    assert jar.capacity == 10

    jar.capacity = 20
    assert jar.capacity == 20

    # Test setting invalid values
    with pytest.raises(ValueError):
        jar.capacity = -1
    with pytest.raises(ValueError):
        jar.capacity = "string"

def test_size_property():
    jar = Jar(10)
    assert jar.size == 0

    jar.size = 5
    assert jar.size == 5

    # Test setting invalid values
    with pytest.raises(ValueError):
        jar.size = -1
    with pytest.raises(ValueError):
        jar.size = "string"

    # Test setting size greater than capacity
    jar.capacity = 6
    with pytest.raises(ValueError):
        jar.size = 10

        