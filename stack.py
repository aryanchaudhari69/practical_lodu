undo_stack = []
redo_stack = []

document = " "

while True:
    print("\n1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document State")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        new_text = input("Enter new document text: ")

        undo_stack.append(document)

        document = new_text

        redo_stack.clear()

        print("Change made successfully")

    elif choice == 2:
        if undo_stack:
            redo_stack.append(document)
            document = undo_stack.pop()
            print("Undo successful")
        else:
            print("Nothing to undo")

    elif choice == 3:
        if redo_stack:
            undo_stack.append(document)
            document = redo_stack.pop()
            print("Redo successful")
        else:
            print("Nothing to redo")

    elif choice == 4:
        print("Current Document State:")
        print(document)

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")