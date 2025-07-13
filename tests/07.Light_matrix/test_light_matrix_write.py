# write(text)
# Displays text on the Light Matrix, one letter at a time, scrolling from right to left.
# Your program will not continue until all of the letters have been shown.
# Parameters
# text
# Text to write.
# Type
# :
# String (text)
# Values
# :
# Any text
# Default
# :
# no default value
# Example
from spike import PrimeHub

def test_light_matrix_write():
    # Create a PrimeHub object
    hub = PrimeHub()

    # Show the text "Hello!" on the Light Matrix
    hub.light_matrix.write('Hello!')

    hub.light_matrix.write('1')
