from lib.my_tasks import *

tasks = MyTasks()
def test_my_tasks_can_be_instantiated():
    assert isinstance(tasks, MyTasks)
    
def test_my_tasks_instantiates_with_ability_to_store_tasks():
    actual = tasks.all_tasks
    expected = {}
    assert actual == expected
    
def test_add_todo_task():
    tasks.add_todo('Laundry', 'Seperate whites')
    actual = tasks.all_tasks['Laundry']
    expected = 'Seperate whites'
    assert actual == expected
    
def test_add_another_todo_task():
    tasks.add_todo('Cleaning', 'Clean my room')
    actual = len(tasks.all_tasks.keys())
    expected = 2
    assert actual == expected
    
def test_list_all_tasks():
    actual = tasks.list_tasks()
    expected = ['Laundry', 'Cleaning']
    assert actual == expected
    