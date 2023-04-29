import sys

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added: ", task)
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed: ", task)
        else:
            print("Task not found: ", task)
    
    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found")
        else:
            print("Tasks:")
            for task in self.tasks:
                print("-", task)

def main():
    todo_list = TodoList()
    
    while True:
        command = input("Enter command (add/remove/show/quit): ")
        
        if command == "add":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif command == "remove":
            task = input("Enter task: ")
            todo_list.remove_task(task)
        elif command == "show":
            todo_list.show_tasks()
        elif command == "quit":
            sys.exit()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
