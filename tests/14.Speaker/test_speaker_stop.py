'''stop()
Stops any sound that is playing.
Example
'''
from spike import PrimeHub

def test_speaker_stop():
    '''stop()'''
    # Create a PrimeHub object
    hub = PrimeHub()

    hub.speaker.start_beep()

    # Do something

    hub.speaker.stop()
