from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet('A string of six different words')
    assert result == 'A string of six different...'

def test_make_snippet_return_sentence():
    result = make_snippet('This is a test')
    assert result == 'This is a test'