'''get_distance_cm(short_range=False)
Retrieves the measured distance in centimeters.
Parameters
short_range
Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
Type:boolean
Values:True or False
Default:False
Returns
The measured distance or "none" if the distance can't be measured.
Type:float (decimal number)
Values:0 to 200 cm
Errors
TypeError
short_range is not a boolean.
RuntimeError
The sensor has been disconnected from the Port.
Example'''
from spike import DistanceSensor
import time

def test_distance_sensor_get_distance_cm():
    # Initialize the Distance Sensor

    wall_detector = DistanceSensor('E')
    dist_cm = wall_detector.get_distance_cm()
    dist_inches = wall_detector.get_distance_inches()
    # Print both results to the console
    print('cm:', dist_cm, 'Inches:', dist_inches)

