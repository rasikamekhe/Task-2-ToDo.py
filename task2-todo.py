def load_tasks(filename="tasks.txt"):
    #Load tasks from file into a list.
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks, filename="tasks.txt"):
    #Save all tasks to file.
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    #Display all tasks.
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):   
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    #Add a new task to the list.
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")


def remove_task(tasks):
    #Remove a task by its number.
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed task: '{removed}'")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


# Main

def main():
    tasks = load_tasks()

    while True:
        print("\n ___TO-DO LIST MENU___")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
