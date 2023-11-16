class MyTasks():
    def __init__(self):
        self.all_tasks = {}
    
    def add_todo(self, task, description):
        self.all_tasks[task] = description
    
    def list_tasks(self):
        return list(self.all_tasks.keys())