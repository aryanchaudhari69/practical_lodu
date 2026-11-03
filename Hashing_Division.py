class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                print("Key updated successfully")
                return

        self.table[index].append([key, value])
        print("Key inserted successfully")

    def search(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                print("Key found. Value =", item[1])
                return

        print("Key not found")

    def delete(self, key):
        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                print("Key deleted successfully")
                return

        print("Key not found")

    def display(self):
        print("\nHash Table:")

        for i in range(self.size):
            print(i, "->", self.table[i])

ht = HashTable()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        value = input("Enter value: ")
        ht.insert(key, value)

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