'''stop()
Stops both motors simultaneously, which will stop a Driving Base.
The motors will either actively hold their current position or coast freely depending on the option that’s been selected by set_stop_action().
Errors
RuntimeError
One or both of the motors has been disconnected or the motors could not be paired.
Example
'''
from spike import MotorPair
import time

def test_stop():
    # Create a MotorPair object with the motors you want to control
    # For example, using motors on ports A and B
    motor_pair = MotorPair('A', 'B')

    # Start the motors at a speed of 50% for 2 seconds
    motor_pair.start(50)
    time.sleep(2)

    # Stop the motors
    motor_pair.stop()
