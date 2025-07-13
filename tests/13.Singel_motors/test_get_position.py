'''get_position()
Retrieves the motor position. This is the clockwise angle between the moving marker and the zero-point marker on the motor.
Returns
The motor’s position.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 359 degrees
Errors
RuntimeError
The motor has been disconnected from the Port.
'''
from spike import Motor

def test_motor_get_position():
    # Create a motor object (assuming the motor is connected to port 'A')
    motor = Motor('A')

    # Run the motor 90 degrees clockwise
    motor.run_for_degrees(90)

    # Get the position of the motor
    position = motor.get_position()

    # Print the position
    print("Motor position:", position)
