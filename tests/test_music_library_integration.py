# File: tests/test_music_library_integration.py

## Tests for multiple classes acting together are called integration tests (also known as feature tests)
## Tests for a single method or class are called unit tests
from lib.music_library import MusicLibrary
from lib.track import Track

def test_returns_tracks_as_list():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.library == [track_1, track_2]

def test_searches_by_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Always The Hard Way") == [track_1]

def test_searches_by_title_track_2():
    library = MusicLibrary() 
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Higher Place") == [track_2] 

def test_searches_by_word_in_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Way") == [track_1]
