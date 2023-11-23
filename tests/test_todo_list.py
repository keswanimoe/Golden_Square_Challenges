from lib.todo_list import *

def test_todo_list_can_be_instantiated():
    my_list = TodoList()
    assert isinstance(my_list, TodoList)
    
def test_initialise_a_todo_list():
    my_list = TodoList()
    result = my_list.to_do_list
    expected = []
    assert result == expected

def test_initially_incomplete_list_is_empty():
    my_list = TodoList()
    result = my_list.incomplete()
    expected = []
    assert result == expected
    
def test_initially_complete_list_is_empty():
    my_list = TodoList()
    result = my_list.complete()
    expected = []
    assert result == expected
    
    