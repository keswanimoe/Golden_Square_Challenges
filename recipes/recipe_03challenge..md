1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

def check_todo(text):
    pass

Name: check_todo
Parameters: one, a string
Returns: True or False
Side Effects: no side effects, nothing is printed to the terminal

3. Create Examples as Tests
Make a list of examples of what the function will take and return

check_todo('#TODO Laundry') == True
check_todo('TODO Laundry') == False
check_todo('To do: Laundry') == False
check_todo('#TODO Laundry, Dishes') == True

4.  Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

e.g.

from lib.check_todo import *

def test_check_todo_returns_true():
    result = check_todo('#TODO Laundry') 
    assert result == True

