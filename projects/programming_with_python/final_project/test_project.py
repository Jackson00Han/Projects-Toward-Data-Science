import pytest
import requests
from wow import process_arguments, get_rate, show_debts
from unittest.mock import patch, Mock

 ### No.1 process_arguments ###
@pytest.mark.parametrize("arguments, error_message", [
    (["wow.py"], "Too few arguments"),
    (["wow.py", "John"], "Too few arguments"),
    (["wow", "John", "Bread", "10", "USD", "10 o'clock"], "Too many arguments")
])
def test_process_arguments(arguments, error_message):
    # 1. Test
    args = ['wow.py', "clear"]
    with patch("wow.save_data") as mock_save_data, patch("sys.exit") as mock_exit:
        process_arguments(args)

        # Check if save_data was called with an empty list
        mock_save_data.assert_called_once_with([])

        # Check if sys.exit was called with the right message
        mock_exit.assert_called_once_with("All data has been cleared")

    # 2. Test invalid number of arguments
    with patch('sys.exit') as mock_exit:
        process_arguments(arguments)
        mock_exit.assert_called_once_with(error_message)

    # 3. Test invalid price
    args = ["script_name", "John", "Bread", "t20", "dkk"]
    with patch("sys.exit") as mock_exit:
        process_arguments(args)
        mock_exit.assert_called_once_with("Please input a valid price")

    # 4. Test invalid currency
    args = ["script_name", "John", "Bread", "20", "Invalid"]
    with patch("sys.exit") as mock_exit:
        process_arguments(args)
        mock_exit.assert_called_once_with("Please change currency")

    # 5. Test valid args
    args = ["wow.py", "John", "Bread", "20", "dkk"]
    assert process_arguments(args) == ('John', 'Bread', '20', 'dkk')


### No.2 get_rate ###
@patch('requests.get')
def test_get_rate(mock_get):
    # Mock the API response
    mock_responce = Mock()
    mock_responce.json.return_value = {
        'rates':{
            'EUR': 1.00,
            'CNY': 7.72,
            'DKK': 7.46,
            'GBP': 0.87,
            'USD': 1.06,
        }
    }
    mock_get.return_value = mock_responce
    # Check the function's output
    assert get_rate("DKK") == 7.46

    assert get_rate("EUR") == 1.00

    assert get_rate('CNY') == 7.72

    assert get_rate('GBP') == 0.87

    assert get_rate('USD') == 1.06


### No. 3 show_debts ###

def test_show_debts():
    data1 = {'jackson': -30, 'yun': 30}
    result1 = show_debts(data1)
    output1 = "yun owes jackson 30.00 EUR"  # Removed extra space
    assert result1 == output1

    data2 = {'jackson': -60, 'yun': 40, 'han': 20}
    result2 = show_debts(data2)
    output2 = "yun owes jackson 40.00 EUR\nhan owes jackson 20.00 EUR"  # Removed extra space
    assert result2 == output2

