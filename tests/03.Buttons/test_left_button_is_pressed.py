from spike import PrimeHub
from spike.control import wait_for_seconds

def test_left_button_is_pressed():
    hub = PrimeHub()

    for x in range(20):
        wait_for_seconds(0.1)
        if hub.left_button.is_pressed():
            print('left button is pressed')
        if hub.right_button.is_pressed():
            print('right button is pressed')