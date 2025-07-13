from spike.control import Timer


def test_timer_now():
    timer = Timer()

    while True:
        # If it has been more than 5 seconds since the Timer started
        if timer.now() > 5:
            # then break out of the while loop
            break