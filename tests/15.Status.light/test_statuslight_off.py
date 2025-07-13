'''off()
Turns off the light.
Example'''
from spike import PrimeHub

def test_status_light_off():
    hub = PrimeHub()

    hub.status_light.off()