from spike import PrimeHub
from spike import ForceSensor
import time


def test_force_sensor_wait_until_pressed():
    """
    Test the ForceSensor wait_until_pressed() method.
    """
    # Create a PrimeHub and a ForceSensor object
    hub = PrimeHub()
    force_sensor = ForceSensor('A')

    # Wait until the force sensor is pressed
    force_sensor.wait_until_pressed()
    # Do something, for example, start the speaker beep
    hub.speaker.start_beep()
    print('pressed')
    # Wait until the force sensor is released
    force_sensor.wait_until_released()
    # Do something, for example, stop the speaker beep
    hub.speaker.stop()
    print('released')

