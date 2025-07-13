'''on(color='white')
Sets the color of the light.
Parameters
color
Illuminates the Hub’s Brick Status Light in the specified color.
Type:String (text)
Values:"azure","black","blue","cyan","green","orange","pink","red","violet","yellow","white"
Default:"white"
Errors
TypeError
color is not a string.
ValueError
color is not one of the allowed values.
Example
'''
from spike import PrimeHub
import time

def test_on():
    """Test the on method of the Status Light."""
    # Create a PrimeHub instance
    hub = PrimeHub()
    # Test the on method with different colors
    colors = ["azure", "black", "blue", "cyan", "green", "orange", "pink", "red", "violet", "yellow", "white"]
    for color in colors:
        hub.status_light.on(color)
        time.sleep(1)  # Sleep for 1 second between color changes
