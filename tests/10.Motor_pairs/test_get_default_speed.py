'''get_default_speed()
Retrieves the default motor speed.
Returns
The default motor speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100 %
Settings
'''
from spike import MotorPair
def test_get_default_speed():
    '''get_default_speed()
    Retrieves the default motor speed.
    Returns
    The default motor speed.
    Type:integer (a positive or negative whole number, including 0)
    Values:-100 to 100 %
    Settings
    '''
    motor_pair = MotorPair('B', 'A')
    return motor_pair.get_default_speed()
