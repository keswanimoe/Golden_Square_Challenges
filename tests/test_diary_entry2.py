# Unit testing for lib/diary_entry2.py
from lib.diary_entry2 import *

def test_diary_entry2_can_be_instantiated():
    entry = DiaryEntry2('My Title', 'These are the contents')
    assert isinstance(entry, DiaryEntry2) == True
    
def test_initialise_with_title_and_contents():
    entry = DiaryEntry2('My Title', 'These are the contents')
    actual_title = entry.title
    actual_contents = entry.contents
    
    expected_title = 'My Title'
    expected_comtents = 'These are the contents'
    
    assert actual_title == expected_title
    assert actual_contents == expected_comtents
    
def test_returns_contents_word_count():
    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.count_words()
    expected = 4

    assert actual == expected
    
def tests_returns_reading_time():
    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_time(4)
    expected = 1

    assert actual == expected  

def test_returns_a_chunk_of_contents():
    entry = DiaryEntry2('My Title', 'These are the contents')
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    assert actual == expected
    
def test_returns_next_chunk_of_contents():
    entry = DiaryEntry2('My Title', 'These are the contents')
    entry.reading_chunk(3, 1)
    actual = entry.reading_chunk(3, 1)
    expected = 'contents'
    assert actual == expected
    
def test_end_of_chunk_restarts():
    entry = DiaryEntry2('My Title', 'These are the contents')
    entry.reading_chunk(3, 1)
    entry.reading_chunk(3, 1)
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    assert actual == expected