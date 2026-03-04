import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import password_errors, check_password


def test_too_short_is_weak():
    assert check_password("Abc12") == "weak"
    assert "too_short" in password_errors("Abc12")


def test_no_digit_is_weak():
    assert check_password("Password!") == "weak"
    assert "no_digit" in password_errors("Password!")


def test_no_letter_is_weak():
    assert check_password("12345678!") == "weak"
    assert "no_letter" in password_errors("12345678!")


def test_contains_space_is_weak():
    assert check_password("Pass word1!") == "weak"
    assert "contains_space" in password_errors("Pass word1!")


def test_medium_when_no_errors_but_no_symbol():
    assert check_password("Password1") == "medium"
    assert password_errors("Password1") == []


def test_strong_password():
    assert check_password("Password1!") == "strong"
    assert password_errors("Password1!") == []


def test_top_level_errors_list_can_contain_multiple_items():
    errs = password_errors("12 34")
    assert "too_short" in errs