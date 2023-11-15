from lib.check_todo import *

def test_check_todo_returns_true():
    result = check_todo('#TODO Laundry') 
    assert result == True
    
def test_check_todo_returns_true():
    result = check_todo('TODO Laundry') 
    assert result == False
    
def test_check_todo_returns_true():
    result = check_todo('To do: Laundry') 
    assert result == False
    
def test_check_todo_returns_true():
    result = check_todo('#TODO Laundry, Dishes') 
    assert result == True