'''wait_for_new_gesture()
Waits until a new gesture happens.
Returns
The new gesture.
Type:String (text)
Values:'shaken','tapped','doubletapped','falling'
Example
'''
from spike import PrimeHub

def test_motion_sensor_wait_for_new_gesture():
    hub = PrimeHub()

    gesture = hub.motion_sensor.wait_for_new_gesture()
    assert gesture in ['shaken', 'tapped', 'doubletapped', 'falling'], "Gesture not recognized"

