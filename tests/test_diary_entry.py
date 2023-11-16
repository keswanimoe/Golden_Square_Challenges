from lib.diary_entry import *

entry = DiaryEntry('My Title', 'These are the contents')
def test_diary_entry_can_be_instantiated():
    assert isinstance(entry, DiaryEntry)

def test_initialises_with_title_and_contents():
    actual_title = entry.title
    actual_contents = entry.contents
    
    expected_title = 'My Title'
    expected_comtents = 'These are the contents'
    
    assert actual_title == expected_title
    assert actual_contents == expected_comtents
    
def test_returns_formatted_diary_entry():    
    actual = entry.format()
    expected = "My Title: These are the contents"
    
    assert actual == expected
    
def test_returns_contents_word_count():
    actual = entry.count_words()
    expected = 6
    
    assert actual == expected
    
def test_returns_estimate_reading_time():
    actual = entry.reading_time(200)
    expected_mins = 6/200
    expected = f'{expected_mins} minutes'
    
    assert actual == expected
    
def test_returns_a_chunk_of_contents():
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    assert actual == expected
    
def test_returns_next_chunk_of_contents():
    actual = entry.reading_chunk(3, 1)
    expected = 'contents'
    assert actual == expected
    
def test_end_of_chunk_restarts():
    actual = entry.reading_chunk(3, 1)
    expected = 'These are the'
    assert actual == expected