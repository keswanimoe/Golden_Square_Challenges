from lib.todo import *
from lib.todo_list import *

def test_adds_an_instance_of_to_do():
    my_list = TodoList()
    my_task = Todo("Laundry")
    my_list.add(my_task)
    result = my_list.to_do_list
    expected = [my_task]
    assert result == expected
    
def test_verify_added_is_instance_of_to_do():
    my_list = TodoList()
    my_task = "Laundry"
    my_list.add(my_task)
    result = my_list.to_do_list
    expected = []
    assert result == expected
    
def test_initially_list_marked_as_incomplete():
    my_list = TodoList()
    my_task = Todo("Laundry")
    my_list.add(my_task)
    result = my_list.incomplete()
    expected = [my_task]
    assert result == expected

def test_mark_complete_updates_complete_list():
    my_list = TodoList()
    my_task = Todo("Laundry")
    my_list.add(my_task)
    
    result = my_list.complete()
    expected = []
    assert result == expected
    
    my_task.mark_complete()
    result = my_list.complete()
    expected = [my_task]
    assert result == expected
    
def test_incomplete_list_updated():
    my_list = TodoList()
    my_task = Todo("Laundry")
    my_list.add(my_task)
    
    result = my_list.incomplete()
    expected = [my_task]
    assert result == expected
    
    my_task.mark_complete()
    result = my_list.incomplete()
    expected = []
    assert result == expected
        
def test_give_up_marks_all_todos_as_complete():
    my_list = TodoList()
    my_task = Todo("Laundry")
    my_list.add(my_task)
    my_list.give_up()
    result = my_list.complete()
    expected = [my_task]
    assert result == expected