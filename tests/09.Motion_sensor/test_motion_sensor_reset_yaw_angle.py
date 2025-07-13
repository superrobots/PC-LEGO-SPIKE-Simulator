'''reset_yaw_angle()
Sets the yaw angle to "0."
'''

from spike import PrimeHub

def test_reset_yaw_angle():
    """
    Test the reset_yaw_angle() method of the motion_sensor class.
    This method is used to set the yaw angle to 0.
    """
    # Create an instance of PrimeHub
    hub = PrimeHub()

    hub.motion_sensor.reset_yaw_angle()
    angle = hub.motion_sensor.get_yaw_angle()
