from spike import ColorSensor
import pytest
@pytest.mark.skipif(True, reason="wait_until_color takes too long")
def test_color_sensor_wait_until_color():
    color_sensor = ColorSensor('A')

    color_sensor.wait_until_color('white')
    assert color_sensor.get_ambient_light()
    assert color_sensor.get_blue() == 0
    assert color_sensor.get_green() == 0
    assert color_sensor.get_red() == 0
    assert color_sensor.get_color() == 'white'
