# Import pytest (used for writing and running tests)
import pytest

# Import functions from utils.py that we want to test
from utils import validate_task, format_task_response


# -------------------------------
# Basic assertion tests
# -------------------------------

def test_validate_task_with_valid_input():
    # Valid title should pass
    is_valid, msg = validate_task("Buy groceries")
    
    assert is_valid is True      # Expect True
    assert msg == ""             # No error message


def test_validate_task_empty_title():
    # Empty title should fail
    is_valid, msg = validate_task("")
    
    assert is_valid is False
    assert "Title cannot be empty" in msg


def test_validate_task_too_long_title():
    # Title longer than 100 chars should fail
    long_title = "a" * 101
    
    is_valid, msg = validate_task(long_title)
    
    assert is_valid is False
    assert "too long" in msg


# -------------------------------
# Parametrized test (multiple cases)
# -------------------------------

@pytest.mark.parametrize("title, expected_valid", [
    ("Valid task", True),     # Normal valid case
    ("", False),              # Empty string
    ("a" * 100, True),        # Exactly 100 chars (valid)
    ("a" * 101, False),       # More than 100 (invalid)
    ("   ", False),           # Only whitespace
])
def test_validate_task_parametrized(title, expected_valid):
    is_valid, _ = validate_task(title)
    
    assert is_valid == expected_valid


# -------------------------------
# Test for formatter function
# -------------------------------

def test_format_task_response():
    # Sample task dictionary
    task = {
        "id": 1,
        "title": "Learn Docker",
        "done": False
    }

    # Format the response
    formatted = format_task_response(task)

    # Check output contains expected values
    assert "Learn Docker" in formatted
    assert "Done: False" in formatted