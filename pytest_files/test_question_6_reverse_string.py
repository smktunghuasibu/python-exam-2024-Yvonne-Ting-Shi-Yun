# test_string_utils.py
import pytest
from question_6_reverse_string import string_reverse, main

def test_string_reverse():
    # Test case 1: Regular string
    assert string_reverse("hello") == "olleh"

    # Test case 2: Empty string
    assert string_reverse("") == ""

    # Test case 3: Single character string
    assert string_reverse("a") == "a"

    # Test case 4: String with spaces and special characters
    assert string_reverse("a b c!") == "!c b a"

    # Test case 5: Palindrome (should return the same string)
    assert string_reverse("madam") == "madam"

    # Test case 6: Numeric string
    assert string_reverse("12345") == "54321"

def test_main(capfd):
    # Call the main function, which prints the output
    main()

    # Capture the printed output
    captured = capfd.readouterr()

    # Define the expected output string
    expected_output = "String reverse for '12345abcde' is edcba54321\n"

    # Check that the captured output matches the expected output
    assert captured.out == expected_output