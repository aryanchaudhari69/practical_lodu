def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


n = int(input("Enter number of employees: "))

salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)

selection_result = selection_sort(salaries.copy())

print("\nSalaries after Selection Sort:")
print(selection_result)

bubble_result = bubble_sort(salaries.copy())

print("\nSalaries after Bubble Sort:")
print(bubble_result)

print("\nTop 5 Highest Salaries:")

top_five = bubble_result[-5:][::-1]

for salary in top_five:
    print(salary)