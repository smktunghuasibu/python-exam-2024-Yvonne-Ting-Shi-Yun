import pytest
from question_5_compound_interest import *

def test_cal_matured_value():
    # Test case 1: Basic scenario
    P = 1000  # Principal
    r = 5     # Rate of interest
    t = 10    # Time in years
    n = 1     # Compounding once per year (annually)
    expected_result = 1000 * (pow(1 + (5 / 100), 10))  # Manually calculate expected result
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

    # Test case 2: Quarterly compounding
    P = 1500
    r = 4
    t = 6
    n = 4  # Compounding quarterly
    expected_result = 1500 * (pow(1 + (4 / 100 / 4), 4 * 6))
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

    # Test case 3: Monthly compounding
    P = 2000
    r = 3
    t = 3
    n = 12  # Compounding monthly
    expected_result = 2000 * (pow(1 + (3 / 100 / 12), 12 * 3))
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

    # Test case 4: Daily compounding
    P = 5000
    r = 2
    t = 5
    n = 365  # Compounding daily
    expected_result = 5000 * (pow(1 + (2 / 100 / 365), 365 * 5))
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

    # Test case 5: Zero interest rate
    P = 1000
    r = 0  # No interest
    t = 5
    n = 12
    expected_result = 1000  # No interest, so result is just the principal
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

    # Test case 6: Zero time (instant compound)
    P = 1000
    r = 5
    t = 0  # No time has passed
    n = 12
    expected_result = 1000  # No time, so result is just the principal
    assert cal_matured_value(P, r, t, n) == pytest.approx(expected_result)

def test_get_inputs(monkeypatch):
    # Simulate user inputs using monkeypatch
    inputs = iter([1000, 5, 10, 4])  # These values will be returned by input() in sequence

    # Monkeypatch the input function to return values from our 'inputs' iterable
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Call the function, which will now use the simulated inputs
    p, r, t, n = get_inputs()

    # Assert the function returns the correct values based on simulated input
    assert p == 1000
    assert r == 5
    assert t == 10
    assert n == 4

def test_main(monkeypatch, capfd):
    # Simulate user inputs
    inputs = iter([1000, 5, 10, 4])  # Simulated input for P, R, T, N (Principal, Rate, Time, Compounding frequency)

    # Monkeypatch the input function to return values from our 'inputs' iterable
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Call the main function, which will use the simulated inputs and print the matured value
    main()

    # Capture printed output
    captured = capfd.readouterr()

    # Manually calculate the expected matured value using the same formula as cal_matured_value()
    expected_matured_value = 1000 * (pow(1 + (5 / 100 / 4), 4 * 10))

    # Check that the output contains the correctly formatted matured value
    expected_output = f"Matured value is {expected_matured_value:.2f}\n"
    assert captured.out == expected_output