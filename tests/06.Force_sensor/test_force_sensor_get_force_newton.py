from spike import ForceSensor
from spike.control import wait_for_seconds
from visualization import HubVisualizer

def test_force_sensor_get_force_newton():
    """
    Test the get_force_newton() method of the ForceSensor class.
    This function initializes a ForceSensor object and retrieves the force in newtons.
    """
    # Initialize the Force Sensor
    door_bell = ForceSensor('E')

    # Measure the force in newtons
    newtons = door_bell.get_force_newton()
    print(f"Force measured: {newtons}N")
