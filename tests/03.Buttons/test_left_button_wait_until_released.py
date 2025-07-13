from spike import PrimeHub

def test_left_button_wait_until_released():
    hub = PrimeHub()


    # Beep every time the Left Button is pressed

    
    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep()
    hub.left_button.wait_until_released()
    hub.speaker.stop()