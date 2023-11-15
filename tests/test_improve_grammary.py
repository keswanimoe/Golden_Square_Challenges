from lib.improve_grammar import *

def test_improve_grammar_returns_false():
    result = improve_grammar('This is a sentence')
    assert result == False

def test_improve_grammar_returns_true():
    result = improve_grammar('This is a sentence.')
    assert result == True
    
def test_improve_grammar_returns_false_caps():
    result = improve_grammar('this is a sentence.')
    assert result == False