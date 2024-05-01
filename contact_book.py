contact = []
def add():
    name = input("Enter your Name ")
    num = input("Enter your number")
    contact.append(num)
    contact.append(name)
    print(f"Contact' {contact} 'added successfully!")


def disply():
   if not contact:
        print("Your contact is empty!")
   else:
        print("Contacts :")
        for i, task in enumerate(contact, 1):
            print(f"{i}. {task}")

  

def delete():
    add()
    if contact:
        try:
            index = int(input("Enter the index of the task you want to remove: ")) - 1
            if 0 <= index < len(contact):
                removed_task = contact.pop(index)
                print(f"Task '{delete}' removed successfully!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input! Please enter a valid integer index.")
    else:
        print("Nothing to remove!")


def main():
    while True:
        print("\nOptions:")
        print("1. Enter name|number")
        print("2. disply a details")
        print("3. Remove a details")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add()
        elif choice == '2':
            disply()
        elif choice == '3':
            delete()
        elif choice == '4':
            print("Thank you for using the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
    add()
    disply()
    delete()
