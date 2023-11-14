from lib.count_words import *

def test_count_words():
    result = count_words('This is a test')
    assert result == 4