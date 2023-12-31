from working import convert
import pytest

def test_valid_input_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_input_2():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_valid_input_3():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid_time_1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_time_2():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")

def test_invalid_format_1():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_format_2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


