from spike import PrimeHub
from spike.control import wait_for_seconds

def test_left_button_was_pressed():
    hub = PrimeHub()

    
    if hub.left_button.was_pressed():
        print('button was pressed')
        # Do something