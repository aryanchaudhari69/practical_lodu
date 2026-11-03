class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None or self.table[new_index] == "DELETED":
                self.table[new_index] = key
                print("Key inserted successfully")
                return

        print("Hash table is full")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index] == key:
                print("Key found at index", new_index)
                return

        print("Key not found")

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            new_index = (index + i) % self.size

            if self.table[new_index] is None:
                break

            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                print("Key deleted successfully")
                return

        print("Key not found")

    def display(self):
        print("\nHash Table:")

        for i in range(self.size):
            print(i, "->", self.table[i])




size = 10
ht = HashTable(size)

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        ht.insert(key)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == 4:
        ht.display()

    elif choice == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")