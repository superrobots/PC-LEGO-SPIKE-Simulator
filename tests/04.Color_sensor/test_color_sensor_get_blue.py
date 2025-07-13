'''get_blue()
Retrieves the color intensity of blue.
Returns
Type:integer (a positive or negative whole number, including 0)
Values:0 to 1024
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor
import time

def test_color_sensor_get_blue():
    # Initialize the Color Sensor

    paper_scanner = ColorSensor('E')
    assert paper_scanner.get_blue()