# Define an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task from the to-do list
def remove_task():
    display_tasks()
    if tasks:
        try:
            index = int(input("Enter the index of the task you want to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input! Please enter a valid integer index.")
    else:
        print("Nothing to remove!")

# Main function to run the program
def main():
    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Thank you for using the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number from 1 to 4.")

if __name__ == "__main__":
    main()
