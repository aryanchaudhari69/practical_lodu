class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

    def display(self, root):
        if root:
            self.display(root.left)
            print(root.data, end=" ")
            self.display(root.right)

    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

bst = BST()
root = None

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        root = bst.insert(root, data)
        print("Inserted successfully")

    elif choice == 2:
        data = int(input("Enter value to delete: "))
        root = bst.delete(root, data)
        print("Deletion completed")

    elif choice == 3:
        data = int(input("Enter value to search: "))

        if bst.search(root, data):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("BST Inorder Traversal:")
        bst.display(root)
        print()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")
