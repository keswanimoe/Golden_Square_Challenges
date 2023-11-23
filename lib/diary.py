# File: lib/diary.py
from lib.diary_entry2 import *

class Diary:
    def __init__(self):
        self.diary = []
        self.words = []
        
    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.diary.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.diary

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        for entry in self.diary:
            self.words.append(entry.count_words())
        return sum(self.words)
        # can refactor using list comprehension:
        # words = [entry.count_words() for entry in self.diary]

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        mins = self.count_words()/wpm
        return int(mins)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        self.count_words()
        readable = wpm*minutes
        can_read = [x for x in self.words if x < readable]
        # [expression for item in iterable if condition]
        
        if can_read == []:
            raise Exception(f"No entries can be read")
        else:
        # find the index of the diary entry with the most words in can_read
            return self.diary[self.words.index(max(can_read))]