# previously I have already created diary_entry class system 
# so I have named this diary_entry2

# File: lib/diary_entry2.py

class DiaryEntry2:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.placeholder = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        slice = self.contents.split(" ")
        return len(slice)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        words = self.count_words()
        mins = int(words/wpm)
        return mins

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words = self.contents.split()
        if self.placeholder >= len(words):
            self.placeholder = 0
        
        words_read = wpm*minutes
        chunk = " ".join(words[self.placeholder:words_read+self.placeholder])
        self.placeholder += words_read
        return chunk