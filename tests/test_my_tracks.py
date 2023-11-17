from lib.my_tracks import *

tracks = MyTracks()

def test_my_tracks_can_be_instantiated():
    assert isinstance(tracks, MyTracks)
    
def test_my_tracks_attribute():
    actual = tracks.songs
    expected = []
    assert actual == expected
    
def test_track_can_be_added():
    tracks.add('my song')
    result = len(tracks.songs)
    expected = 1
    assert result == expected
    
def test_list_tracks():
    result = tracks.list()
    expected = ['my song']
    assert result == expected