'''set_motor_rotation(amount, unit='cm')
Sets the ratio of one motor rotation to the distance traveled.
If there are no gears used between the motors and the wheels of the Driving Base, the "amount" is the circumference of one wheel.
Calling this method does not affect the Driving Base if it’s already running. It will only have an effect the next time one of the move or start methods is used.
Parameters
amount
The distance that the Driving Base moves when both motors move one rotation each.
Type:float (decimal number)
Values:any value
Default:17.6
unit
The unit of measurement specified for the "amount" parameter.
Type:String (text)
Values:"cm","in"
Default:cm
Errors
TypeError
amount is not a number or unit is not a string.
ValueError
unit is not one of the allowed values.
Example
'''
import math
from spike import MotorPair

def test_set_motor_rotation():
    # Create a MotorPair object with ports 'A' and 'B'
    motor_pair = MotorPair('B', 'A')

    # Set the motor rotation to 17.6 cm
    motor_pair.set_motor_rotation(17.6, 'cm')

    # Check if the motor rotation is set correctly
    assert motor_pair.motor_pair.amount == 17.6, "Motor rotation not set correctly"
    assert motor_pair.motor_pair.unit == 'cm', "Unit not set correctly"
