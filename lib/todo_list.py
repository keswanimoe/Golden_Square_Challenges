# File: lib/todo.py
# File: lib/todo_list.py
from lib.todo import *

class TodoList:
    def __init__(self):
        self.to_do_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        if isinstance(todo, Todo):
            self.to_do_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [task for task in self.to_do_list if task.complete == False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [task for task in self.to_do_list if task.complete == True]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.to_do_list:
            if task.complete == False:
                task.complete = True