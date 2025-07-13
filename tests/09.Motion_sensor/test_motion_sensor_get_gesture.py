'''get_gesture()
Retrieves the most recently-detected gesture.
Returns
The gesture.
Type:String (text)
Values:'shaken','tapped','doubletapped','falling'
Example
'''
from spike import PrimeHub


def test_motion_sensor_get_gesture():
	hub = PrimeHub()
	assert hub.motion_sensor.get_gesture() != 'falling'
	