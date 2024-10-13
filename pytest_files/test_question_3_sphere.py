# test_geometry.py
import pytest
from question_3_sphere import volume_sphere, main
from math import pi

def test_volume_sphere():
    # Test case 1: radius=3
    radius = 3
    expected_volume = 4/3 * pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected_volume)

    # Test case 2: radius=0 (edge case)
    radius = 0
    expected_volume = 0
    assert volume_sphere(radius) == pytest.approx(expected_volume)
    
    # Test case 3: radius=1 (basic test)
    radius = 1
    expected_volume = 4/3 * pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected_volume)

    # Test case 4: radius=2.5 (decimal radius)
    radius = 2.5
    expected_volume = 4/3 * pi * radius ** 3
    assert volume_sphere(radius) == pytest.approx(expected_volume)

def test_main(monkeypatch, capfd):
    # Simulate user input: radius = 3
    monkeypatch.setattr('builtins.input', lambda _: '3')
    
    # Run the main function
    main()
    
    # Capture printed output
    captured = capfd.readouterr()
    
    # Expected output for radius = 3
    expected_output = "Isipadu sfera = 113.10\n"  # volume for radius=3 is about 113.097
    
    # Assert that printed output matches expected output
    assert captured.out == expected_output