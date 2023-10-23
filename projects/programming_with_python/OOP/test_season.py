from seasons import get_minutes
import pytest
import sys


def test_format():
    with pytest.raises(SystemExit, match="Invalid date"):
        get_minutes("1992.1.1")
    with pytest.raises(SystemExit, match="Invalid date"):
        get_minutes("1992")
    with pytest.raises(SystemExit, match="Invalid date"):
        get_minutes("Jan 1, 1992")