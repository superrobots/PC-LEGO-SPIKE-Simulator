'''
get_default_speed()
Retrieves the current default motor speed.
Returns
The default motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:(-100% to 100%).
'''
from spike import Motor

def test_get_default_speed():
    '''
    Test the get_default_speed() method of the Motor class.
    '''
    motor = Motor('A')

    print(str(motor.get_default_speed()))