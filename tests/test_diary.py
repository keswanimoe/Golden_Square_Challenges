# Unit testing for lib/diary.py
from lib.diary import *

def test_diary_can_be_instantiated():
    entry = Diary()
    assert isinstance(entry, Diary) == True

def test_initialise_diary_is_empty_list():
    entry = Diary()
    actual = entry.diary
    expected = []
    assert actual == expected

def test_initially_returns_an_empty_list_for_all():
    entry = Diary()
    actual = entry.all()
    expected = []
    assert actual == expected  
        