# off()
# Turns off all of the pixels on the Light Matrix.
# Example
from spike import PrimeHub

def test_light_matrix_off():
    """
    Test the light matrix off() method.
    """
    # Create a PrimeHub instance
    hub = PrimeHub()

    hub.light_matrix.off()
