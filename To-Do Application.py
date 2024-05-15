import csv
from datetime import datetime

# Function to load tasks from the file
def load_tasks(file_name):
    tasks = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(row)
    except FileNotFoundError:
        pass
    return tasks

# Function to save tasks to the file
def save_tasks(tasks, file_name):
    with open(file_name, 'w', newline='') as file:
        fieldnames = tasks[0].keys() if tasks else []
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tasks)

# Function to add a task
def add_task(tasks):
    name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({'name': name, 'priority': priority, 'due_date': due_date, 'completed': 'No'})

# Function to remove a task
def remove_task(tasks):
    print("Tasks:")
    display_tasks(tasks)
    index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
    else:
        print("Invalid index")

# Function to mark a task as completed
def complete_task(tasks):
    print("Tasks:")
    display_tasks(tasks)
    index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = 'Yes'
    else:
        print("Invalid index")

# Function to display tasks
def display_tasks(tasks):
    for index, task in enumerate(tasks, 1):
        print(f"{index}. [{task['completed']}] {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

# Main function
def main():
    file_name = "tasks.csv"
    tasks = load_tasks(file_name)

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. View Tasks\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks, file_name)
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
