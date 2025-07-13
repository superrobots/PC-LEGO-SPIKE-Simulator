'''get_speed()
Retrieves the motor speed.
Returns
The motor’s current speed
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%
Errors
RuntimeError
The motor has been disconnected from the Port
'''

from spike import Motor

def test_get_speed():
    '''
    Test the get_speed() method of the Motor class.
    '''
    # Create a motor object on port A
    motor = Motor('A')

    # Set the motor speed to 50%
    motor.run_for_degrees(90, 50)

    # Get the current speed of the motor
    speed = motor.get_speed()

    # Check if the speed is equal to 50%
    assert speed == 50, f"Expected speed: 50, but got: {speed}"

