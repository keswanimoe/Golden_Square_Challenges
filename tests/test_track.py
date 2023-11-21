# unit tests for lib/track
from lib.track import Track

def test_construct_track_and_get_title():
    track = Track("My Title", "My Artist")
    assert track.title == "My Title" 
    
def test_formats_title_and_artist():
    track = Track("My Title", "My Artist")
    assert track.format() == "My Title by My Artist"