import pytest
from question_1_calculation import *
#import isipadu_tangki_air

def test_calculation_normal_case():
    # Normal case where both x and y are non-zero
    result = calculation(10, 5)
    assert result == (5, 50, 2.0)  # subtraction=5, multiplication=50, division=2.0

def test_calculation_division_by_zero():
    # Case where y is zero; division should return None
    result = calculation(10, 0)
    assert result == (10, 0, None)  # subtraction=10, multiplication=0, division=None

def test_calculation_negative_values():
    # Case where both x and y are negative
    result = calculation(-10, -5)
    assert result == (-5, 50, 2.0)  # subtraction=-5, multiplication=50, division=2.0

def test_calculation_mixed_signs():
    # Case where x is positive and y is negative
    result = calculation(10, -5)
    assert result == (15, -50, -2.0)  # subtraction=15, multiplication=-50, division=-2.0

def test_calculation_floating_point_values():
    # Case with floating point values
    result = calculation(7.5, 2.5)
    assert result == (5.0, 18.75, 3.0)  # subtraction=5.0, multiplication=18.75, division=3.0

def test_get_numbers(monkeypatch):
    # Simulate user inputs using monkeypatch
    inputs = iter([5.0, 10.0])  # Simulated inputs for A and B

    # Monkeypatch the 'input' function to return the next value from 'inputs' on each call
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the function
    A, B = get_numbers()

    # Assert that the returned values are as expected
    assert A == 5.0
    assert B == 10.0

def test_main(monkeypatch, capfd):
    # Simulate user input for get_numbers()
    inputs = iter([15.0, 3.0])  # Simulate A = 15, B = 3

    # Use monkeypatch to mock input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the main function, which will use the simulated inputs and print the output
    main()

    # Capture the printed output
    captured = capfd.readouterr()

    # Manually compute the expected values
    expected_subtraction = 15.0 - 3.0  # 12.0
    expected_multiplication = 15.0 * 3.0  # 45.0
    expected_division = 15.0 / 3.0  # 5.0

    # Define the expected output string
    expected_output = f"subtraction = {expected_subtraction}, multiplication = {expected_multiplication}, division = {expected_division}\n"

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output
