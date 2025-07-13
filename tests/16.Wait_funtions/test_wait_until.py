from spike import ColorSensor, Motor
from spike.control import wait_until

def test_wait_until():

    color_sensor = ColorSensor('A')
    motor = Motor('B')

    def red_or_position():
        return color_sensor.get_color() == 'red' or motor.get_position() > 90

    wait_until(red_or_position)
