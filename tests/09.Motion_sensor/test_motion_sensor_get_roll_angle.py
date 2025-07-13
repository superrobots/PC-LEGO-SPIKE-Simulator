'''get_roll_angle()
Retrieves the Hub’s roll angle.
Roll is the rotation around the front-back (longitudinal) axis. Yaw is the rotation around the front-back (vertical) axis. Pitch is the rotation around the left-right (transverse) axis.
Returns
The roll angle, specified in degrees.
Type:Integer (a positive or negative whole number, including 0)
Values:-180 to 180
Example
'''
from spike import PrimeHub

def test_motion_sensor_get_roll_angle():
    hub = PrimeHub()

    assert hub.motion_sensor.get_roll_angle() is not None, "get_roll_angle() should not return None"

