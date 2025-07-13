'''get_orientation()
Retrieves the Hub's current orientation.
Returns
The Hub’s current orientation.
Type:String (text)
Values:'front','back','up','down','leftside','rightside'
Example
'''
from spike import PrimeHub

def test_motion_sensor_get_orientation():
    '''get_orientation()
    Retrieves the Hub's current orientation.
    Returns
    The Hub’s current orientation.
    Type:String (text)
    Values:'front','back','up','down','leftside','rightside'
    Example
    '''
    hub = PrimeHub()

    assert hub.motion_sensor.get_orientation() in ['front', 'back', 'up', 'down', 'leftside', 'rightside'], "Orientation is not valid"
