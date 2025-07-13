'''was_stalled()
Tests whether the motor was stalled.
Returns
True if the motor has stalled since the last time was_stalled() was called, otherwise false.
Type:Boolean
Values:True or False
Errors
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor

def test_was_stalled():
    # Create a motor object for motor A
    motor = Motor('A')

    # Enable stall detection
    motor.set_stall_detection(True)

    # Run the motor for 2 rotations
    motor.run_for_rotations(2)

    # Check if the motor was stalled
    assert motor.was_stalled() == False, "Motor should not be stalled after running for 2 rotations"