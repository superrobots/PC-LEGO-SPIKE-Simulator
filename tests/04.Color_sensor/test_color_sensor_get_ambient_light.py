'''
get_ambient_light()
Retrieves the intensity of the ambient light.
This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in ambient light mode.

Returns
The ambient light intensity.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100 %
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
import time
from spike import ColorSensor

def test_color_sensor_get_ambient_light():
    """
    Test the get_ambient_light() method of the ColorSensor class.
    """

    # Initialize the Color Sensor

    paper_scanner = ColorSensor('E')


    # Measure the light
    for x in range(200):
        light = paper_scanner.get_ambient_light()

 

