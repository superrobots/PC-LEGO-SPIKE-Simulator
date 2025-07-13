'''
get_reflected_light()
Retrieves the intensity of the reflected light.
Returns
The reflected light intensity.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100 %
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor

def test_get_reflected_light():
    """
    Test the get_reflected_light method of the ColorSensor class.
    This test checks if the method returns a value between 0 and 100.
    """
    # Initialize the Color Sensor
    paper_scanner = ColorSensor('E')

    # Measure the color reflected_light
    reflected_light = paper_scanner.get_reflected_light()

    # Check if the reflected_light is within the expected range
    assert 0 <= reflected_light <= 100, f"Reflected light intensity out of range: {reflected_light}"
