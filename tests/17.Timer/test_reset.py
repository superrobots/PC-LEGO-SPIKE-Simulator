from spike.control import Timer
def test_timer_reset():
    timer = Timer()
    # After some time...
    timer.reset()