
import json

class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            return removed_task["task"]
        except IndexError:
            return None

    def mark_completed(self, index):
        try:
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            return self.tasks[index - 1]["task"]
        except IndexError:
            return None

    def show_tasks(self):
        print("\nCurrent To-Do List:")
        if not self.tasks:
            print("Your To-Do List is empty!")
            return
        for i, item in enumerate(self.tasks, 1):
            status = "Done" if item["completed"] else "Pending"
            print(f"{i}. {item['task']} - [Status: {status}]")

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List App!")

    while True:
        todo_list.show_tasks()
        print("\nOptions: add <task>, remove <index>, complete <index>, exit")
        action = input("What would you like to do? ").strip()

        if action.startswith('add '):
            task = action[4:]
            todo_list.add_task(task)
            print(f"Added task: {task}")
        elif action.startswith('remove '):
            try:
                index = int(action[7:])
                removed_task = todo_list.remove_task(index)
                if removed_task:
                    print(f"Removed task: {removed_task}")
                else:
                    print("No task found at the given index.")
            except ValueError:
                print("Please enter a valid number for task index.")
        elif action.startswith('complete '):
            try:
                index = int(action[9:])
                completed_task = todo_list.mark_completed(index)
                if completed_task:
                    print(f"Marked task as completed: {completed_task}")
                else:
                    print("No task found at the given index.")
            except ValueError:
                print("Please enter a valid number for task index.")
        elif action == 'exit':
            print("Saving tasks...")
            todo_list.save_tasks()
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()


