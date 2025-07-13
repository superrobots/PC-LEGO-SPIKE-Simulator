'''
get_rgb_intensity()
Retrieves the overall color intensity, and intensity of rgb_intensity, green, and blue.
Returns
Type:tuple of int
Values:rgb_intensity, green, blue, and overall intensity (0-1024)
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor

def test_get_rgb_intensity():
    # Initialize the Color Sensor

    paper_scanner = ColorSensor('E')

    paper_scanner.get_rgb_intensity()

