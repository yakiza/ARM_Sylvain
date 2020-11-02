import pytest
from arm_flask.balance_checker import check_if_is_balanced


def test_balanced_string():
    result = check_if_is_balanced("()")
    assert result == "It is BALANCED"

def test_not_balanced_string():
    result = check_if_is_balanced("(((}")
    assert result ==  "Is not BALANCED"