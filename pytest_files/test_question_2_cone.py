import pytest
from question_2_cone import *
from math import pi

def test_volume_cone():
    # Test case 1: radius=3, height=5
    radius = 3
    height = 5
    expected_volume = 1/3 * pi * radius ** 2 * height
    assert volume_cone(radius, height) == pytest.approx(expected_volume)
    
    # Test case 2: radius=0 (edge case), height=7
    radius = 0
    height = 7
    expected_volume = 0
    assert volume_cone(radius, height) == pytest.approx(expected_volume)
    
    # Test case 3: radius=2, height=4 (a random case)
    radius = 2
    height = 4
    expected_volume = 1/3 * pi * radius ** 2 * height
    assert volume_cone(radius, height) == pytest.approx(expected_volume)

def test_main(monkeypatch, capfd):
    # Simulate user input for radius and height using monkeypatch
    inputs = iter(["3", "5"])  # Test case: radius = 3, height = 5
    
    # Replace input() with our simulated inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Call the main() function
    main()
    
    # Capture the output printed by main() using capfd
    captured = capfd.readouterr()
    
    # Check if the output matches the expected value
    expected_output = "Volume of cone = 47.12\n"
    assert captured.out == expected_output