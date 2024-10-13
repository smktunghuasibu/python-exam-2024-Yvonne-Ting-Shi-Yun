# test_math_utils.py
import pytest
from question_4_min_max import *

def test_min_value():
    # Test case 1: a is the smallest
    assert min_value(1, 5, 7, 9) == 1

    # Test case 2: b is the smallest
    assert min_value(10, 2, 15, 8) == 2

    # Test case 3: c is the smallest
    assert min_value(4, 6, 1, 9) == 1

    # Test case 4: d is the smallest
    assert min_value(7, 5, 3, 0) == 0

    # Test case 5: all values are the same
    assert min_value(5, 5, 5, 5) == 5

    # Test case 6: some values are equal
    assert min_value(3, 2, 2, 4) == 2

    # Test case 7: negative values
    assert min_value(-5, -3, -9, -1) == -9

    # Test case 8: mix of positive and negative values
    assert min_value(-7, 0, 5, -3) == -7

def test_max_value():
    # Test case 1: a is the largest
    assert max_value(10, 3, 5, 7) == 10
    
    # Test case 2: b is the largest
    assert max_value(4, 12, 6, 8) == 12
    
    # Test case 3: c is the largest
    assert max_value(1, 5, 9, 3) == 9
    
    # Test case 4: d is the largest
    assert max_value(2, 8, 4, 15) == 15
    
    # Test case 5: all values are the same
    assert max_value(5, 5, 5, 5) == 5
    
    # Test case 6: some values are equal
    assert max_value(3, 7, 7, 2) == 7
    
    # Test case 7: negative values
    assert max_value(-1, -3, -2, -4) == -1
    
    # Test case 8: mix of positive and negative values
    assert max_value(-5, 0, -2, 3) == 3

def test_main(capfd):
    # Run the main function
    main()
    
    # Capture printed output
    captured = capfd.readouterr()

    # Expected output
    expected_output = (
        "Minimum is 22.23\n"
        "Maximum is 48.89\n"    
    )

    # Assert that captured output matches the expected output
    assert captured.out == expected_output