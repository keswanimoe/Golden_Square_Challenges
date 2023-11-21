# File: lib/music_library.py
from lib.track import Track
class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.library = []

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self.library.append(track)
    
    def all(self):
        return self.library
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        results = []
        for track in self.library:
            # this will get title since track is an instance of class Track
            if keyword in track.title:
                results.append(track)
        return results
        # refactored in list comprehension:
        # nts: remeber you can do this to create a new list without the extra step to create an empty list
        # list comprehension: [expression for item in iterable if condition == True]
        # return [
            # track 
            # for track in self.library 
            # if keyword in track.title 
        # ]