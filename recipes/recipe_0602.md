## 1. Describe the Problem
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

name: my_task_checklist

method: add_todo 
parameters: 2 strings, one containing the task and another detailing the task 
returns: nothing

method: list_tasks 
parameters: none 
returns: the tasks

method: mark_complete, removes completed task
parameters: dictionary key
returns: nothing