import pytest
from lib.diary import *
from lib.diary_entry2 import *

def test_add_an_entry_to_diary():
    entries = Diary()
    entry = DiaryEntry2('My Title', 'These are the contents')
    entries.add(entry)
    actual = entries.diary
    expected = [entry]
    assert actual == expected
    
def test_returns_list_of_entries():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.all()
    expected = [entry1, entry2]
    assert actual == expected
    
def test_returns_word_count_for_all_entries():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.count_words()
    expected = 8
    assert actual == expected
    

def test_returns_estimate_reading_time_for_all():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents')
    entry2 = DiaryEntry2('A Title', 'This is the contents')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.reading_time(4)
    expected = 2
    assert actual == expected
    
def test_find_best_reading_time_given_reading_speed():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry2('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.find_best_entry_for_reading_time(13, 1)
    expected = entry1
    assert actual == expected
    
    
def test_find_best_reading_time_given_reading_speed_again():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry2('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    entries.add(entry1)
    entries.add(entry2)
    actual = entries.find_best_entry_for_reading_time(16, 1)
    expected = entry2
    assert actual == expected
    
def test_best_reading_time_does_not_exist():
    entries = Diary()
    entry1 = DiaryEntry2('My Title', 'These are the contents of my diary which I write')
    entry2 = DiaryEntry2('A Title', 'This is the contents of my diary entry which I believe is fiften words long')
    entries.add(entry1)
    entries.add(entry2)
    with pytest.raises(Exception) as e: 
        entries.find_best_entry_for_reading_time(8, 1)
    error_message = str(e.value) 
    expected = "No entries can be read"
    assert error_message == expected