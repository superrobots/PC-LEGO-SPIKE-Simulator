from spike import ForceSensor
from spike.control import wait_for_seconds


def test_force_sensor_is_pressed():
    # Initialize the Force Sensor
   door_bell = ForceSensor('E')

    # Measure the force in newtons or as a percentage
   door_bell.is_pressed()