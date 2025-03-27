tasks = []

def showtasks():
    if not tasks:
        print("task is not found.")
    else:
        for i in tasks:
            print(i)

def addtask(name):
    tasks.append(name)
    print("Task is added", name)

def removetask(name):
    if name in tasks:
        tasks.remove(name)
        print("Task is removed:", name)
    else:
        print("Task  is not found.")

def sorttasks():
    tasks.sort()
    print("Tasks is  sorted.")

while True:
    print("1. Show the Tasks")
    print("2. Add the Task")
    print("3. Remove the Task")
    print("4. Sort the Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        showtasks()
    elif choice == '2':
        name = input("Enter the task: ")
        addtask(name)
    elif choice == '3':
        name = input("Enter the task to remove it: ")
        removetask(name)
    elif choice == '4':
        sorttasks()
    elif choice == '5':
        print("thankyou")
        break
    else:
        print("Invalid choice.")
    print()
