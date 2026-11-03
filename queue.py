from collections import deque

event_queue = deque()

while True:
    print("\n1. Add Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel Event")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        event = input("Enter event name: ")
        event_queue.append(event)
        print("Event added successfully")

    elif choice == 2:
        if event_queue:
            event = event_queue.popleft()
            print("Processed event:", event)
        else:
            print("No pending events")

    elif choice == 3:
        if event_queue:
            print("Pending Events:")
            for event in event_queue:
                print(event)
        else:
            print("No pending events")

    elif choice == 4:
        event = input("Enter event to cancel: ")

        if event in event_queue:
            event_queue.remove(event)
            print("Event cancelled successfully")
        else:
            print("Event not found")

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")