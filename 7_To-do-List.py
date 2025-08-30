import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks found.\n")
    else:
        print("\n📌 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added!\n")

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"🗑️ Task '{removed}' deleted!\n")
                else:
                    print("⚠️ Invalid task number!\n")
            except ValueError:
                print("⚠️ Please enter a valid number!\n")

        elif choice == "4":
            print("👋 Goodbye! Tasks saved.")
            break

        else:
            print("⚠️ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
