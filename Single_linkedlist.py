class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        print("Student added successfully")

    def delete(self, roll):
        temp = self.head
        prev = None

        while temp:
            if temp.roll == roll:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                print("Student deleted successfully")
                return

            prev = temp
            temp = temp.next

        print("Student not found")

    def update(self, roll):
        temp = self.head

        while temp:
            if temp.roll == roll:
                temp.name = input("Enter new name: ")
                temp.marks = float(input("Enter new marks: "))
                print("Student updated successfully")
                return

            temp = temp.next

        print("Student not found")

    def search(self, roll):
        temp = self.head

        while temp:
            if temp.roll == roll:
                print("Student Found")
                print("Roll No:", temp.roll)
                print("Name:", temp.name)
                print("Marks:", temp.marks)
                return

            temp = temp.next

        print("Student not found")

    def display(self):
        if self.head is None:
            print("No records available")
            return

        temp = self.head

        print("\nStudent Records:")
        while temp:
            print(temp.roll, temp.name, temp.marks)
            temp = temp.next

    def sort(self, field, order):
        if self.head is None:
            return

        current = self.head

        while current:
            index = current.next

            while index:
                swap = False

                if field == "roll":
                    if order == "asc" and current.roll > index.roll:
                        swap = True
                    elif order == "desc" and current.roll < index.roll:
                        swap = True

                elif field == "marks":
                    if order == "asc" and current.marks > index.marks:
                        swap = True
                    elif order == "desc" and current.marks < index.marks:
                        swap = True

                if swap:
                    current.roll, index.roll = index.roll, current.roll
                    current.name, index.name = index.name, current.name
                    current.marks, index.marks = index.marks, current.marks

                index = index.next

            current = current.next

        print("Records sorted successfully")


students = StudentList()

while True:
    print("\n1. Add")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Display")
    print("6. Sort")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students.add(roll, name, marks)

    elif choice == 2:
        roll = int(input("Enter Roll No to delete: "))
        students.delete(roll)

    elif choice == 3:
        roll = int(input("Enter Roll No to update: "))
        students.update(roll)

    elif choice == 4:
        roll = int(input("Enter Roll No to search: "))
        students.search(roll)

    elif choice == 5:
        students.display()

    elif choice == 6:
        print("Sort by:")
        print("1. Roll No")
        print("2. Marks")

        sort_choice = int(input("Enter choice: "))

        print("1. Ascending")
        print("2. Descending")

        order_choice = int(input("Enter choice: "))

        field = "roll" if sort_choice == 1 else "marks"
        order = "asc" if order_choice == 1 else "desc"

        students.sort(field, order)
        students.display()

    elif choice == 7:
        print("Program ended")
        break

    else:
        print("Invalid choice")