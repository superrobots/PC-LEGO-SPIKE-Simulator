from spike import PrimeHub


def test_left_button_wait_until_pressed():
    hub = PrimeHub()

    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep()
    print('pressed')
    hub.left_button.wait_until_released()
    hub.speaker.stop()
    print('released')