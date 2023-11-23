from lib.todo import *

def test_todo_can_be_instanstiated():
    to_do = Todo("My Task")
    assert isinstance(to_do, Todo) == True
    

def test_task_property_is_set():
    to_do = Todo("My Task")
    actual = to_do.task
    expected = "My Task"
    assert actual == expected
    
def test_initially_complete_property_set_to_false():
    to_do = Todo("My Task")
    actual = to_do.complete
    expected = False
    assert actual == expected
    
def test_mark_complete_sets_complete_to_true():
    to_do = Todo("My Task")
    actual = to_do.mark_complete()
    actual = to_do.complete
    expected = True
    assert actual == expected