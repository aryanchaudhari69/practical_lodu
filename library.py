members = {
    "Amit": 3,
    "Rahul": 0,
    "Riya": 5,
    "Neha": 2,
    "Karan": 0
}

books = {
    "Python": 8,
    "DSA": 12,
    "Java": 12,
    "DBMS": 5,
    "CN": 3
}


total = sum(members.values())
average = total / len(members)

print("Average books borrowed:", average)


max_borrow = max(books.values())
min_borrow = min(books.values())

highest_books = []
lowest_books = []

for book, count in books.items():

    if count == max_borrow:
        highest_books.append(book)

    if count == min_borrow:
        lowest_books.append(book)

print("\nHighest borrowed book(s):", highest_books)
print("Number of borrowings:", max_borrow)

print("\nLowest borrowed book(s):", lowest_books)
print("Number of borrowings:", min_borrow)


zero_count = 0

for count in members.values():
    if count == 0:
        zero_count += 1

print("\nMembers who borrowed no books:", zero_count)

print("\nMost frequently borrowed book(s):")

for book, count in books.items():
    if count == max_borrow:
        print(book, "->", count, "times")