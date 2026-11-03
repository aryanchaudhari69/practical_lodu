def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1


def binary_search(ids, target):
    low = 0
    high = len(ids) - 1

    while low <= high:
        mid = (low + high) // 2

        if ids[mid] == target:
            return mid

        elif ids[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1



n = int(input("Enter number of customer IDs: "))

customer_ids = []

for i in range(n):
    account_id = int(input("Enter customer ID: "))
    customer_ids.append(account_id)

target = int(input("Enter ID to search: "))


result = linear_search(customer_ids, target)

if result != -1:
    print("\nLinear Search: ID found")
else:
    print("\nLinear Search: ID not found")

sorted_ids = sorted(customer_ids)

print("Sorted IDs:", sorted_ids)

result = binary_search(sorted_ids, target)

if result != -1:
    print("Binary Search: ID found")
else:
    print("Binary Search: ID not found")