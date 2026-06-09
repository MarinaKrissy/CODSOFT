def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added successfully.")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to delete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    number = int(input("Enter task number to delete: "))
                    if 1 <= number <= len(tasks):
                        removed_task = tasks.pop(number - 1)
                        print(f"Deleted: {removed_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()